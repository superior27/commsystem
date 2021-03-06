from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import RegisterForm , tentativa1 , alterar_usuario, tentativa2 ,FormAtividade, FormName, FormChoiceUser
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User , Group ,Permission
from models import Atividade
from django.contrib.comments.models import Comment
from django import forms

#@permission_required('loguin.ver_todos_usuarios')
@login_required
def bem_vindo(request):
    return render_to_response("bemvindo.html",{},
          context_instance=RequestContext(request))
    
def leia_mais(request):
    
     return render_to_response("leiaMais.html",{},
          context_instance=RequestContext(request))

@login_required
def registrar(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
              
        if form.is_valid():

          usuario = form.save(commit=False)

          usuario.save()

          return render_to_response("salvo.html")
        else:
          return render_to_response("registrar.html",{'form':form}, 
              context_instance=RequestContext(request))
    return render_to_response("registrar.html",{'form':RegisterForm()}, 
              context_instance=RequestContext(request))

@login_required
def criar_grupo(request):

    if request.method == "POST":   
        form = tentativa1(request.POST)


        if form.is_valid():
          form.save()
            
          return render_to_response("salvo.html")
        else:
            return render_to_response("grupo.html",{'form':form,},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':tentativa1()},
             context_instance=RequestContext(request))

@login_required
def cadastrar_permissao_grupo(request):
  if request.method == "POST":   
        form = tentativa2(request.POST)
        if form.is_valid():
          Permissao = form.cleaned_data['Permissao3']
          Grupo = form.cleaned_data['Grupo']
          for permissionOb in Permissao:
            for groupOb in Grupo:
              permission = Permission.objects.get(id = permissionOb.id)
              group = Group.objects.get(id = groupOb.id)
              group.permissions.add(permission)
            
          return render_to_response("salvo.html")
        else:
            return render_to_response("cadastrar_permissao_grupo.html",{'form':form,},
             context_instance=RequestContext(request))
  return render_to_response("cadastrar_permissao_grupo.html",{'form':tentativa2()},
           context_instance=RequestContext(request))

@login_required
def cadastrar_usuario_grupo(request):

    if request.method == "POST":   
        form = alterar_usuario(request.POST)
        
        if form.is_valid():
            Usuario = form.cleaned_data['Usuario']
            Grupo = form.cleaned_data['Grupo']
            """
            usuarioOb = User.objects.get(id = Usuario)
            groupOb = Group.objects.get(id = Grupo)
            
            usuarioOb.groups.add(groupOb)
            """

            for userOb in Usuario:
              for groupOb in Grupo:                
                user = User.objects.get(id = userOb.id)
                group = Group.objects.get(id = groupOb.id)
                #user = usuarioOb.user
                #group = grupoOb.groups
                user.groups.add(group)
              

            return render_to_response("salvo.html")
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
    nomeComment = ''
    if request.method == "POST":   
        form = FormName(request.POST, request.FILES)        
        if form.is_valid():
            nome = form.cleaned_data['name']
        

    form = FormName()       
    return render_to_response("lista_atividade.html",{ 'lista_itens':Atividade.objects.filter(grupo=request.user.groups.filter(name__exact=nome)),'form':form,'groups':request.user.groups.all()},
              context_instance=RequestContext(request))


@login_required
def quant_atividade(request):
    nomeComment = 0
    if request.method == "POST":   
        form2 = FormChoiceUser(request.POST, request.FILES)
        if form2.is_valid():
            Usuario = form2.cleaned_data['name']
            userOb= User.objects.get(id=Usuario.id)
            nomeComment = userOb

    form2 = FormChoiceUser()   
    return render_to_response("quant_atividade.html",{ 'quantComment':Comment.objects.filter(user=nomeComment).count(),'form2':form2},
              context_instance=RequestContext(request))