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
t.show_in_browser()
