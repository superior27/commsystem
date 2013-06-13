from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User , Group
from models import Grupo
from models import Permissao_Grupo
from models import Grupo_Usuario

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email",help_text="")
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    username = forms.CharField(min_length = 2, max_length=15, required=True,error_messages={'requied': 'Hi'}) 

    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        fields = ('username','first_name','last_name','email')


class RegistrarGrupo(forms.ModelForm):
	

	class Meta:
		model = Grupo

class GrupoPermissao(forms.ModelForm):
	
	class Meta:
		model = Permissao_Grupo

class InserirUsuario(forms.ModelForm):
	
	class Meta:
		model = Grupo_Usuario	

class tentativa1(forms.ModelForm):

	class Meta:
		model = Group

