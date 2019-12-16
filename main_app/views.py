from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Motorcycle

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def motorcycles_index(request):
  motorcycles = Motorcycle.objects.all()
  return render(request, 'motorcycles/index.html', {'motorcycles': motorcycles})

def motorcycles_detail(request, motorcycle_id):
  motorcycle = Motorcycle.objects.get(id=motorcycle_id)
  return render(request, 'motorcycles/detail.html', { 'motorcycle': motorcycle })

class MotorcycleCreate(CreateView):
  model = Motorcycle
  fields = '__all__'

class MotorcycleUpdate(UpdateView):
  model = Motorcycle
  fields = '__all__'

class MotorcycleDelete(DeleteView):
  model = Motorcycle
  success_url = '/motorcycles/'
