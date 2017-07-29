

from astropy.io import fits

from os import listdir
from os.path import isfile, join

path = './raw_data/He2FilteringFiles/'

file_paths = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

for file_path in file_paths:
    hdulist = fits.open(file_path)
    flux = hdulist[1].data['flux']
    
    
    
    
    










