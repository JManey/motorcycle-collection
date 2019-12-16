from django.db import models

# Create your models here.

class Motorcycle(models.Model):
  brand = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  year = models.IntegerField()
  color = models.CharField(max_length=100)
  
  
