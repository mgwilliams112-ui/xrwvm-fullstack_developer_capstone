from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    country_origin = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=50)
    CAR_TYPES = [
        ('CONVERTIBLE', 'Convertible'),
        ('COUP', 'Coup'),
        ('HATCHBACK', 'Hatchback'),
        ('PICKUP', 'Pickup'),
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=11, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(default=2026,
        validators=[
            MaxValueValidator(2026),
            MinValueValidator(2010)
        ])

    def __str__(self):
        return self.name

