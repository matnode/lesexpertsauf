from django import forms

class ExpertphotoForm(forms.Form):
	photo = forms.ImageField()
