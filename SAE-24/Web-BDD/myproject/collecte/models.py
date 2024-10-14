from django.db import models
from django.utils import timezone

class Capteur(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    nom = models.CharField(max_length=100, unique=True)
    piece = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)
    def __str__(self):
        return self.nom


class Donnee(models.Model):
    id = models.AutoField(primary_key=True)
    capteur = models.ForeignKey('Capteur', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField(max_length=5)
    presence = models.BooleanField(default=False) 
    nombre_individus = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.capteur} - {self.timestamp}"


