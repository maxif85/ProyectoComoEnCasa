from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):    
    return render(request, "index.html")

def menu(request, nro_menu):    
    html = "<html><body>MENU</body></html>" + nro_menu
    return HttpResponse(html)

def contacto(request):    
    return render(request, "contacto.html")
    

def sucursales(request):
    return render(request, "sucursales.html")

