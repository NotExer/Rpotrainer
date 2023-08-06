from django.db import models

class diagnostico(models.Model):
    Objetivo_Fisico=models.CharField(max_length=900)
    Nivel_entrenamiento_años=models.IntegerField()
    Frecuencia_semanal=models.IntegerField()
    Dias_de_entrenamiento=models.IntegerField()
    Tiempo_Por_Sesion=models.IntegerField()
    Material_Entreno=models.CharField(max_length=50)
    Fuma=models.CharField(max_length=50)
    Consume_alcohol=models.CharField(max_length=50)
    Cirugias_anteriores=models.CharField(max_length=200)
    Entrenos_anteriores=models.CharField(max_length=200)
    Enfermedad_de_base=models.CharField(max_length=200)
    Fracturas=models.CharField(max_length=50)
    Tiempo_sueño=models.IntegerField()