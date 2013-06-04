from django.shortcuts import render_to_response

def bemVindo(request):
    return render_to_response("bemvindo.html",{})
