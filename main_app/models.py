from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

MAINTENANCE = (
  ('Oil', 3000),
  ('Chain', 500),
  ('Tires', 7000)
)

class Acc(models.Model):
  name = models.CharField(max_length=100)
  size = models.CharField(max_length=100)
  color = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("accs_detail", kwargs={'pk': self.id})
      

class Motorcycle(models.Model):
  brand = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  year = models.IntegerField()
  color = models.CharField(max_length=100)
  mileage = models.IntegerField(default=100)
  accs = models.ManyToManyField(Acc)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'A {self.brand} {self.model}'

  def get_absolute_url(self):
      return reverse("detail", kwargs={"motorcycle_id": self.id})
  
class Photo(models.Model):
  url = models.CharField(max_length=200)
  motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for motorcycle_id: {self.motorcycle_id} @{self.url}"

class maint(models.Model):
  done = models.IntegerField()
  maintenance = models.CharField(
    max_length=50,
    choices=MAINTENANCE,
    default=MAINTENANCE[0][0],
  )
  motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)
  def __str__(self):
    return f"Maintenance due in x miles"
