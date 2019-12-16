from django.db import models
from django.urls import reverse
# Create your models here.

class Motorcycle(models.Model):
  brand = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  year = models.IntegerField()
  color = models.CharField(max_length=100)
  
  def __str__(self):
    return self.brand, self.model

  def get_absolute_url(self):
      return reverse("detail", kwargs={"motorcycle_id": self.id})
  
  
