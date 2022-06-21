"""
models
"""
from django.db import models


# Create your models here.
class Country(models.Model):
    db_id = models.PositiveIntegerField(primary_key=True)
    name_rus = models.CharField(max_length=100, blank=False, unique=True)
    name_eng = models.CharField(max_length=100, unique=True, null=True)
    code_eng = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.name_rus


class City(models.Model):
    country = models.ForeignKey(Country, default=1, on_delete=models.CASCADE)
    id_aviasales = models.PositiveIntegerField(default=0, null=True)
    name_rus = models.CharField(max_length=70, blank=False, unique=True, primary_key=True)
    name_eng = models.CharField(max_length=70, null=True)

    def __str__(self):
        return self.name_rus


class Airport(models.Model):
    city = models.ForeignKey(City, default="Москва", on_delete=models.CASCADE)
    name_rus = models.CharField(max_length=70, blank=False, unique=True)
    name_eng = models.CharField(max_length=70, null=True, unique=True)
    code_IATA = models.CharField(max_length=3, null=True, unique=True)
    code_ICAO = models.CharField(max_length=4, null=True, unique=True)
    code_rus = models.CharField(max_length=3, null=True, unique=True)

    def __str__(self):
        return self.name_rus
