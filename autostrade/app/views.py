import traceback
from urllib import request
from django.http import HttpResponse
from django.template import loader
import app.customlib
from app.forms import AutostradaForm, CaselloForm, ComuneForm, ComuneModalDeleteForm, ComuneModalEditForm, ComuneModalInsertForm

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

# -3 = fallimento eliminazione
# -2 = fallimento modifica
# -1 = fallimento inserimento
#  0 = stato iniziale, netruale
#  1 = successo inserimento
#  2 = successo modifica
#  3 = successo eliminazione

def comune(request, success=0):
    try:
        post_data:dict[str,str] = request.POST
        if request.method == "POST":
            form = ComuneForm(post_data)
            listaelementi = app.customlib.getDataListSearch("comune", post_data)
        else:
            if request.GET.get('codice') is not None:
                get_codice = request.GET.get('codice')
                form = ComuneForm({"codice": get_codice})
                listaelementi = app.customlib.getDataListSearch("comune", {"codice": get_codice})
            else:
                listaelementi = app.customlib.getDataList("comune")
                form = ComuneForm()
        formModalEdit = ComuneModalEditForm()
        formModalDelete = ComuneModalDeleteForm()
        formModalInsert = ComuneModalInsertForm()
        context = {"listaelementi" : listaelementi, "form": form, "formModal": formModalEdit, "formDeleteModal": formModalDelete, "formInsertModal": formModalInsert, "success": success}
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
		post_data:dict[str,str] = request.POST

		if request.method == "POST":
			form = CaselloForm(post_data)
			listaelementi = app.customlib.getDataListSearch("casello", post_data)
		else:
			if request.GET.get('comune') is not None:
				get_comune = request.GET.get('comune')
				form = CaselloForm({"comune": get_comune})
				listaelementi = app.customlib.getDataListSearch("casello", {"comune": get_comune})
			elif request.GET.get('autostrada') is not None:
				get_autostrada = request.GET.get('autostrada')
				form = CaselloForm({"cod_naz": get_autostrada})
				listaelementi = app.customlib.getDataListSearch("casello", {"cod_naz": get_autostrada})
			else:
				form = CaselloForm()
				listaelementi = app.customlib.getDataList("casello")
		
		for i in range(len(listaelementi)):
			elemento = list(listaelementi[i])
			if elemento[9] != "NULL":
				elemento_split:list[str] = elemento[9].split("-")
				elemento[9] = elemento_split[2] + "/" + elemento_split[1] + "/" + elemento_split[0]
				listaelementi[i] = elemento

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
		post_data:dict[str,str] = request.POST
		if request.method == "POST":
			form = AutostradaForm(post_data)
			listaelementi = app.customlib.getDataListSearch("autostrada", post_data)
		else:
			if request.GET.get('cod_naz') is not None:
				get_cod_naz = request.GET.get('cod_naz')
				form = AutostradaForm({"cod_naz": get_cod_naz})
				listaelementi = app.customlib.getDataListSearch("autostrada", {"cod_naz": get_cod_naz})
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
# View api_aggiungi
#################################################
def api_aggiungi(request):
	try:
		app.customlib.addDataTable("comune", request)
		return comune(request, 1)
	except Exception as err:
		return comune(request, -1)

#################################################
# View api_modifica
#################################################
def api_modifica(request):
	try:
		app.customlib.updateDataTable("comune", request)
		return comune(request, 2)
	except Exception as err:
		return comune(request, -2)

#################################################
# View api_elimina
#################################################
def api_elimina(request):
	try:
		app.customlib.removeDataTable("comune", request)
		return comune(request, 3)
	except Exception as err:
		return comune(request, -3)

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