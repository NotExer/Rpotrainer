from django.db import models

class asesorias(models.Model):
    Guia_Suplemento = models.CharField(max_length=100)
    Nutricion=models.TextField(max_length=350)
    Tarifa=models.IntegerField()
    Duracion=models.IntegerField()
