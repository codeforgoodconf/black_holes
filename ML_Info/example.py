import numpy as np
from astropy.io import fits
from astropy.table import Table
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

"""
A simple example of some of AstroPy's functionality with Flexible Image 
Transport System (FITS) files. This script will load a random spectrum from 
Brinchmann et al. (2008): http://adsabs.harvard.edu/abs/2008A%26A...485..657B 
so that you can see where the HeII 4686 line and Wolf-Rayet (WR) "blue bump" is 
found. While the HeII line is easy to spot and parameterize, the shape and width 
of the blue bump varies quite a bit. Hence why I'm hoping machine learning can 
help make a more complete sample of WR galaxies from the SDSS Legacy (DR7) 
survey.
"""

spec_dir = './Brinchmann08_spectra/'

t = Table.read('Brinchmann08_Tab3and5.fits')

# Pick a random WR galaxy and plot it
idx = np.random.choice(len(t))

# Or pick the WR galaxy with the highest equivalent width of the WR blue bump
# Equivalent width definition: https://en.wikipedia.org/wiki/Equivalent_width

#idx = np.where(t['EWBB'] == max(t['EWBB']))[0][0]

SpecID = t[idx]['SpecID']

# Fix the zero issue with the Brinchmann table
SpecID = '%s0%s' % (SpecID[:-3], SpecID[-3:])

# Open spectrum FITS file
spec_path = spec_dir + 'spec-%s.fits' % SpecID

print spec_path
hdulist = fits.open(spec_path)

# A simple demonstration of the FITS file structure
print "\nA simple demonstration of the SDSS spectrum FITS file stucture"
print "\nHDU 0 data: "
print hdulist[0].data
print "... Spectral files have no 2D array (e.g., an image)"
print "\nFiber right ascension: %s" % hdulist[0].header['PLUG_RA']
print "Fiber declination: %s" % hdulist[0].header['PLUG_DEC']
print "... HDU 0 header contains observation information."
print ("\nHere's the spectrum.\nDotted line: where HeII 4686 is found." +
       "\nBlue shading: where the WR blue bump is found.")

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
