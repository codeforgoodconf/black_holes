import pytest

from app.source.PlotBuilder import PlotBuilder



def test_returns_div():
    pb = PlotBuilder()

    # generate a plot and confirm it is a div

    div = pb.random_plot()
    assert div[:4] == "<div"




