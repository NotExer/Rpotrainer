from django.db import models

class cliente(models.Model):
    
    NombreCompleto = models.CharField(max_length=100)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    FechaPago = models.DateField()
    Edad = models.IntegerField()
    Telefono = models.CharField(max_length=20)
    Email = models.EmailField()
    Domicilio = models.CharField(max_length=200)

    