from django.db import models

class nutricion(models.Model):
    Tarifa=models.IntegerField()
    Duracion=models.IntegerField()
    Guia_Alimentos=models.TextField(max_length=350)
    Lista_Alimentos=models.TextField(max_length=350)
