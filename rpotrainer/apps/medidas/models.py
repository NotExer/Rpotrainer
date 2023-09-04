from django.db import models

class medidas(models.Model):
    Brazo_Izquierdo=models.IntegerField()
    Brazo_Derecho=models.IntegerField()
    Torax=models.IntegerField()
    Brazo_Relajado=models.IntegerField()
    Cadera=models.IntegerField()
    Cintura=models.IntegerField()
    Muslo_Derecho_Contraido=models.IntegerField()
    Muslo_Izquierdo_Contraido=models.IntegerField()
    Pantorrilla_Derecha_Contraida=models.IntegerField()
    Pantorrilla_Izquierda_Contraida=models.IntegerField()