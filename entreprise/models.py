from posixpath import supports_unicode_filenames
from django.db import models

# Create your models here.
class Entreprise(models.Model):
    name = models.CharField(max_length=32)
    logopath = models.ImageField(upload_to='uploads/')
    numeroEnt = models.IntegerField()
    namePDG = models.CharField(max_length=30)

class Employe(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=30)
    sex = models.BooleanField()
    nationality = models.CharField(max_length=60)
    numRegNat = models.IntegerField()
    numAccount = models.CharField(max_length=40)
    stateCivil = models.CharField(max_length=60)
    adresse = models.CharField(max_length=60)

class rank(models.Model):
    name = models.CharField(max_length=60)
    levelRank = models.IntegerField()

class relationnel(models.Model):
    idEnt = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    idEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)
    idRank = models.ForeignKey(rank, on_delete=models.CASCADE)