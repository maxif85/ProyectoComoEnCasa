from django.db import models
from django.contrib.auth.models import User 

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Productos(models.Model):
    nombreProducto = models.CharField(max_length=200)
    precioUnitario = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    # imagenProducto = models.ImageField(null=True, upload_to="static\img\Menu")

    def __str__(self):
        return self.nombreProducto
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField('Productos', through='ItemCarrito')

    def __str__(self):
        return f'Carrito de {self.usuario.username}'
    
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombreProducto}'