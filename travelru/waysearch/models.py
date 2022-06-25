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
    code_eng = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.name_rus

    @classmethod
    def import_from_file(cls):
        filename = '.\waysearch\IATA_aiports.txt'
        with open(filename, 'r') as f:
            str_lines =f.read().splitlines()
#           print(str_list1[1])
            for line in str_lines:
                words = line.split('\t')
                print(f"length: {cls.objects.filter(name_rus=words[0]).count()}")
                if cls.objects.filter(name_rus=words[0]).count() == 0:
                    print(f"{words[0]} - new city add")
                    new_city = City(name_rus=words[0])
                    new_city.save()
                else:
                    print(f"{words[0]} - city already exists")



class Airport(models.Model):
    city = models.ForeignKey(City, default="Москва", on_delete=models.CASCADE)
    name_rus = models.CharField(max_length=70, blank=False, unique=True)
    name_eng = models.CharField(max_length=70, null=True)
    code_IATA = models.CharField(max_length=3, null=True, unique=True)
    code_ICAO = models.CharField(max_length=4, null=True)
    code_rus = models.CharField(max_length=3, null=True)

    def __str__(self):
        ret_string = f"{self.name_rus}({self.code_IATA}), г.{self.city.name_rus}"
        return ret_string

    @classmethod
    def import_from_file(cls):
        filename = '.\waysearch\IATA_aiports.txt'
        with open(filename, 'r') as f:
            str_lines =f.read().splitlines()
#           print(str_list1[1])
            for line in str_lines:
                words = line.split('\t')
                print(f"city={City.objects.get(name_rus=words[0])}, name_rus={words[1]}, code_IATA={words[2]}, "
                      f"code_ICAO={words[3]},  code_rus={words[4]}")
                if cls.objects.filter(name_rus=words[1]).count() == 0:
                    if not words[2] == " ":
                        print(f"{words[1]} - new airport add")
                        new_airport = Airport(city=City.objects.get(name_rus=words[0]), name_rus=words[1], code_IATA=words[2],
                                              code_ICAO=words[3], code_rus=words[4])
                        new_airport.save()
                    else:
                        print(f"{words[2]} - NO CODE")
                else:
                    print(f"{words[1]} - ERROR! airport already exists")

