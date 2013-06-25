# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User , Group , Permission
from models import Atividade

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email",help_text="")
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    username = forms.CharField(label="username")

    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        fields = ('username','first_name','last_name','email')


class tentativa1(forms.ModelForm):

	class Meta:
	   model = Group
        fields = ('name')
        

class alterar_usuario(forms.Form):
	
	Usuario = forms.ModelMultipleChoiceField(queryset= User.objects.all() )
	Grupo = forms.ModelMultipleChoiceField(queryset = Group.objects.all())
	
class tentativa2(forms.Form):
	#Permissao = forms.ModelMultipleChoiceField(queryset = Permission.objects.filter(content_type = 8))
    Permissao1 = Permission.objects.filter(content_type = 8)
    Permissao2 = Permissao1.exclude(id = 25)
    Permissao3 = forms.ModelMultipleChoiceField(Permissao2,label = "Permissões")
    Grupo = forms.ModelMultipleChoiceField(queryset = Group.objects.all(),label = "Grupos")

"""Apaguei o form anterior de atividades, estava ruim"""

class FormAtividade(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ('titulo','dataInicial','horaInicial','dataFinal','horaFinal','descricao','grupo')

class FormName (forms.Form):
    name = forms.CharField(label="Digite o nome de um grupo para visualizar as atividades")
    class Meta:
        fields = ('name')

class FormChoiceUser (forms.Form):
    name = forms.ModelChoiceField(queryset=User.objects.all(),label="Escolha o usuário e verifique a quantidade de atividades feitas")
    class Meta:
        fields = ('name')