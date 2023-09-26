from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):    
    return render(request, "index.html")

def menu(request, nro_menu):    
    # html = "<html><body>MENU</body></html>" + nro_menu
    # return HttpResponse(html)

    lista_menu1 = ('Brochetas de Pollo y carne con pure.', '$2000')
    lista_menu2 = ('Cachapa con queso y cochino frito.', '$1500')

    context = {'menu1': 'Brochetas',
               'detalle1': lista_menu1,            
               'menu2': 'Cachapa',       
               'detalle2': lista_menu2,               
               'menu3': 'Empanadas',
               'menu4': 'Pastel de Platano',
               'menu5': 'Pasticho de carne',
               'menu6': 'Patacon Maduro',
               'menu7': 'Patacon Verde',
               'menu8': 'Sopa de Res',
               }

    return render(request, "menu.html", context)

def contacto(request):    
    return render(request, "contacto.html")
    

def sucursales(request):
    return render(request, "sucursales.html")

