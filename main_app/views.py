from django.shortcuts import render
from django.http import HttpResponse
from .models import Motorcycle

# Create your views here.
def home(request):
  return HttpResponse('<h1> hello</h1>')

def about(request):
  return render(request, 'about.html')

def motorcycles_index(request):
  motorcycles = Motorcycle.objects.all()
  return render(request, 'motorcycles/index.html', {'motorcycles': motorcycles})

def motorcycles_detail(request, motorcycle_id):
  motorcycle = Motorcycle.objects.get(id=motorcycle_id)
  return render(request, 'motorcycles/detail.html', { 'motorcycle': motorcycle })