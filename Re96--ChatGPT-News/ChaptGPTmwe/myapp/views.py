# all below added by Re per error at runserver.  Matthes p. 396

from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')
