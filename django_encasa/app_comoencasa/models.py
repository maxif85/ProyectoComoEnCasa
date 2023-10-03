from django.db import models

# Create your models here.

class clientes(models.Model):
    """id = models.#Auto increment ??"""
    nombre = models.CharField(max_length=80, null=False)
    apellido = models.CharField(max_length=80, null=False)

class pedido(models.Model):
    prueba = models.CharField(max_length=50)