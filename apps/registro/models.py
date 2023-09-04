from django.db import models
from apps.registro.forms import CustomUserForm
from django.contrib.auth.models import AbstractUser

class CustomUserForm(models.Model):
    NombreCompleto = models.CharField(max_length=100)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    FechaPago = models.DateField()
    Edad = models.IntegerField()
    Telefono = models.CharField(max_length=20)
    Email = models.EmailField()
    Domicilio = models.CharField(max_length=200)

