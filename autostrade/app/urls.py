from django.urls import path

from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path("landingpage", views.landingpage, name="landingpage"),
    path("comune", views.comune, name="comune"),
    path("casello", views.casello, name="casello"),
    path("autostrada", views.autostrada, name="autostrada"),
	path("api_modifica", views.api_modifica, name="api_modifica"),
	path("api_elimina", views.api_elimina, name="api_elimina"),
	path("api_aggiungi", views.api_aggiungi, name="api_aggiungi"),
    path("crediti", views.crediti, name="crediti"),
    path("licenza", views.licenza, name="licenza")
]
