from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.http import HttpResponseRedirect
from forms import RegisterForm , tentativa1 , alterar_usuario
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User , Group


@permission_required('loguin.ver_todos_usuarios')
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
          group = Group.objects.get(name='God')

          usuario.save()

          usuario.groups.add(group)

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
            return render_to_response("grupo.html",{'form':form},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':tentativa1()},
             context_instance=RequestContext(request))


def mudaropcao(request):

    if request.method == "POST":   
        form = alterar_usuario(request.POST)
        
        if form.is_valid():
            form.save()
            #usuario = form.save(commit=False)
            #group = Group.objects.get(name='God')

            #usuario.save()

            #usuario.groups.add(group)

            return HttpResponseRedirect("/mudaropcao/")
        else:
            return render_to_response("grupo.html",{'form':form},
             context_instance=RequestContext(request))
    return render_to_response("grupo.html",{'form':alterar_usuario()},
             context_instance=RequestContext(request))
