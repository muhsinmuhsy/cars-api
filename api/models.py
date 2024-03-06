from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="car-image", null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)