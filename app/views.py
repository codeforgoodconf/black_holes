from flask import render_template, request, redirect

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


@app.route("/add_label")
def update_label():
    id = request.args['id']
    new_wr = request.args['is_wr']


    return redirect('/')


def generate_plot():
    galaxyList = Galaxy.query.all()
    galaxy = galaxyList[0]
    xs, ys = FitsLoader().load_fits(galaxy.file_url)
    div = PlotBuilder().build(xs, ys)

    return div

@app.route("/galaxy")
def get_galaxies():
    return render_template("galaxies.html", galaxies = galaxyList)
