from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .forms import ContactoForm


# Create your views here.
def index(request):    
    return render(request, "index.html")

def menu(request, nro_menu):    
    # html = "<html><body>MENU</body></html>" + nro_menu
    # return HttpResponse(html)

    lista_plato1 = ('Brochetas de Pollo y carne con pure.', '$2000')
    lista_plato2 = ('Cachapa con queso y cochino frito.', '$1500')

    context = {'plato1': 'Brochetas',
               'detalle1': lista_plato1,            
               'plato2': 'Cachapa',       
               'detalle2': lista_plato2,               
               'plato3': 'Empanadas',
               'plato4': 'Pastel de Platano',
               'plato5': 'Pasticho de carne',
               'plato6': 'Patacon Maduro',
               'plato7': 'Patacon Verde',
               'plato8': 'Sopa de Res',
               }

    return render(request, "menu.html", context)

from django.shortcuts import render, redirect
from .models import clientes

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            cliente = clientes(
                nombre=formulario.cleaned_data['nombre'],
                apellido=formulario.cleaned_data['apellido'],
                direccion=formulario.cleaned_data['direccion'],
                ciudad = formulario.cleaned_data['ciudad'],
                zipcode = formulario.cleaned_data['codigo_postal'],
                nacimiento = formulario.cleaned_data['nacimiento'],
                email = formulario.cleaned_data['email']
            )
            cliente.save()
            return redirect('index-view')
    else:
        formulario = ContactoForm()

    context = {
        'contacto_form': formulario
    }
    return render(request, "contacto.html", context)


def sucursales(request):
    return render(request, "sucursales.html")

