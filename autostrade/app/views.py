from django.http import HttpResponse
from django.template import loader
import app.customlib

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def landingpage(request):
    template = loader.get_template("landingpage.html")
    return HttpResponse(template.render())

def comune(request):
    listacomuni = app.customlib.getDataList("comune")
    context = {"comuni" : listacomuni}
    template = loader.get_template("comune.html")
    return HttpResponse(template.render(context, request))

def casello(request):
    listacaselli = app.customlib.getDataList("casello")
    context = {"caselli" : listacaselli}
    template = loader.get_template("casello.html")
    return HttpResponse(template.render(context, request))

def autostrada(request):
    listaautostrade = app.customlib.getDataList("autostrada")
    context = {"autostrade" : listaautostrade}
    template = loader.get_template("autostrada.html")
    return HttpResponse(template.render(context, request))

def crediti(request):
    template = loader.get_template("crediti.html")
    return HttpResponse(template.render())

def licenza(request):
    template = loader.get_template("licenza.html")
    return HttpResponse(template.render())

# def test(request):
#     context = {"cacarot" : 1}
#     template = loader.get_template("test.html")
#     return HttpResponse(template.render(context, request))

