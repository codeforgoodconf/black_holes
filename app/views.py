from flask import render_template

from app import app
from app.source.FitsLoader import FitsLoader
from app.source.PlotBuilder import PlotBuilder
from app.db import db, Galaxy


@app.route("/")
@app.route("/index")
def hello():
    someplotdiv = generate_plot()
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
    galaxy = Galaxy.query.get(id)
    xs, ys = FitsLoader().load_fits(galaxy.file_url)
    div = PlotBuilder().build(xs, ys)

    return div

@app.route("/galaxy")
def get_galaxies():
    galaxyList = Galaxy.query.all()

    return render_template("galaxies.html", galaxies = galaxyList)
