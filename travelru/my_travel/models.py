from django.db import models
from django.conf import settings

# Create your models here.
# class User(models):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Item(models.Model):
    ITEM_TYPE = [
        ('HOTEL', 'Hotel'),
        ('AVIA', 'Avia')
        ]
#    id = models.AutoField()
    name = models.CharField(max_length=40)
    city_from = models.CharField(max_length=40)
    city_to = models.CharField(max_length=40)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPE)
    date_beg = models.DateField()
    time_beg = models.TimeField()
    date_end = models.DateField()
    time_end = models.TimeField()
    price = models.IntegerField()
    hotel_city = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    user


class Avia(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    link = models.CharField(max_length=300)


class Hotel(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)

