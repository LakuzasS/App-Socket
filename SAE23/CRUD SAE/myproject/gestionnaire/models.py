from django.db import models

# Create your models here.

class Etudiant(models.Model):
    numero_etudiant = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    groupe = models.CharField(max_length=100)
    photo = models.BinaryField(null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class UnitesEnseignement(models.Model):
    code = models.TextField(primary_key=True)
    nom = models.TextField()
    semestre = models.IntegerField()
    credit_ects = models.IntegerField()

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Examen(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateField()
    coefficient = models.IntegerField()

    def __str__(self):
        return f"{self.titre}"

class RessourcesUE(models.Model):
    code = models.ForeignKey('gestionnaire.UnitesEnseignement', on_delete=models.CASCADE)
    code_ressource = models.CharField(primary_key=True, max_length=50)
    nom = models.TextField()
    descriptif = models.TextField()
    coefficient = models.IntegerField()

    def __str__(self):
        return f"{self.nom} - {self.code}"
    

class Note(models.Model):
    examen = models.ForeignKey('gestionnaire.Examen', on_delete=models.CASCADE)
    etudiant = models.ForeignKey('gestionnaire.Etudiant', on_delete=models.CASCADE)
    note = models.FloatField()
    appreciation = models.TextField()

    def __str__(self):
        return f"Note {self.pk}: {self.note} - {self.etudiant} - {self.examen}"


    




