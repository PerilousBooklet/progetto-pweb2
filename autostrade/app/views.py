from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def autostrada(request):
    template = loader.get_template('autostrada.html')
    return HttpResponse(template.render)


def casello(request):
    template = loader.get_template('casello.html')
    return HttpResponse(template.render)


def comune(request):
    template = loader.get_template('comune.html')
    return HttpResponse(template.render)


def licenza(request):
    template = loader.get_template('licenza.html')
    return HttpResponse(template.render)


def crediti(request):
    template = loader.get_template('crediti.html')
    return HttpResponse(template.render)
