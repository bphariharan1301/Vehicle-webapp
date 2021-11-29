from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Vehicle(models.Model):
  name = models.CharField(max_length=100)
  photo_main = CloudinaryField('vehicle', blank=True)
  speed = models.DecimalField(max_digits=5, decimal_places=2)
  avg_speed = models.DecimalField(max_digits=5, decimal_places=2)
  temp = models.DecimalField(max_digits=5, decimal_places=2)
  fuel_level = models.DecimalField(max_digits=5, decimal_places=2)
  engine_status = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return self.name


