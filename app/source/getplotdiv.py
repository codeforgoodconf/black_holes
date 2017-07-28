# takes a list of x-values and a list of y-values 
# and a title for the plot and returns a div
# NOTE: include plotly js script above this div for it to work

import plotly
from plotly.graph_objs import Scatter, Layout

def getdiv(x,y,title):
    return plotly.offline.plot({
    "data": [Scatter(x=x, y=y)],
    "layout": Layout(title=title)
}, output_type='div', include_plotlyjs=False)