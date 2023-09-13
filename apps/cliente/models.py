from django.db import models
from apps.diagnostico.views import diagnostico
from apps.medidas.views import medidas

class cliente(models.Model):
    
    NombreCompleto = models.CharField(max_length=100)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    FechaPago = models.DateField()
    Edad = models.IntegerField()
    Telefono = models.CharField(max_length=20)
    Email = models.EmailField()
    Domicilio = models.CharField(max_length=200)
    Medidas = models.ForeignKey(medidas, null=True, blank=True, on_delete=models.CASCADE)
    Diagnostico = models.ForeignKey(diagnostico, null=True, blank=True, on_delete=models.CASCADE)

    