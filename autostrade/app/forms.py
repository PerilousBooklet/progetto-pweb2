from django import forms

class ComuneForm(forms.Form):
	codice = forms.CharField(label="codice", max_length=100)
	provincia = forms.CharField(label="provincia", max_length=100)
	nome = forms.CharField(label="nome", max_length=100)