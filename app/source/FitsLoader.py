import numpy as np
from astropy.io import fits



class FitsLoader:
    def load_fits(self, file_url):
        hdu = fits.open(file_url)
        dat, hdr = hdu[1].data, hdu[0].header
        z = hdu[2].data['Z'][0]    # This is the redshift
        hdu.close()

        wav = 10**(dat['loglam'])/(1+z)    # Convert to rest-frame
        flx = dat['flux']

        idx = np.where((wav > 4200) & (wav < 5200))

        xs = np.log(wav[idx])
        ys = np.log(flx[idx])

        return xs, ys



