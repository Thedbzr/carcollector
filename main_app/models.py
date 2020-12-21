from django.db import models
from django.urls import reverse

SERVICES = (
    ('O', 'OilChange'),
    ('S', 'SparkPlugs'),
    ('C', 'CoilPacks'),
    ('B', 'Brakes'),
    ('R', 'Rotors'),
    ('F', 'Fluids')
)

# Modifications
class Mod(models.Model):
    category: models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('mods_detail', kwargs={'pk': self.id})


# Create your models here.
class Car(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    engine = models.CharField(max_length=200)
    vin = models.IntegerField()
    # Adds M:M relationship
    mods = models.ManyToManyField(Mod)
    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Tuneup(models.Model):
    date = models.DateField('Tuneup date')
    service = models.CharField(
        max_length=1,
        choices=SERVICES,
        default=SERVICES[0][0]
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['-date']