from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import RegisterForm , tentativa1 , alterar_usuario, tentativa2 ,insereAtividade
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User , Group ,Permission


#@permission_required('loguin.ver_todos_usuarios')
@login_required
def bemVindo(request):
    return render_to_response("bemvindo.html",{},
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
            return render_to_response("grupo.html",{'form':form},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':alterar_usuario()},
             context_instance=RequestContext(request))

@login_required
def atividades(request):
    #usuario = request.user
    #grupoUsuario = usuario.groups.all()
    if request.method == "POST":   
      
        form = insereAtividade(request.POST)
        #form.fk_group = form.ModelMultipleChoiceField(usuario.group.get())
        if form.is_valid():
            dados = form.cleaned_data
            item = Atividade(   
                        nome = dados['nome'],
                        descricao = dados['descricao'],
                        dataInicial = dados['dataInicial'],
                        dataFinal = dados['dataFinal'],
                        conclusao = dados['conclusao'],
                        fk_group = Group.objects.get(id=dados['fk_group']))
            item.save()
            return HttpResponseRedirect("/bemVindo/")
        else:
            return render_to_response("templateAtividade.html",{'form':form}, 
                context_instance=RequestContext(request))
    return render_to_response("templateAtividade.html",{'form':insereAtividade()}, 
              context_instance=RequestContext(request))
    


"""  
                            )"""