from django.db import models

class entrenamiento(models.Model):
            Musculo = models.CharField(max_length=50)
            NombreEjercicio = models.CharField(max_length=50)
            Repeticiones = models.IntegerField()
            Series = models.IntegerField()
            Rir = models.IntegerField()
            MicroPausa = models.IntegerField()
            MacroPausa = models.IntegerField()
            Descripcion = models.CharField(max_length=500)
