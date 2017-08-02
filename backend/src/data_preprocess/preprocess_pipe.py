import numpy as np
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import os

def get_wr_data(idx, spec_dir):

    t = Table.read('../raw_data/Brinchmann08_Tab3and5.fits')

    SpecID = t[idx]['SpecID']

    # Fix the zero issue with the Brinchmann table
    SpecID = '%s0%s' % (SpecID[:-3], SpecID[-3:])

    # Open spectrum FITS file
    spec_path = spec_dir + 'spec-%s.fits' % SpecID

    hdulist = fits.open(spec_path)

    # Get wavelength data, and correct it to the rest-frame of the galaxy:
    wav = 10**hdulist[1].data['loglam']

    z =  t[idx]['z']

    wav_rest = wav / (1 + z)    # See https://en.wikipedia.org/wiki/Redshift

    # Get flux density, in this case erg/cm^2/s/Angstrom.
    fwav = hdulist[1].data['flux']

    crop_range = [4686-250, 4686+250]
    wav_rest, fwav = crop_data(wav_rest, fwav, crop_range)

    hdulist.close()

    return wav_rest, fwav, SpecID


def get_notwr_data(idx, spec_dir, filenames):

    spec_path = spec_dir+filenames[idx]
    SpecID = spec_path[6:21]

    hdulist = fits.open(spec_path)

    # Get wavelength data
    wav_rest = 10**hdulist[1].data['loglam']

    # Get flux density, in this case erg/cm^2/s/Angstrom.
    fwav = hdulist[1].data['flux']

    crop_range = [4686-250, 4686+250]
    wav_rest, fwav = crop_data(wav_rest, fwav, crop_range)

    hdulist.close()

    return wav_rest, fwav, SpecID


def remove_slope(wav_rest, fwav):

    bump_edges = [4517, 4785]
    edge_region_width = 50.

    edge_sum = [0,0]
    edge_points = [0,0]
    for i, edge in enumerate(bump_edges):
        for j, val in enumerate(fwav):
            if (wav_rest[j] > edge - edge_region_width/2
                    and wav_rest[j] < edge + edge_region_width/2):
                edge_sum[i] += val
                edge_points[i] += 1
    edge_ave = [edge_sum[i]/edge_points[i] for i in range(2)]

    slope = (edge_ave[1]-edge_ave[0])/(bump_edges[1]-bump_edges[0])
    y_int = edge_ave[0] - (slope * bump_edges[0])

    for i, wav_val in enumerate(wav_rest):
        fwav[i] -= (slope*wav_val + y_int)

    return wav_rest, fwav


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

    wav_rest = wav_rest_smooth
    fwav = fwav_smooth

    crop_range = [4686-150, 4686+150]
    wav_rest, fwav = crop_data(wav_rest, fwav, crop_range)

    return wav_rest, fwav


def plot(wav_rest, fwav):

    plt.plot(wav_rest,fwav)
    plt.xlim([4686-150, 4686+150])
    plt.show()


def crop_data(wav_rest, fwav, crop_range):

    wav_rest_cropped = [wav_rest[i] for i in range(len(wav_rest))
        if (wav_rest[i] > crop_range[0] and wav_rest[i] < crop_range[1])]
    fwav_cropped = [fwav[i] for i in range(len(wav_rest))
        if (wav_rest[i] > crop_range[0] and wav_rest[i] < crop_range[1])]
    wav_rest = wav_rest_cropped
    fwav = fwav_cropped

    return wav_rest, fwav


def interpolate_to_std_domain(wav_rest, fwav):

    stepsize = 1.03 #similar to the native step size
    data_range = [4686-150, 4686+150]
    wav_rest_standard = [i*stepsize+data_range[0]
        for i in range(int((data_range[1]-data_range[0])/1.03)+1)]
    fwav_interp = np.interp(wav_rest_standard, wav_rest, fwav)
    wav_rest = wav_rest_standard
    fwav = fwav_interp

    return wav_rest, fwav


def save_result():

    wr_flag = 0

    if wr_flag == 1:
        data_dir = '../raw_data/Brinchmann08_spectra/'

    if wr_flag == 0:
        data_dir = '../raw_data/negativeSpectra/'

    output_filename = 'data_preprocessed.csv'
    #output = open(output_filename,"w")
    output = open(output_filename,"a")

    filenames = [name for name in os.listdir(data_dir)
        if os.path.isfile(data_dir+name)]

    for idx in range(len(filenames)):

        if wr_flag == 1:
            wav_rest, fwav, SpecID = get_wr_data(idx, data_dir)
        else:
            wav_rest, fwav, SpecID = get_notwr_data(idx, data_dir, filenames)
        wav_rest, fwav = remove_slope(wav_rest, fwav)
        wav_rest, fwav = gaussian_smooth(wav_rest, fwav)
        wav_rest, fwav = interpolate_to_std_domain(wav_rest, fwav)

        print('Saving data for observation {} out of {}'.format(idx+1,
            len(filenames)))

        #if idx != 0:
        if True:
            output.write('\n')
        output.write(str(SpecID)+','+str(wr_flag))
        for val in fwav:
            output.write(','+str(val))

    output.close()
    

if __name__ == '__main__':
    save_result()
