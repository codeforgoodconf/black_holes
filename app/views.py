from flask import render_template, request

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

@app.route("/next", methods=["GET"])
def new_function():
    id = request.args[0]
    if is_af != "skip":
        if is_af == "true":
            is_af = True
        else:
            is_af = False
    else:
        is_af = Null
    return "My name is world, hello"


@app.route("/unlabeled_samples")
def unlabled_samples():

    return "return a plot that has the unlabeled dataset"


def generate_plot():
    galaxyList = Galaxy.query.all()
    galaxy = galaxyList[0]
    xs, ys = FitsLoader().load_fits(galaxy.file_url)
    div = PlotBuilder().build(xs, ys)

    return div

@app.route("/galaxy")
def get_galaxies():
    return render_template("galaxies.html", galaxies = galaxyList)
