from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import RegisterForm
from django.contrib.auth.decorators import login_required


@login_required
def bemVindo(request):
    return render_to_response("bemvindo.html",{},
          context_instance=RequestContext(request))

def registrar(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/bemVindo/")
        else:
            return render_to_response("registrar.html",{'form':form}, context_instance=RequestContext(request))
    return render_to_response("registrar.html",{'form':RegisterForm()}, context_instance=RequestContext(request))

def grupo(request):
    if request.method == "POST":    
        form = RegistrarGrupo(request.POST)
    
    return render_to_response("grupo.html",{'form':RegistrarGrupo()}, context_instance=RequestContext(request))


    
