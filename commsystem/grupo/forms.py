from django import forms
from models import Grupo

class RegistrarGrupo(forms.ModelForm):
	class Meta:
		model = Grupo