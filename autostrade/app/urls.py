from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("licenza/", views.licenza, name='licenza'),
    path("crediti/", views.crediti, name='crediti'),
    path("autostrada/", views.autostrada, name='autostrada'),
    path("casello/", views.casello, name='casello'),
    path("comune/", views.comune, name='comune')
]
