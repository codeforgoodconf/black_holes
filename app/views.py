from flask import render_template, request, redirect

from app import app
from app.source.FitsLoader import FitsLoader
from app.source.PlotBuilder import PlotBuilder
from app.db import Galaxy
from app.db.controls import update_human_label,rand_galaxy

@app.route("/")
@app.route("/index")
def hello():
    someplotdiv = generate_plot(rand_galaxy())
    return render_template("homepage.html", someplot=someplotdiv) #Hello World"

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/add_label")
def update_label():
    id = request.args['id']
    new_wr = request.args['is_wr']
    update_human_label(id,new_wr)
    return redirect('/')


def generate_plot(galaxy):
    # galaxy = Galaxy.query.get(id)
    xs, ys = FitsLoader().load_fits(galaxy.file_url)
    div = PlotBuilder().build(xs, ys)

    return div

@app.route("/galaxy")
def get_galaxies():
    galaxyList = Galaxy.query.all()

    return render_template("galaxies.html", galaxies = galaxyList)
