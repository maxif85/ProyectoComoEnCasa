from django.db import models

# Create your models here.

class clientes(models.Model):
    nombre = models.CharField(max_length=80, null=False)
    apellido = models.CharField(max_length=80, null=False)
    direccion = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()
    nacimiento = models.DateField()
    email = models.EmailField()

class Productos(models.Model):
    nombre_plato = models.CharField(max_length=50, null=False)
    desc_plato = models.CharField(max_length=80, null=False)
    precio_plato = models.FloatField()

    def __str__(self):
        return self.nombre_plato
    
class Pedido(models.Model):
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)  # Si tienes un modelo de cliente
    productos = models.ManyToManyField(Productos, through='ElementoPedido')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

class ElementoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

