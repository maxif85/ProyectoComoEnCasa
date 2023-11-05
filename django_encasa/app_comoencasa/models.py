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
    pedidos = models.ManyToManyField('pedido', related_name='clientes')

class Pedido(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return f'Pedido #{self.id}'

class A_domicilio(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre" )

class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre" )

class Envios(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre" )
    apellido = models.CharField(max_length=150, verbose_name="Apellido" )
    direccion = models.CharField(max_length=150, verbose_name="Direccion" )
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()
    email = models.EmailField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    a_domicilio = models.ManyToManyField(A_domicilio)
    nombre = models.CharField(max_length=150, verbose_name="Nombre" )