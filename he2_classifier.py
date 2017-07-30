

from astropy.io import fits
import numpy as np

#from os import listdir
#from os.path import isfile, join

import os

import datetime


def lerp(a, b, t):
    return a*(1.0-t) + b*t


def remove_slope(wls, fxs):
    
    edge_wl = [4517, 4785]
    
    ew = 50.0
    ewo2 = ew/2

    edge_sum = [0, 0]
    edge_points = [0, 0]
    for i, edge in enumerate(edge_wl):
        for j, fx in enumerate(fxs):
            if edge-ewo2 < wls[j] < edge+ewo2:
                edge_sum[i] += fx
                edge_points[i] += 1
    edge_ave = [edge_sum[i]/edge_points[i] for i in range(2)]

    slope = (edge_ave[1]-edge_ave[0])/(edge_wl[1]-edge_wl[0])
    y_int = edge_ave[0] - slope*edge_wl[0]
    
    for i, wav_val in enumerate(wls):
        fxs[i] -= (slope*wav_val + y_int)

def gaussian_smooth(wav_rest, fwav):

    kernel_width = 2
    stepsize = wav_rest[1]-wav_rest[0]

    num_steps = int(kernel_width/stepsize * 3) #Calculate out to 1%
    kernel = [np.exp(-((i*stepsize)**2)/(2*kernel_width**2))
        for i in range(num_steps)]
    kernel = kernel[::-1] + kernel[1:]
    kernel = [i/np.sum(kernel) for i in kernel] #normalize the kernel

    fwav_smooth = [0]*(len(fwav)-len(kernel)+1)
    wav_rest_smooth = [0]*(len(fwav)-len(kernel)+1)
    for i in range(len(fwav_smooth)):
        use_fwav_vals = fwav[i:i+len(kernel)]
        fwav_smooth[i] = np.sum([use_fwav_vals[j]*kernel[j]
            for j in range(len(kernel))])
        wav_rest_smooth[i] = wav_rest[i+int((len(kernel)-1)/2)]
    
    return wav_rest_smooth, fwav_smooth


def crop_data(wls, fxs, wl_min, wl_max):
    wlsc = [wls[i] for i in range(len(wls)) if wl_min < wls[i] < wl_max]
    fxsc = [fxs[i] for i in range(len(wls)) if wl_min < wls[i] < wl_max]
    return wlsc, fxsc


def is_he2(wls, fxs):
    wl_min = 4686-5
    wl_max = 4686+5
    difference = 0
    for i,wl in enumerate(wls):
        if wl_min < wl < wl_max:
            difference += fxs[i]
    return difference > 0


def standardize_domain(wls, fxs, wl_min, wl_max, n_samples):
    new_wls = [lerp(wl_min, wl_max, i/(n_samples-1)) for i in range(n_samples)]
    new_fxs = np.interp(new_wls, wls, fxs)
    return new_wls, new_fxs


def process_file(path, wl_min, wl_max, n_samples, check_he2=False):
    hdulist = fits.open(path)
    wls = 10**hdulist[1].data['loglam']
    fxs = hdulist[1].data['flux']
    z = hdulist[2].data['z']
    wls = wls / (1 + z)
    if wl_min < wls[0] or wl_max > wls[-1]:
        return None
    remove_slope(wls, fxs)
    wls, fxs = gaussian_smooth(wls, fxs)
    wls, fxs = crop_data(wls, fxs, wl_min, wl_max)
    wls, fxs = standardize_domain(wls, fxs, wl_min, wl_max, n_samples)
    if check_he2:
        if is_he2(wls, fxs):
            print('including ' + path)
            return fxs
        print('excluding ' + path)
        return None
    return fxs


def process_folder(path, wl_min, wl_max, n_samples, label=None, check_he2=False):
    r = []
    r.append(['wl_'+str(lerp(wl_min, wl_max, i/(n_samples-1))) for i in range(n_samples)])
    r[0].insert(0, 'label')
    r[0].insert(0, 'file')
    
    file_paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.fits')]
    for file_path in file_paths:
        flux = process_file(file_path, wl_min, wl_max, n_samples, check_he2)
        
        if flux is not None:
            flux = list(flux)
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            if label is None:
                flux.insert(0, '?')
            else:
                flux.insert(0, label)
            flux.insert(0, file_name)
            r.append(flux)
    return r


def save_csv(name, table):
    name = name+'-'+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.csv'
    with open(name, 'w') as file:
        for i in range(len(table)):
            for j in range(len(table[i])):
                file.write(str(table[i][j]))
                if j < len(table[i])-1:
                    file.write(',')
            file.write('\n')


def main():
    
    wl_min = 4686-150
    wl_max = 4686+150
    n_samples = 300
    
    table_negative = process_folder('./raw_data/hasHe2_NoWR/', wl_min, wl_max, n_samples, 0, False)
    table_positive = process_folder('./raw_data/Brinchmann08_spectra', wl_min, wl_max, n_samples, 1, False)
    table_negative.extend(table_positive)
    save_csv('./processed_data/classified', table_negative)
    
    table_he2 = process_folder('./raw_data/firstThousandSpectra/thousandSpectra/', wl_min, wl_max, n_samples, label=None, check_he2=True)
    save_csv('./processed_data/unclassified-he2', table_he2)
    
    
    
    
        

if __name__ == '__main__':
    main()


