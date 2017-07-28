import numpy as np
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt

def get_data():

    spec_dir = '../ML_Info/Brinchmann08_spectra/'

    t = Table.read('../ML_Info/Brinchmann08_Tab3and5.fits')

    #len(t) = 570
    idx = 300

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

    # Plotting
    fig, ax = plt.subplots()

    # Normalize the spectrum for plotting purposes.
    def find_nearest(array,value):
        """Quick nearest-value finder."""
        return int((np.abs(array-value)).argmin())

    norm = fwav[find_nearest(wav_rest, 5100)]

    return wav_rest, fwav

    hdulist.close()


def remove_slope(wav_rest, fwav):

    bump_edges = [4686-150, 4686+150]
    edge_region_width = 20.

    edge_sum = [0,0]
    edge_points = [0,0]
    for i, edge in enumerate(bump_edges):
        for j, val in enumerate(fwav):
            print(val)
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

def plot():
    wav_rest, fwav = get_data()
    wav_rest, fwav = remove_slope(wav_rest, fwav)

    plt.plot(wav_rest, fwav)
    plt.xlim([4686-150, 4686+150])
    plt.ylim([-10,10])
    plt.show()

    # Close the FITS file.
    hdulist.close()


if __name__ == '__main__':
    plot()
