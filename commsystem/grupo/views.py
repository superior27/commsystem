from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import RegistrarGrupo



def grupo(request):
    if request.method == "POST":    
        form = RegistrarGrupo(request.POST)
    
    return render_to_response("grupo.html",{'form':RegistrarGrupo()}, context_instance=RequestContext(request))


    
