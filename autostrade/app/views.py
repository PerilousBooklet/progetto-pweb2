import traceback
from django.http import HttpResponse
from django.template import loader
import app.customlib
from app.forms import (
    AutostradaForm,
    CaselloForm,
    ComuneForm,
    ComuneModalDeleteForm,
    ComuneModalEditForm,
    ComuneModalInsertForm,
)


#################################################
# View Index
# Qui si carica il template della pagina principale
#################################################
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def landingpage(request):
    template = loader.get_template("landingpage.html")
    return HttpResponse(template.render())


#################################################
# View Comune
# Qui si carica il template della pagina dei comuni
#################################################
# Significato dei valori di success, usato per indicare quale alert usare durante gli inserimenti
# -3 = fallimento eliminazione
# -2 = fallimento modifica
# -1 = fallimento inserimento
#  0 = stato iniziale, netruale
#  1 = successo inserimento
#  2 = successo modifica
#  3 = successo eliminazione


def comune(request, success=0):
    try:
        post_data: dict[str, str] = request.POST
        # Caso POST
        # Esso succede quando viene effettuata una ricerca o un inserimento.
        if request.method == "POST":
            if (
                (request.POST.get("codiceModalInsert") is None)
                and (request.POST.get("provinciaModalInsert") is None)
                and (request.POST.get("nomeModalInsert") is None)
            ):
                form = ComuneForm(post_data)
            else:
                form = ComuneForm(app.customlib.insertToForm(request.POST))

            listaelementi = app.customlib.getDataListSearch("comune", post_data)
        # Caso GET o senza richiesta
        # Succede soltanto quando si usano i link all'interno della
        # pagina dei caselli per andare al comune di appartenenza
        else:
            # Se nella richiesta GET c'è il codice, allora cerca quel comune
            if request.GET.get("codice") is not None:
                get_codice = request.GET.get("codice")
                form = ComuneForm({"codice": get_codice})
                listaelementi = app.customlib.getDataListSearch(
                    "comune", {"codice": get_codice}
                )
            # Se nella richiesta GET NON c'è il codice, allora restituisci tutti i comuni
            else:
                listaelementi = app.customlib.getDataList("comune")
                form = ComuneForm()
        # Prepara tutti i campi delle form dei modali
        formModalEdit = ComuneModalEditForm()
        formModalDelete = ComuneModalDeleteForm()
        formModalInsert = ComuneModalInsertForm()
        # Prepara il context da dare al template
        context = {
            "listaelementi": listaelementi,
            "form": form,
            "formModal": formModalEdit,
            "formDeleteModal": formModalDelete,
            "formInsertModal": formModalInsert,
            "success": success,
        }
        # Prepara il template stesso
        template = loader.get_template("comune.html")
        # Risposta HTTP
        return HttpResponse(template.render(context, request))
    # In caso errore, Ritorna la pagina di errore che mostra lo stacktrace
    # Questo caso non dovrebbe mai succedere, a meno che non ci sua una
    # configuraizone errata
    except Exception as err:
        context = {"pagina": "Comune", "stacktrace": traceback.format_exc()}
        template = loader.get_template("userError.html")
        return HttpResponse(template.render(context))


#################################################
# View Casello
# Qui si carica il template della pagina dei caselli
#################################################
def casello(request):
    try:
        post_data: dict[str, str] = request.POST

        # Caso POST
        # Esso succede quando viene effettuata una ricerca.
        if request.method == "POST":
            form = CaselloForm(post_data)
            listaelementi = app.customlib.getDataListSearch("casello", post_data)
        # Caso GET o senza richiesta
        # Succede soltanto quando si usano i link all'interno della
        # pagina dei comuni e delle autostrade per vedere i loro caselli
        else:
            # Caso Comune->Casello
            if request.GET.get("comune") is not None:
                get_comune = request.GET.get("comune")
                form = CaselloForm({"comune": get_comune})
                listaelementi = app.customlib.getDataListSearch(
                    "casello", {"comune": get_comune}
                )
            # Caso Autostrada->Casello
            elif request.GET.get("autostrada") is not None:
                get_autostrada = request.GET.get("autostrada")
                form = CaselloForm({"cod_naz": get_autostrada})
                listaelementi = app.customlib.getDataListSearch(
                    "casello", {"cod_naz": get_autostrada}
                )
            # Caso nessuna richiesta
            else:
                form = CaselloForm()
                listaelementi = app.customlib.getDataList("casello")

        # Qui viene effettuata la conversione di formato delle date
        for i in range(len(listaelementi)):
            elemento = list(listaelementi[i])
            if elemento[9] != "NULL":
                elemento_split: list[str] = elemento[9].split("-")
                elemento[9] = (
                    elemento_split[2]
                    + "/"
                    + elemento_split[1]
                    + "/"
                    + elemento_split[0]
                )
                listaelementi[i] = elemento  # type: ignore

        # Prepara il context da dare al template
        context = {"listaelementi": listaelementi, "form": form}
        # Prepara il template stesso
        template = loader.get_template("casello.html")
        # Risposta HTTP
        return HttpResponse(template.render(context, request))
    # In caso errore, Ritorna la pagina di errore che mostra lo stacktrace
    # Questo caso non dovrebbe mai succedere, a meno che non ci sua una
    # configuraizone errata
    except Exception as err:
        context = {"pagina": "Casello", "stacktrace": traceback.format_exc()}
        template = loader.get_template("userError.html")
        return HttpResponse(template.render(context))


#################################################
# View Autostrada
#################################################
def autostrada(request):
    try:
        post_data: dict[str, str] = request.POST
        # Caso POST
        # Esso succede quando viene effettuata una ricerca.
        if request.method == "POST":
            form = AutostradaForm(post_data)
            listaelementi = app.customlib.getDataListSearch("autostrada", post_data)
        # Caso GET o senza richiesta
        # Succede soltanto quando si usano i link all'interno della
        # pagina dei caselli per andare all'autostrada di appartenenza
        else:
            # Se nella richiesta GET c'è il cod_naz, allora cerca quell'autostrada
            if request.GET.get("cod_naz") is not None:
                get_cod_naz = request.GET.get("cod_naz")
                form = AutostradaForm({"cod_naz": get_cod_naz})
                listaelementi = app.customlib.getDataListSearch(
                    "autostrada", {"cod_naz": get_cod_naz}
                )
            # Se nella richiesta GET NON c'è il codice, allora restituisci tutte le autostrade
            else:
                listaelementi = app.customlib.getDataList("autostrada")
                form = AutostradaForm()

        # Prepara il context da dare al template
        context = {"listaelementi": listaelementi, "form": form}
        # Prepara il template stesso
        template = loader.get_template("autostrada.html")
        # Risposta HTTP
        return HttpResponse(template.render(context, request))
    # In caso errore, Ritorna la pagina di errore che mostra lo stacktrace
    # Questo caso non dovrebbe mai succedere, a meno che non ci sua una
    # configuraizone errata
    except Exception as err:
        context = {"pagina": "Autostrada", "stacktrace": traceback.format_exc()}
        template = loader.get_template("userError.html")
        return HttpResponse(template.render(context))


#################################################
# View Crediti e Licenza
# Questo è usato per le pagine dei crediti e delle licenze
#################################################
def crediti(request):
    template = loader.get_template("crediti.html")
    return HttpResponse(template.render())


def licenza(request):
    template = loader.get_template("licenza.html")
    return HttpResponse(template.render())


#################################################
# View api_aggiungi
# Essa viene eseguita quando viene aggiunto
# un nuovo comune
#################################################
def api_aggiungi(request):
    try:
        # Esegue la query di aggiunta
        app.customlib.addDataTable("comune", request)
        # Ritorna la pagina di comune in caso di successo
        return comune(request, 1)
    except Exception as err:
        # Ritorna la pagina di comune in caso di errore
        return comune(request, -1)


#################################################
# View api_modifica
# Essa viene eseguita quando viene modificato
# il comune selezionato
#################################################
def api_modifica(request):
    try:
        # Esegue la query di modifica
        app.customlib.updateDataTable("comune", request)
        # Ritorna la pagina di comune in caso di successo
        return comune(request, 2)
    except Exception as err:
        # Ritorna la pagina di comune in caso di errore
        return comune(request, -2)


#################################################
# View api_elimina
# Essa viene eseguita quando viene eleminato
# il comune selezionato
#################################################
def api_elimina(request):
    try:
        # Esegue la query di eliminazione
        app.customlib.removeDataTable("comune", request)
        # Ritorna la pagina di comune in caso di successo
        return comune(request, 3)
    except Exception as err:
        # Ritorna la pagina di comune in caso di errore
        return comune(request, -3)


#################################################
# View Test [DEBUG]
# View di testing, non viene realmente usata
# da niente nel sito
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

    context = {"comuni": listaelementi, "form": form}
    template = loader.get_template("test.html")
    return HttpResponse(template.render(context, request))


#################################################
# View userError [DEBUG]
# View di testing, non viene realmente usata
# da niente nel sito
#################################################
def usererror(request):
    context = {"pagina": "usererror"}
    template = loader.get_template("userError.html")
    return HttpResponse(template.render(context))
