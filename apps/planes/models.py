from django.db import models
from apps.cliente.models import cliente
from apps.medidas.models import medidas
from apps.diagnostico.models import diagnostico

class planes(models.Model):
    nombre = models.CharField(max_length=250)
    tarifa = models.IntegerField()
    descuento = models.IntegerField()
    total = models.IntegerField()
    fechainicio = models.DateField()
    fechafin = models.DateField()
    modalidad = models.CharField(max_length=250)