from django.db import models


class Fahrzeug(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=10)


class Logmessage(models.Model):
    stichwort = models.CharField(max_length=20)
    adresse = models.TextField()
    fahrzeuge = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
