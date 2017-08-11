import os
from django.shortcuts import render

from tinder.src.DbController import DbController
from tinder.src.PlotBuilder import PlotBuilder
from tinder.src.FitsLoader import FitsLoader

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
    return render(request, 'affirmation.html')


def galaxies(request):
    return render(request, 'galaxies.html')
