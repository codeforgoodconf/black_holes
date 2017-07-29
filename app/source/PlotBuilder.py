# takes a list of x-values and a list of y-values and a title for the plot and returns a div
# NOTE: include plotly js script above this div for it to work


import random
import plotly

from plotly.graph_objs import Scatter, Layout


# lower limit = 4200
# upper limit = 5300

class PlotBuilder:
    def build(self, x, y, title=""):
        div = plotly.offline.plot({
            "data": [Scatter(x=x, y=y)],
            "layout": Layout(title=title,

                             xaxis=dict(range=[4200, 5300]),
                             yaxis=dict(range=[0.5, 2]),
                             )
        }, output_type='div', include_plotlyjs=False)

        return div

    def random_plot(self):
        x = list(range(10))
        y = [random.random() for _ in x]

        div = self.build(x, y)
        return div
