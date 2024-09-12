from django import forms
import app.customlib as customlib

class ComuneForm(forms.Form):
	codice = forms.CharField(label="Codice comune", max_length=100, required=False)
	codice.widget.attrs.update({"class": "form-control"})

	provincia = forms.CharField(label="Provincia", widget=forms.Select(choices=customlib.getProvincieUnique()), required=False)
	provincia.widget.attrs.update({"class": "form-select"})

	nome = forms.CharField(label="Nome comune", max_length=100, required=False)
	nome.widget.attrs.update({"class": "form-control"})

class ComuneModalEditForm(forms.Form):
    codiceModalEdit = forms.CharField(label="", max_length=100, required=False)
    codiceModalEdit.widget.attrs.update({"class": "form-control", "hidden": " "})

    provinciaModalEdit = forms.CharField(label="Provincia", widget=forms.Select(choices=customlib.getProvincieUnique()), required=False)
    provinciaModalEdit.widget.attrs.update({"class": "form-select"})

    nomeModalEdit = forms.CharField(label="Nome comune", max_length=100, required=False)
    nomeModalEdit.widget.attrs.update({"class": "form-control"})

class ComuneModalDeleteForm(forms.Form):
    codiceModalDelete = forms.CharField(label="", max_length=100, required=False)
    codiceModalDelete.widget.attrs.update({"class": "form-control", "hidden": " "})

    provinciaModalDelete = forms.CharField(label="", widget=forms.Select(choices=customlib.getProvincieUnique()), required=False)
    provinciaModalDelete.widget.attrs.update({"class": "form-select", "hidden": " "})

    nomeModalDelete = forms.CharField(label="", max_length=100, required=False)
    nomeModalDelete.widget.attrs.update({"class": "form-control", "hidden": " "})

class ComuneModalInsertForm(forms.Form):
    codiceModalInsert = forms.CharField(label="Codice comune", max_length=100, required=False)
    codiceModalInsert.widget.attrs.update({"class": "form-control"})

    provinciaModalInsert = forms.CharField(label="Provincia", widget=forms.Select(choices=customlib.getProvincieUnique()), required=False)
    provinciaModalInsert.widget.attrs.update({"class": "form-select"})

    nomeModalInsert = forms.CharField(label="Nome comune", max_length=100, required=False)
    nomeModalInsert.widget.attrs.update({"class": "form-control"})

class AutostradaForm(forms.Form):
	cod_naz = forms.CharField(label="Codice nazionale", max_length=100, required=False)
	cod_naz.widget.attrs.update({"class": "form-control"})

	cod_eu = forms.CharField(label="Codice Europeo", max_length=100, required=False)
	cod_eu.widget.attrs.update({"class": "form-control"})

	nome = forms.CharField(label="Nome", max_length=100, required=False)
	nome.widget.attrs.update({"class": "form-control"})

	lunghezza = forms.CharField(label="Lunghezza", max_length=100, required=False)
	lunghezza.widget.attrs.update({"class": "form-control", "type": "number"})

class CaselloForm(forms.Form):
	opzioniAutomatico = [("0", "Presenziato"), ("1", "Automatico"), ("", "Tutti")]

	codice = forms.CharField(label="Codice casello", max_length=100, required=False)
	codice.widget.attrs.update({"class": "form-control"})

	cod_naz = forms.CharField(label="Codice autostrada", max_length=100, widget=forms.Select(choices=customlib.getAutostradeUnique()), required=False)
	cod_naz.widget.attrs.update({"class": "form-select"})

	comune = forms.CharField(label="Codice comune", max_length=100, required=False)
	comune.widget.attrs.update({"class": "form-control"})

	nome = forms.CharField(label="Nome", max_length=100, required=False)
	nome.widget.attrs.update({"class": "form-control"})

	x = forms.CharField(label="Coordinata X", required=False)
	x.widget.attrs.update({"class": "form-control", "type": "number", "step": "0.000001"})

	y = forms.CharField(label="Coordinata Y", required=False)
	y.widget.attrs.update({"class": "form-control", "type": "number", "step": "0.000001"})

	is_automatico = forms.ChoiceField(label="Tipo casello", widget=forms.RadioSelect, choices=opzioniAutomatico, required=False)
	is_automatico.widget.attrs.update({"class": "form-check-input", "onclick": "blockDate()"})

	data_automazione = forms.DateField(label="Data automazione", widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
	data_automazione.widget.attrs.update({"class": "date form-control"})