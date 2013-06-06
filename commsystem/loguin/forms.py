from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email",help_text="")
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    username = forms.CharField(label="Login")
    
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
