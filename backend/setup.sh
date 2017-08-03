#!/usr/bin/env bash

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/accessSpectra/loadFromDrive.py
tar -xvzf data/raw_data/blackhole_spectra.tar.gz -C data/raw_data
