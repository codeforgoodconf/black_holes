import pytest


from app.source.FitsLoader import FitsLoader


def test_loaded():
    fl = FitsLoader()
    fits = fl.load_fits("spectrum_data/spec-1342-52793-0537.fits")

    assert isinstance(fits, tuple)
    assert len(fits) == 2
    assert isinstance(fits[0], list)



