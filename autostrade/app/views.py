from email import contentmanager
import traceback
from urllib import request
from django.http import HttpResponse
from django.template import loader
import app.customlib
from app.forms import AutostradaForm, CaselloForm, ComuneForm, ComuneModalForm

#################################################
# View Index
#################################################
def index(request):
	#return HttpResponse("Hello, world. You're at the polls index.")
	template = loader.get_template("index.html")
	return HttpResponse(template.render())

def landingpage(request):
	template = loader.get_template("landingpage.html")
	return HttpResponse(template.render())

#################################################
# View Comune
#################################################
def comune(request):
	try:
		if request.method == "POST":
			form = ComuneForm(request.POST)
			listaelementi = app.customlib.getDataListSearch("comune", request)
		else:
			listaelementi = app.customlib.getDataList("comune")
			form = ComuneForm()
		formModal = ComuneModalForm()
		context = {"listaelementi" : listaelementi, "form": form, "formModal": formModal}
		template = loader.get_template("comune.html")
		return HttpResponse(template.render(context, request))
	except Exception as err:
		context = {"pagina": "Comune", "stacktrace": traceback.format_exc()}
		template = loader.get_template("userError.html")
		return HttpResponse(template.render(context))

#################################################
# View Casello
#################################################
def casello(request):
	try:
		if request.method == "POST":
			form = CaselloForm(request.POST)
			listaelementi = app.customlib.getDataListSearch("casello", request)
		else:
			listaelementi = app.customlib.getDataList("casello")
			form = CaselloForm()
		
		for i in range(listaelementi.__len__()-1):
			elemento = listaelementi[i]
			if elemento[7] != "NULL":
				elemento_split:list[str] = elemento[7].split("-")
				data = elemento_split[2] + "/" + elemento_split[1] + "/" + elemento_split[0]
				temp_elemento = (elemento[0],elemento[1],elemento[2],elemento[3],elemento[4],elemento[5],elemento[6],data)
				listaelementi[i] = temp_elemento

		context = {"listaelementi" : listaelementi, "form": form}
		template = loader.get_template("casello.html")
		return HttpResponse(template.render(context, request))
	except Exception as err:
		context = {"pagina": "Casello", "stacktrace": traceback.format_exc()}
		template = loader.get_template("userError.html")
		return HttpResponse(template.render(context))

#################################################
# View Autostrada
#################################################
def autostrada(request):
	try:
		if request.method == "POST":
			form = AutostradaForm(request.POST)
			listaelementi = app.customlib.getDataListSearch("autostrada", request)
		else:
			listaelementi = app.customlib.getDataList("autostrada")
			form = AutostradaForm()

		context = {"listaelementi" : listaelementi, "form": form}
		template = loader.get_template("autostrada.html")
		return HttpResponse(template.render(context, request))
	except Exception as err:
		context = {"pagina": "Autostrada", "stacktrace": traceback.format_exc()}
		template = loader.get_template("userError.html")
		return HttpResponse(template.render(context))

#################################################
# View Crediti e Licenza
#################################################
def crediti(request):
	template = loader.get_template("crediti.html")
	return HttpResponse(template.render())

def licenza(request):
	template = loader.get_template("licenza.html")
	return HttpResponse(template.render())

#################################################
# View api_modifica
#################################################
def api_modifica(request):
	app.customlib.updateDataTable("comune", request)
	template = loader.get_template("api_generic.html")
	return HttpResponse(template.render())

#################################################
# View api_elimina
#################################################
def api_elimina(request):
	app.customlib.removeDataTable("comune", request)
	template = loader.get_template("api_generic.html")
	return HttpResponse(template.render())

#################################################
# View api_aggiungi
#################################################
def api_aggiungi(request):
	app.customlib.addDataTable("comune", request)
	template = loader.get_template("api_generic.html")
	return HttpResponse(template.render())

#################################################
# View Test
#################################################
def test(request):
	if request.method == "POST":
		form = ComuneForm(request.POST)
		listaelementi = app.customlib.getDataListSearch("comune", request)
	else:
		listaelementi = app.customlib.getDataList("comune")
		form = ComuneForm()

	listaUnica = []

	for comune in listaelementi:
		if comune[1] not in listaUnica:
			listaUnica.append(comune[1])

	listaUnica.sort()

	context = {"comuni" : listaelementi, "form": form}
	template = loader.get_template("test.html")
	return HttpResponse(template.render(context, request))

#################################################
# View userError
#################################################
def usererror(request):
	context = {"pagina": "usererror"}
	template = loader.get_template("userError.html")
	return HttpResponse(template.render(context))