from django.db import models

class entrenador(models.Model):
    nombre=models.CharField(max_length=50)   
    apellido=models.CharField(max_length=50)
    correo=models.EmailField(max_length=50)
    numero_contacto=models.IntegerField()