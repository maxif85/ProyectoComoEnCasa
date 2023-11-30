from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import *
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProductosForm

def index(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("Usuario autenticado correctamente")
                return redirect('index')
        else:
            print("Formulario no válido")
    else:
        form = AuthenticationForm()

    return render(request, 'iniciar_sesion.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def contacto(request):
    return render(request, 'contacto.html')

def menu(request):
    productos = Productos.objects.all()

    context = {
        'productos': productos,
    }

    return render(request, 'menu.html', context)

def ver_productos(request):
    mensaje = None
    productos = Productos.objects.all()
    
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        if producto_id:
            producto = Productos.objects.get(id=producto_id)
            carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
            item, _ = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
            item.cantidad += 1
            item.save()
            mensaje = f"{producto.nombreProducto} se ha agregado al carrito."
    
    return render(request, 'ver_productos.html', {'productos': productos, 'mensaje': mensaje})



def ver_carrito(request):
    if request.user.is_authenticated:
        usuario = request.user
        carrito = Carrito.objects.filter(usuario=usuario).first()
        if carrito:
            items = carrito.itemcarrito_set.all()
        else:
            items = []

        return render(request, 'ver_carrito.html', {'items': items})
    else:
        return redirect('iniciar_sesion')
    
def eliminar_del_carrito(request, producto_id):
    if request.user.is_authenticated:
        try:
            item = ItemCarrito.objects.get(id=producto_id)
            item.delete()
        except ItemCarrito.DoesNotExist:
            pass
    return redirect('ver_carrito')


class PlatosListView(ListView):
    template_name = "nuestros_platos.html"
    context_object_name = "productos"
    model = Productos

class PlatosCreateView(CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = "crear_producto.html"
    context_object_name = "productos"