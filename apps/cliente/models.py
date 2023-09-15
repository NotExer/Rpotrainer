from django.db import models
from apps.diagnostico.views import diagnostico
from apps.medidas.views import medidas

class cliente(models.Model):
    
    NombreCompleto = models.CharField(max_length=100)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    FechaPago = models.DateField()


    