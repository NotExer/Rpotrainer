from django.db import models

class nutricion(models.Model):
    dia=models.TextField(max_length=350)
    hora=models.TextField(max_length=350)
    tipo_comida=models.TextField(max_length=350)
    alimento=models.TextField(max_length=350)
    porcion=models.TextField(max_length=350)
    evitar=models.TextField(max_length=350)
    otras_recomendaciones=models.TextField(max_length=350)
    ingesta_agua=models.TextField(max_length=350)
    dia_trampa=models.TextField(max_length=350)
    suplementos=models.TextField(max_length=350)
    lista_compra=models.TextField(max_length=350)
