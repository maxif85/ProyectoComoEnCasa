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

class pedido(models.Model):
    prueba = models.CharField(max_length=50)