from flask import render_template, request, redirect

from app import app
from app.source.FitsLoader import FitsLoader
from app.source.PlotBuilder import PlotBuilder
from app.db import Galaxy
from app.db.controls import Controller

import json


@app.route("/")
@app.route("/index")
def index():
    galaxy = Controller().rand_galaxy()
    if galaxy:
        galaxy_id = galaxy.id

        someplotdiv = generate_plot(galaxy)
    else:
        galaxy_id = None
        someplotdiv = "All of the Galaxies have been labeled. Thank You"

    return render_template("homepage.html", someplot=someplotdiv, id=galaxy_id)


@app.route("/affirmation")
def check_machine():
    galaxy = Controller().machine_labeled_galaxy()
    if galaxy:
        galaxy_id = galaxy.id

        someplotdiv = generate_plot(galaxy)
        machine_label = galaxy.tf_label
    else:
        galaxy_id = None
        someplotdiv = "There are no machine labels yet"
        machine_label = None
    return render_template("affirmation.html", someplot=someplotdiv, id=galaxy_id, answer=machine_label)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/add_label")
def update_label():
    id = request.args['id']
    new_wr = request.args['is_wr']
    print(f"ID: {id}, label: {new_wr}")
    Controller().update_human_label(id, new_wr)

    return redirect('/')


@app.route("/verify_machine_label")
def verify_label():
    id = request.args['id']
    new_wr = request.args['is_wr']
    print(f"ID: {id}, label: {new_wr}")
    # Controller().update_human_label(id, new_wr)
    return redirect('/affirmation')


@app.route("/galaxy")
def get_galaxies():
    galaxyList = Galaxy.query.all()
    return render_template("galaxies.html", galaxies=galaxyList)


def generate_plot(galaxy):
    xs, ys = FitsLoader().load_fits(galaxy.file_url)
    div = PlotBuilder().build(xs, ys)

    return div


@app.route("/predict", methods=["GET", "POST"])
def machine_labels():
    """
        example:

        {
            "predictions": [
                "spec xxxx": 0.983,
                "spec xxxx": 0.983,
                "spec xxxx": 0.983,
                "spec xxxx": 0.983,
            ]
        }

    """

    print(request)
    print(request.json)

    predictions = request.json
    if 'predictions' in predictions:
        add_machine_labels(predictions['predictions'])

    return json.dumps(request.json)


def add_machine_labels(predictions):
    controller = Controller()

    for filename, value in predictions.items():
        print(f"File: {filename}, value: {value}")
        controller.add_machine_label(filename, value)
