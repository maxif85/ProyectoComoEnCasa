from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .forms import ContactoForm
from .models import *


# Create your views here.
def index(request):    
    return render(request, "index.html")

def menu(request):
    productos = Productos.objects.all()
    return render(request, 'menu.html', {'productos': productos})

from django.shortcuts import render, redirect
from  .models import clientes

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            cliente = clientes(
                nombre=formulario.cleaned_data['nombre'],
                apellido=formulario.cleaned_data['apellido'],
                direccion=formulario.cleaned_data['direccion'],
                ciudad = formulario.cleaned_data['ciudad'],
                codigo_postal = formulario.cleaned_data['codigo_postal'],
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

