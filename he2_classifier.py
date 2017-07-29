

from astropy.io import fits
import numpy as np

from os import listdir
from os.path import isfile, join

import datetime


def lerp(a, b, t):
    return a*(1.0-t) + b*t


def remove_slope(wls, fxs):
    
    edge_wl = [4517, 4785]
    ew = 50.0
    ewo2 = ew/2

    edge_sum = [0,0]
    edge_points = [0,0]
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


def crop_data(wls, fxs, wl_min, wl_max):
    wlsc = [wls[i] for i in range(len(wls)) if wl_min < wls[i] < wl_max]
    fxsc = [fxs[i] for i in range(len(wls)) if wl_min < wls[i] < wl_max]
    return wlsc, fxsc


def is_he2(wls, fxs):
    wl_min = 4686-5
    wl_max = 4686+5
    difference = 0
    for i,wl in wls:
        if wl_min < wl < wl_max:
            difference += fxs[i]
    return difference > 0


def standardize_domain(wls, fxs, wl_min, wl_max, n_samples):
    new_wls = [lerp(wl_min, wl_max, i/(n_samples-1)) for i in range(n_samples)]
    new_fxs = np.interp(new_wls, wls, fxs)
    return new_wls, new_fxs


def process_file(path, wl_min, wl_max, n_samples):
    hdulist = fits.open(path)
    wls = 10**hdulist[1].data['loglam']
    fxs = hdulist[1].data['flux']
    z = hdulist[2].data['z']
    wls = wls / (1 + z)
    remove_slope(wls, fxs)
    wls, fxs = crop_data(wls, fxs, wl_min, wl_max)
    wls, fxs = standardize_domain(wls, fxs, wl_min, wl_max, n_samples)
    #if is_he2(wls, fxs):
    return fxs


def process_folder(path, wl_min, wl_max, n_samples, label):
    r = []
    file_paths = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.endswith('.fits')]
    for file_path in file_paths:
        flux = process_file(file_path, wl_min, wl_max, n_samples)
        if flux is None:
            print('excluding ' + file_path)
        else:
            print('including ' + file_path)
            flux = list(flux)
            flux.append(label)
            r.append(flux)
    return r


def save_csv(table):
    name = 'compiled'+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.csv'
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
    n_samples = 100
    
    table_negative = process_folder('./raw_data/hasHe2_NoWR/', wl_min, wl_max, n_samples, 0)
    table_positive = process_folder('./raw_data/Brinchmann08_spectra', wl_min, wl_max, n_samples, 1)
    
    table_negative.extend(table_negative)
    save_csv(table_negative)
        

if __name__ == '__main__':
    main()


