#!/usr/bin/env bash

# setup virtual environment - if `python` does not point to python3, then you'll have to use python3.
#   Also, if you use anaconda, you'll have to follow different steps for the venv
python -m venv venv
source venv/bin/activate


pip install -r requirements.txt

# Download spectra data from Google Drive
python src/accessSpectra/loadFromDrive.py

# Unzip the spectra data
tar -xvzf data/raw_data/blackhole_spectra.tar.gz -C data/raw_data


