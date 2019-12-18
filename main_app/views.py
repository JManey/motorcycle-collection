from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Motorcycle, Acc

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
  accs_not_included = Acc.objects.exclude(id__in = motorcycle.accs.all().values_list('id'))

  return render(request, 'motorcycles/detail.html', { 
    'motorcycle': motorcycle , 'accs': accs_not_included
  })

class MotorcycleCreate(CreateView):
  model = Motorcycle
  fields = '__all__'

class MotorcycleUpdate(UpdateView):
  model = Motorcycle
  fields = '__all__'

class MotorcycleDelete(DeleteView):
  model = Motorcycle
  success_url = '/motorcycles/'

def assoc_acc(request, motorcycle_id, acc_id):
  Motorcycle.objects.get(id=motorcycle_id).accs.add(acc_id)
  return redirect('detail', motorcycle_id=motorcycle_id)

def unassoc_acc(request, motorcycle_id, acc_id):
  Motorcycle.objects.get(id=motorcycle_id).accs.remove(acc_id)
  return redirect('detail', motorcycle_id=motorcycle_id)
