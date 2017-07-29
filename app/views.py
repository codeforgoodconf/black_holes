from flask import render_template

from app import app
from app.source.FitsLoader import FitsLoader
from app.source.PlotBuilder import PlotBuilder


@app.route("/")
@app.route("/index")
def hello():
    someplotdiv = generate_plot(5)
    return render_template("homepage.html", someplot=someplotdiv) #Hello World"

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/helloworld", methods=["GET"])
def new_function():
    return "My name is world, hello"


@app.route("/unlabeled_samples")
def unlabled_samples():

    return "return a plot that has the unlabeled dataset"


def generate_plot(id):
    xs, ys = FitsLoader().load_fits("spectrum_data/spec-1342-52793-0537.fits")
    div = PlotBuilder().build(xs, ys)

    return div




