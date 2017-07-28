import numpy as np
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt

def get_data():

    spec_dir = '../ML_Info/Brinchmann08_spectra/'

    t = Table.read('../ML_Info/Brinchmann08_Tab3and5.fits')

    #len(t) = 570
    idx = 49

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

    keep_wav = [4686-200, 4686+200]
    wav_rest_cropped = [wav_rest[i] for i in range(len(wav_rest))
        if (wav_rest[i] > keep_wav[0] and wav_rest[i] < keep_wav[1])]
    fwav_cropped = [fwav[i] for i in range(len(wav_rest))
        if (wav_rest[i] > keep_wav[0] and wav_rest[i] < keep_wav[1])]

    wav_rest = wav_rest_cropped
    fwav = fwav_cropped

    hdulist.close()

    return wav_rest, fwav, SpecID


def remove_slope(wav_rest, fwav):

    bump_edges = [4686-150, 4686+150]
    edge_region_width = 20.

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

    kernel_width = 3. #kernel width in angstroms
    stepsize = wav_rest[1]-wav_rest[0]
    num_steps = int(kernel_width/stepsize * 3) #Calculate out to 1%
    kernel = [np.exp(-((i*stepsize)**2)/(2*kernel_width**2))
        for i in range(num_steps)]
    kernel = kernel[::-1] + kernel[1:]
    kernel = [i/np.sum(kernel) for i in kernel] #normalize the kernel

    fwav_norm = [0]*(len(fwav)-len(kernel)+1)
    wav_rest_norm = [0]*(len(fwav)-len(kernel)+1)
    for i in range(len(fwav_norm)):
        use_fwav_vals = fwav[i:i+len(kernel)]
        fwav_norm[i] = np.sum([use_fwav_vals[j]*kernel[j]
            for j in range(len(kernel))])
        wav_rest_norm[i] = wav_rest[i+int((len(kernel)-1)/2)]

    wav_rest = wav_rest_norm
    fwav = fwav_norm
    return wav_rest, fwav

def plot(wav_rest,fwav):

    plt.plot(wav_rest,fwav)
    plt.show()

def save_result():
    wav_rest, fwav, SpecID = get_data()
    wav_rest, fwav = remove_slope(wav_rest, fwav)
    wav_rest, fwav = gaussian_smooth(wav_rest, fwav)

    output_filename = 'spec-%s.csv' % SpecID

    output = open(output_filename,"w")
    output = open(output_filename,"a")
    for val in fwav:
        output.write(str(val)+',')
    output.close()

    plot(wav_rest,fwav)




if __name__ == '__main__':
    save_result()
