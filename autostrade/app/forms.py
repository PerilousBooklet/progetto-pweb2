from django import forms

class ComuneForm(forms.Form):
	codice = forms.CharField(label="codice", max_length=100,)