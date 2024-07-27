from django import forms
import app.customlib as customlib

class ComuneForm(forms.Form):
	forms.Select
	codice = forms.CharField(label="Codice comune", max_length=100, required=False)
	codice.widget.attrs.update({"class": "form-control"})

	provincia = forms.CharField(label="Provincia", widget=forms.Select(choices=customlib.getProvincieUnique()), required=False)
	provincia.widget.attrs.update({"class": "form-control"})

	nome = forms.CharField(label="Nome comune", max_length=100, required=False)
	nome.widget.attrs.update({"class": "form-control"})

class ComuneModalForm(forms.Form):
	forms.Select
	codiceModal = forms.CharField(label="Codice comune", max_length=100, required=False)
	codiceModal.widget.attrs.update({"class": "form-control"})

	provinciaModal = forms.CharField(label="Provincia", widget=forms.Select(choices=customlib.getProvincieUnique()), required=False)
	provinciaModal.widget.attrs.update({"class": "form-control"})

	nomeModal = forms.CharField(label="Nome comune", max_length=100, required=False)
	nomeModal.widget.attrs.update({"class": "form-control"})

class AutostradaForm(forms.Form):
	cod_naz = forms.CharField(label="cod_naz", max_length=100, required=False)
	cod_naz.widget.attrs.update({"class": "form-control"})

	cod_eu = forms.CharField(label="provincia", max_length=100, required=False)
	cod_eu.widget.attrs.update({"class": "form-control"})

	nome = forms.CharField(label="nome", max_length=100, required=False)
	nome.widget.attrs.update({"class": "form-control"})

	lunghezza = forms.CharField(label="nome", max_length=100, required=False)
	lunghezza.widget.attrs.update({"class": "form-control"})

class AutostradaModalForm(forms.Form):
	cod_nazModal = forms.CharField(label="cod_naz", max_length=100, required=False)
	cod_nazModal.widget.attrs.update({"class": "form-control"})

	cod_euModal = forms.CharField(label="provincia", max_length=100, required=False)
	cod_euModal.widget.attrs.update({"class": "form-control"})

	nomeModal = forms.CharField(label="nome", max_length=100, required=False)
	nomeModal.widget.attrs.update({"class": "form-control"})

	lunghezzaModal = forms.CharField(label="nome", max_length=100, required=False)
	lunghezzaModal.widget.attrs.update({"class": "form-control"})

class CaselloForm(forms.Form):
	codice = forms.CharField(label="codice", max_length=100, required=False)
	codice.widget.attrs.update({"class": "form-control"})

	cod_naz = forms.CharField(label="cod_naz", max_length=100, widget=forms.Select(choices=customlib.getAutostradeUnique()), required=False)
	cod_naz.widget.attrs.update({"class": "form-control"})

	comune = forms.CharField(label="provincia", max_length=100, widget=forms.Select(choices=customlib.getComuniUnique()), required=False)
	comune.widget.attrs.update({"class": "form-control"})

	nome = forms.CharField(label="nome", max_length=100, required=False)
	nome.widget.attrs.update({"class": "form-control"})

	x = forms.CharField(label="x", max_length=100, required=False)
	x.widget.attrs.update({"class": "form-control"})

	y = forms.CharField(label="y", max_length=100, required=False)
	y.widget.attrs.update({"class": "form-control"})

	is_automatico = forms.CharField(label="is_automatico", max_length=100, required=False)
	is_automatico.widget.attrs.update({"class": "form-control", "onclick": "blockDate()"})

	data_automazione = forms.CharField(label="data_automazione", max_length=100, required=False)
	data_automazione.widget.attrs.update({"class": "form-control"})

class CaselloModalForm(forms.Form):
	codiceModal = forms.CharField(label="codice", max_length=100, required=False)
	codiceModal.widget.attrs.update({"class": "form-control"})

	cod_nazModal = forms.CharField(label="cod_naz", max_length=100, widget=forms.Select(choices=customlib.getAutostradeUnique()), required=False)
	cod_nazModal.widget.attrs.update({"class": "form-control"})

	comuneModal = forms.CharField(label="provincia", max_length=100, widget=forms.Select(choices=customlib.getComuniUnique()), required=False)
	comuneModal.widget.attrs.update({"class": "form-control"})

	nomeModal = forms.CharField(label="nome", max_length=100, required=False)
	nomeModal.widget.attrs.update({"class": "form-control"})

	xModal = forms.CharField(label="x", max_length=100, required=False)
	xModal.widget.attrs.update({"class": "form-control"})

	yModal = forms.CharField(label="y", max_length=100, required=False)
	yModal.widget.attrs.update({"class": "form-control"})

	is_automaticoModal = forms.CharField(label="is_automatico", max_length=100, required=False)
	is_automaticoModal.widget.attrs.update({"class": "form-control", "onclick": "blockDate()"})

	data_automazioneModal = forms.CharField(label="data_automazione", max_length=100, required=False)
	data_automazioneModal.widget.attrs.update({"class": "form-control"})
