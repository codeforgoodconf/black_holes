from flask import render_template

from app import app

@app.route("/")
@app.route("/index")
def hello():
    someplotdiv = "THERE IS THE BIG PLT"

    return render_template("homepage.html", someplot=someplotdiv) #Hello World"



@app.route("/helloworld", methods=["GET"])
def new_function():
    return "My name is world, hello"


@app.route("/unlabeled_samples")
def unlabled_samples():

    return "return a plot that has the unlabeled dataset"

