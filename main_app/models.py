from django.db import models
from django.urls import reverse
# Create your models here.

class Acc(models.Model):
  name = models.CharField(max_length=100)
  size = models.CharField(max_length=100)
  color = models.CharField(max_length=100)

# class oil_due(model.Models):
#   return self.


class Motorcycle(models.Model):
  brand = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  year = models.IntegerField()
  color = models.CharField(max_length=100)
  mileage = models.IntegerField(default=100)
  accs = models.ManyToManyField(Acc)
  
  def __str__(self):
    return f'A {self.brand} {self.model}'

  def get_absolute_url(self):
      return reverse("detail", kwargs={"motorcycle_id": self.id})
  


