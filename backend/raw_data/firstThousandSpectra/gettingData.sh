#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:10:33 2017

@author: samking
"""


f = open('realfirstThousandGal_samking.csv', 'r')

for line in f: 
    plate, mjd, fiberid = line.split(',')
    try:
        print('wget http://data.sdss3.org/sas/dr12/sdss/spectro/redux/26/spectra/%s/spec-%s-%s-%s.fits'%(plate.zfill(4), plate.zfill(4), mjd.zfill(5), fiberid.strip().zfill(4)))
    except:
        pass
