from django.db import models

# Create your models here.
class Car(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    engine = models.CharField(max_length=200)
    vin = models.IntegerField()
    def __str__(self):
        return self.model
