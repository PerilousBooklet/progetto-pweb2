from django.http import HttpResponse
from django.template import loader
import app.customlib
import collections

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def comune(request):
    listacomuni = app.customlib.getDataList("comune")
    templateTuple = collections.namedtuple("templateTuple", ("codice", "provincia", "nome"))
    # print (listacomuni)
    context = {"comuni" : listacomuni}
    template = loader.get_template("comune.html")
    return HttpResponse(template.render(context, request))

def casello(request):
    context = {}
    template = loader.get_template("casello.html")
    return HttpResponse(template.render(context, request))

def autostrada(request):
    context = {}
    template = loader.get_template("autostrada.html")
    return HttpResponse(template.render(context, request))

# def test(request):
#     context = {"cacarot" : 1}
#     template = loader.get_template("test.html")
#     return HttpResponse(template.render(context, request))

