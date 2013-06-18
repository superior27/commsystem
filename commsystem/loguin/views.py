from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import RegisterForm , tentativa1 , alterar_usuario, tentativa2 ,FormAtividade, FormName
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User , Group ,Permission
from models import Atividade


#@permission_required('loguin.ver_todos_usuarios')
@login_required
def bemVindo(request):
    return render_to_response("bemvindo.html",{},
          context_instance=RequestContext(request))
    
def leiaMais(request):
    
     return render_to_response("leiaMais.html",{},
          context_instance=RequestContext(request))

@login_required
def registrar(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
              
        if form.is_valid():

          usuario = form.save(commit=False)

          usuario.save()

          return HttpResponseRedirect("/bemVindo/")
        else:
          return render_to_response("registrar.html",{'form':form}, 
              context_instance=RequestContext(request))
    return render_to_response("registrar.html",{'form':RegisterForm()}, 
              context_instance=RequestContext(request))

@login_required
def tentativa(request):

    if request.method == "POST":   
        form = tentativa1(request.POST)


        if form.is_valid():
          form.save()
            
          return HttpResponseRedirect("/tentativa/")
        else:
            return render_to_response("grupo.html",{'form':form,},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':tentativa1()},
             context_instance=RequestContext(request))

@login_required
def cadastrarUsuarioGrupo(request):

    if request.method == "POST":   
        form = alterar_usuario(request.POST)
        
        if form.is_valid():
            Usuario = form.cleaned_data['Usuario']
            Grupo = form.cleaned_data['Grupo']

            usuarioOb = User.objects.get(id = Usuario)
            groupOb = Group.objects.get(id = Grupo)
            
            usuarioOb.groups.add(groupOb)

            return HttpResponseRedirect("/cadastrarUsuarioGrupo/")
        else:
            return render_to_response("cadastrarUsuario.html",{'form':form},
             context_instance=RequestContext(request))
    return render_to_response("cadastrarUsuario.html",{'form':alterar_usuario()},
             context_instance=RequestContext(request))



"""Apaguei a anterior estava muito ruim"""
@login_required
def atividade(request):
    if request.method == "POST":
        form = FormAtividade(request.POST, request.FILES)
        if form.is_valid():          
          form.save()
          return render_to_response("salvo.html")
    else:
        form = FormAtividade()
        
    form = FormAtividade()
    return render_to_response("atividade.html",{'form': form},
      context_instance=RequestContext(request))


@login_required
def lista_atividade(request):
    nome =''
    if request.method == "POST":   
        form = FormName(request.POST, request.FILES) 
        
        if form.is_valid():
            nome = form.cleaned_data['name']                     
    form = FormName()   
    return render_to_response("lista_atividade.html",{ 'lista_itens':Atividade.objects.filter(grupo=request.user.groups.filter(name=nome)),'form':form,'groups':request.user.groups.all()},
              context_instance=RequestContext(request))