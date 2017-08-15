from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^labeller', views.labeller, name='labeller'),
    url(r'^galaxies', views.galaxies, name='galaxies'),
    url(r'^affirmation', views.affirmation, name='affirmation')
]