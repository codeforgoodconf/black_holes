import numpy as np
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt

import numpy as np
from astropy.io import fits

s = 'spec-0267-51608-0384.fits'

hdu = fits.open(s)
dat, hdr = hdu[1].data, hdu[0].header
z = hdu[2].data['Z'][0]    # This is the redshift
hdu.close()

wav = 10**(dat['loglam'])/(1+z)    # Convert to rest-frame
flx = dat['flux']

idx = np.where((wav > 4200) & (wav < 5200))

plt.plot(np.log(wav[idx]), np.log(flx[idx]), c='k', linestyle='steps-mid')

plt.show()

