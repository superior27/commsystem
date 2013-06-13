from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import RegisterForm
from django.contrib.auth.decorators import login_required,permission_required
from forms import RegistrarGrupo
from forms import GrupoPermissao
from forms import InserirUsuario
from models import Grupo_Usuario
from models import Permissao_Grupo
from forms import  tentativa1
from django.contrib.auth.models import User , Group


@permission_required('loguin.ver_todos_usuarios')
@login_required
def bemVindo(request):
    return render_to_response("bemvindo.html",{},
          context_instance=RequestContext(request))

@login_required
def registrar(request):

    #item = Grupo_Usuario.objects.filter(id_usuario = request.user)
    #print(item)
    #grupo = 
    #permissao = Permissao_Grupo.objects.filter(grupo = item)
     
    #if permissao !=0:
    #if it
    if request.method == "POST":
        form = RegisterForm(request.POST)
              
        if form.is_valid():
          """
          Não foi fácil para que conseguisse fazer isso.
          Não será fácil para que você consiga entender!
          :)
          

          """

            usuario = form.save(commit=False)
            """ 
              Aqui em vez de salvar logo o meu form direto no meu BD
              eu faço com que esse meu form preenchido seja gravado
              em uma variável que chamei de usuario
            """
            group = Group.objects.get(name='God')
            """
              Aqui eu crio um variável que receberá um onjeto do tipo
              Group que tem como nome God, o único grupo cadastrado no caso
              No caso quando formos ajeitar isso, provavelmente colocaremos
              um retorno de todos os grupos e todos os usuários, o cara que
              for cadastrar o usuário dentro do grupo terá que escolher quem
              ficará em qual grupo
            """
            usuario.save()
            """
              Salvo o meu usuario dentro do meu BD

            """
            usuario.groups.add(group)
            """
              Aqui é onde a mágica acontece, eu adiciono um usuário a
              um grupo, já que dentro de usuário a uma foreign key de
              many to many, se não me engano com todos os grupos que
              o mesmo está cadastrado, dessa forma utilizo a função
              add e adiciono o meu grupo
            """

            """
            Enfim isso foi só para testar, depois a gente terá
            fazer um formulário um html e tal...
            Creio que amanhã(14/06/2013) eu e matheus já concluamos isso.

            """
            return HttpResponseRedirect("/bemVindo/")
        else:
            return render_to_response("registrar.html",{'form':form}, 
                context_instance=RequestContext(request))
    return render_to_response("registrar.html",{'form':RegisterForm()}, 
                context_instance=RequestContext(request))

@login_required
def cadasgrupo(request):
    if request.method == "POST":    
        form = RegistrarGrupo(request.POST, request.FILES)
        
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/permissaogrupo/")
        else:
           return render_to_response("grupo.html",{'form':form},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':RegistrarGrupo()},
             context_instance=RequestContext(request))
        
@login_required
def permissaogrupo(request):

    if request.method == "POST":   
        form = GrupoPermissao(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/bemVindo/")
        else:
            return render_to_response("grupo.html",{'form':form},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':GrupoPermissao()},
             context_instance=RequestContext(request))

@login_required
def inserirUser(request):

    if request.method == "POST":   
        form = InserirUsuario(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/bemVindo/")
        else:
            return render_to_response("grupo.html",{'form':form},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':InserirUsuario()},
             context_instance=RequestContext(request))

def tentativa(request):

    if request.method == "POST":   
        form = tentativa1(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/tentativa/")
        else:
            return render_to_response("grupo.html",{'form':form},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':tentativa1()},
             context_instance=RequestContext(request))


    
