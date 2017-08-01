import pytest


from app.source.FitsLoader import FitsLoader


def test_loaded():
    fl = FitsLoader()
    fits = fl.load_fits("spec-1342-52793-0537")

    assert isinstance(fits, tuple)
    assert len(fits) == 2




