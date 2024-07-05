from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=10)


class Operation(models.Model):
    keyword = models.CharField(max_length=20)
    address = models.TextField()
    vehicles = models.TextField()
    dispatched = models.DateTimeField(auto_now_add=True)
