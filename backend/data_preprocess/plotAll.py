import numpy as np
from astropy.io import fits
from astropy.table import Table
print "ok"
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from astropy.io import fits
import sys
import os

def plotAll(targetDir, toPlot):
	print "alright %s" % toPlot
	for f in toPlot:
		if "Brinchmann08_Tab3and5.fits" in f:
			continue
		if "negativeSpecctra" in f:
			continue
		target = f.replace('raw_data/Brinchmann08_spectra/','positive-').replace('raw_data/hasHe2_NoWR/','negative-').replace('raw_data/He2FilteringFiles/','unknown-').replace('raw_data/firstThousandGal/','unknown-').replace('.fits', '.png')
		target = targetDir + "/" + target
		print "testing file"
		if os.path.isfile(target):
			print "skipping"
			continue
		print "filetested!"
		print "writing %s" % target
		plotImage(f, target)
	
def plotImage(f, target):
	hdulist = fits.open(f)
	dat, hdr = hdulist[1].data, hdulist[0].header
	z = hdulist[2].data['Z'][0]    # This is the redshift

	hdulist.close()
	wav_rest = 10**(dat['loglam'])/(1+z)    # Convert to rest-frame
	fwav = dat['flux']


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

	# idx = np.where((wav > 4200) & (wav < 5200))

	# plt.plot(np.log(wav[idx]), np.log(flx[idx]), c='k', linestyle='steps-mid')

	#plt.show()
	
	plt.savefig(target)

targetDir = sys.argv[1]
toPlot = sys.argv[2:]
plotAll(targetDir, toPlot)