import numpy as np
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt

spec_dir = '../ML_Info/Brinchmann08_spectra/'

t = Table.read('../ML_Info/Brinchmann08_Tab3and5.fits')

# Pick a random WR galaxy and plot it
#idx = np.random.choice(len(t))

#len(t) = 570
idx = 200

# Or pick the WR galaxy with the highest equivalent width of the WR blue bump
# Equivalent width definition: https://en.wikipedia.org/wiki/Equivalent_width

#idx = np.where(t['EWBB'] == max(t['EWBB']))[0][0]

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
fwav = fwav / norm

ax.plot(wav_rest, fwav, c='k', linestyle='steps-mid')

# Stretch the plot to accentuate the WR blue bump
ax.axis([4200, 5300, 0.5, 2])

ax.set_xlabel('Ang')
ax.set_ylabel('%s / %s' % (hdulist[0].header['BUNIT'], norm))

ax.axvspan(4686-150, 4686+150, alpha=0.3, color='b')
ax.axvline(x=4686, color='k', linestyle=':')

plt.show()

# Close the FITS file.
hdulist.close()
