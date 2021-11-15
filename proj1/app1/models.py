from django.db import models

class Laptop(models.Model):
    lname = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    price = models.FloatField()
    ram = models.IntegerField()
