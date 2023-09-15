from django.db import models
from apps.cliente.models import cliente
from apps.medidas.models import medidas
from apps.diagnostico.models import diagnostico

class planes(models.Model):
    
    nombre = models.CharField(max_length=250)
    tarifa = models.FloatField()
    descuento = models.FloatField()
    fechainicio = models.DateField()
    fechafin = models.DateField()
    modalidad = models.CharField(max_length=250)
    Cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    Medidas = models.ForeignKey(medidas, on_delete=models.CASCADE)
    Diagnostico = models.ForeignKey(diagnostico, on_delete=models.CASCADE)


    