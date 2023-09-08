from django.db import models

class entrenamiento(models.Model):
            musculo = models.TextField(max_length=25)
            ejercicio = models.TextField(max_length=25)
            series = models.FloatField(max_length=25)
            repeticiones = models.FloatField(max_length=25)
            rir = models.FloatField(max_length=25)
            cadencia = models.FloatField(max_length=25)
            microPausa = models.FloatField(max_length=25)
            macroPausa = models.FloatField(max_length=25)
            descripcion = models.TextField(max_length=25)
            imagen = models.ImageField()