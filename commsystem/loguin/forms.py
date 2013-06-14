from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User , Group , Permission

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


class alterar_usuario(forms.Form):
	
	Usuario = forms.ModelMultipleChoiceField(queryset= User.objects.all() )
	Grupo = forms.ModelMultipleChoiceField(queryset = Group.objects.all())
	
class tentativa2(forms.Form):
	Permissao = forms.ModelMultipleChoiceField(queryset = Permission.objects.exclude(content_type = 8))
	Grupo = forms.ModelMultipleChoiceField(queryset = Group.objects.all())