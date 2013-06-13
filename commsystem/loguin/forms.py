from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User , Group


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


class tentativa1(forms.ModelForm):

	class Meta:
		model = Group


class alterar_usuario(UserChangeForm):
	
	#usuario_opcao = User.object.all()
	#grupos_opcao = Group.object.get(name)
	#usuario = forms.ChoiceField(required=True, label='usuario', choices=usuario_opcao)
	#grupo = forms.ChoiceField(required=True, label='grupo', choices=grupos_opcao)
	class Meta:
		model = User