from django.db import models

class planes(models.Model):
    
    nombre = models.CharField(max_length=250)
    tarifa = models.FloatField()
    fechainicio = models.DateField()
    fechafin = models.DateField()
    modalidad = models.CharField(max_length=250)


    