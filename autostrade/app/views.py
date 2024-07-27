from django.http import HttpResponse
from django.template import loader
import app.customlib
from app.forms import ComuneForm

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def comune(request):
	if request.method == "POST":
		listacomuni = app.customlib.getDataListSearch("comune", request)
	else:
		listacomuni = app.customlib.getDataList("comune")
		
	listaUnica = []
	
	for comune in listacomuni:
		if comune[1] not in listaUnica:
			listaUnica.append(comune[1])

	listaUnica.sort()

	context = {"comuni" : listacomuni, "listaCodiciProvince" : listaUnica}
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

def test(request):
	if request.method == "POST":
		form = ComuneForm(request.POST)
		listacomuni = app.customlib.getDataListSearch("comune", request)
	else:
		listacomuni = app.customlib.getDataList("comune")
		form = ComuneForm()
		
	listaUnica = []
	
	for comune in listacomuni:
		if comune[1] not in listaUnica:
			listaUnica.append(comune[1])

	listaUnica.sort()

	context = {"comuni" : listacomuni, "listaCodiciProvince" : listaUnica, "form": form}
	template = loader.get_template("test.html")
	return HttpResponse(template.render(context, request))

