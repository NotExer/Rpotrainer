from django.db import models

class cliente(models.Model):
    
    Nombre = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Edad = models.IntegerField()
    Telefono = models.CharField(max_length=20)
    Email = models.EmailField()
    Domicilio = models.CharField(max_length=200)
    
    def __str__(self):
        return '{} {}'.format(self.Nombre,self.Apellidos)
    