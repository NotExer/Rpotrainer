from django.db import models

class entrenamiento(models.Model):
    Tipo = models.CharField(max_length=50)
    Tarifa = models.IntegerField()
    Modalidad = models.CharField(max_length=50)
    Duracion = models.IntegerField()
    Lista_Ejercicios = models.CharField(max_length=500)
