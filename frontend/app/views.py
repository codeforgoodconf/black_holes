import json

from flask import render_template, request, redirect

from app import app
from app.source.FitsLoader import FitsLoader
from app.source.PlotBuilder import PlotBuilder
from app.db import Galaxy
from app.db.controls import DbController

controller = DbController()


def add_machine_labels(predictions):
    for filename, value in predictions.items():
        print(f"File: {filename}, value: {value}")
        controller.add_machine_label(filename, value)


def generate_plot(galaxy):
    xs, ys = FitsLoader().load_fits(galaxy.file_url)
    div = PlotBuilder().build(xs, ys)

    return div


@app.route("/")
@app.route("/index")
def index():
    return render_template("about.html")


@app.route("/labeler")
def labels():
    galaxy = controller.next_unlabeled_galaxy()

    if galaxy:
        galaxy_id = galaxy.id
        plot_div = generate_plot(galaxy)
    else:
        galaxy_id = None
        plot_div = "All of the Galaxies have been labeled. Thank You"

    return render_template("labeller.html", someplot=plot_div, id=galaxy_id)


@app.route("/add_label")
def update_label():
    id = request.args['id']
    new_wr = request.args['is_wr']
    print(f"ID: {id}, label: {new_wr}")
    DbController().update_human_label(id, new_wr)

    return redirect('/labeler')


@app.route("/affirmation")
def check_machine():
    galaxy = controller.next_machine_labeled_galaxy()
    if galaxy:
        galaxy_id = galaxy.id

        someplotdiv = generate_plot(galaxy)
        machine_label = galaxy.tf_label
    else:
        galaxy_id = None
        someplotdiv = "There are no machine labels yet"
        machine_label = None

    return render_template("affirmation.html", someplot=someplotdiv, id=galaxy_id, answer=machine_label)


@app.route("/verify_machine_label")
def verify_label():
    id = request.args['id']
    new_wr = request.args['is_wr']
    print(f"ID: {id}, label: {new_wr}")
    DbController().update_human_label(id, new_wr)
    return redirect('/affirmation')


@app.route("/galaxy")
def get_galaxies():
    galaxyList = Galaxy.query.all()
    return render_template("galaxies.html", galaxies=galaxyList)


@app.route("/predict", methods=["GET", "POST"])
def machine_labels():
    """
        Receive machine predictions over server, add labels to db

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

    predictions = request.json
    if 'predictions' in predictions:
        add_machine_labels(predictions['predictions'])

    return json.dumps(request.json)
