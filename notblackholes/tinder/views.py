import os
from django.shortcuts import render

from tinder.src.DbController import DbController
from tinder.src.PlotBuilder import PlotBuilder
from tinder.src.FitsLoader import FitsLoader

from tinder.models import Galaxy

controller = DbController()


def generate_plot(galaxy):
    xs, ys = FitsLoader().load_fits(os.path.join(galaxy.original_root_extension, galaxy.file_url))
    div = PlotBuilder().build(xs, ys)

    return div


def index(request):
    return render(request, 'about.html')


def labeller(request):
    if request.method == "POST":
        is_wr = request.POST['is_wr']
        id = request.POST['id']

        if is_wr != "SKIP":
            controller.update_human_label(id, is_wr)

    galaxy = controller.next_unlabeled_galaxy()

    if galaxy:
        galaxy_id = galaxy.id
        plot_div = generate_plot(galaxy)
    else:
        galaxy_id = None
        plot_div = "All of the Galaxies have been labeled. Thank You"

    return render(request, 'labeller.html', {'someplot': plot_div, 'id': galaxy_id})


def affirmation(request):
    if request.method == "POST":
        id = request.args['id']
        new_wr = request.args['is_wr']
        print(f"ID: {id}, label: {new_wr}")
        controller.update_machine_affirmation(id, new_wr)

    galaxy = controller.next_machine_labeled_galaxy()
    if galaxy:
        galaxy_id = galaxy.id

        someplotdiv = generate_plot(galaxy)
        machine_label = galaxy.tf_label
    else:
        galaxy_id = None
        someplotdiv = "There are no machine labels yet"
        machine_label = None

    return render(request, 'affirmation.html', {'someplot': someplotdiv, 'id': galaxy_id, 'answer': machine_label})


def galaxies(request):
    galaxyList = Galaxy.objects.all()

    return render(request, 'galaxies.html', {'galaxies': galaxyList})
