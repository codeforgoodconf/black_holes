import numpy as np
from astropy.io import fits



class FitsLoader:
    def load_fits(self, file_url):
        hdu = fits.open(file_url)
        dat, hdr = hdu[1].data, hdu[0].header
        z = hdu[2].data['Z'][0]    # This is the redshift
        hdu.close()

        wav_rest= 10**(dat['loglam'])/(1+z) #convert to rest frame
           # See https://en.wikipedia.org/wiki/Redshift
        fwav = dat['flux']    # Get flux density, in this case erg/cm^2/s/Angstrom.

        #xs = np.log(wav[idx])
        #ys = np.log(flx[idx])

        # Normalize the spectrum for plotting purposes.
        def find_nearest(array, value):
            """Quick nearest-value finder."""
            return int((np.abs(array - value)).argmin())

        norm = fwav[find_nearest(wav_rest, 5100)]
        fwav = fwav / norm

        return wav_rest, fwav



