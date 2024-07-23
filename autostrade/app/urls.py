from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("comune", views.comune, name="comune"),
    path("casello", views.casello, name="casello"),
    path("autostrada", views.autostrada, name="autostrada"),
    path("test", views.test, name="test"),
]
