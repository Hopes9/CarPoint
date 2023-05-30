from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class State(models.Model):
    state_id = models.CharField(max_length=2)
    state_name = models.CharField(max_length=100)


class County(models.Model):
    county_fips = models.CharField(max_length=5)
    county_name = models.CharField(max_length=100)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)


class Location(models.Model):
    zip = models.IntegerField(primary_key=True, unique=True)
    lat = models.FloatField()
    lng = models.FloatField()
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.city


class Cargo(models.Model):
    pickup_lat = models.FloatField()
    pickup_lng = models.FloatField()
    zipCode = models.ForeignKey(Location, on_delete=models.CASCADE)
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()

    def __str__(self):
        return f"Cargo #{self.id}"


class Car(models.Model):
    number = models.CharField(max_length=5, unique=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    carrying_capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    def __str__(self):
        return f"Car #{self.number}"
