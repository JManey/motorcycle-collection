from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Motorcycle, Acc, Photo

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'cat-image-collector'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def motorcycles_index(request):
  motorcycles = Motorcycle.objects.all()
  return render(request, 'motorcycles/index.html', {'motorcycles': motorcycles})

@login_required
def motorcycles_detail(request, motorcycle_id):
  motorcycle = Motorcycle.objects.get(id=motorcycle_id)
  accs_not_included = Acc.objects.exclude(id__in = motorcycle.accs.all().values_list('id'))

  return render(request, 'motorcycles/detail.html', { 
    'motorcycle': motorcycle , 'accs': accs_not_included
  })

class MotorcycleCreate(LoginRequiredMixin, CreateView):
  model = Motorcycle
  fields = '__all__'

class MotorcycleUpdate(LoginRequiredMixin, UpdateView):
  model = Motorcycle
  fields = '__all__'

class MotorcycleDelete(LoginRequiredMixin, DeleteView):
  model = Motorcycle
  success_url = '/motorcycles/'

@login_required
def assoc_acc(request, motorcycle_id, acc_id):
  Motorcycle.objects.get(id=motorcycle_id).accs.add(acc_id)
  return redirect('detail', motorcycle_id=motorcycle_id)

@login_required
def unassoc_acc(request, motorcycle_id, acc_id):
  Motorcycle.objects.get(id=motorcycle_id).accs.remove(acc_id)
  return redirect('detail', motorcycle_id=motorcycle_id)

@login_required
def add_photo(request, motorcycle_id):
  	# photo-file was the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to motorcycle_id or motorcycle (if you have a motorcycle object)
      photo = Photo(url=url, motorcycle_id=motorcycle_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', motorcycle_id=motorcycle_id)

class AccList(LoginRequiredMixin, ListView):
  model = Motorcycle

class AccDetail(LoginRequiredMixin, DetailView):
  model = Motorcycle

class AccCreate(LoginRequiredMixin, CreateView):
  model = Motorcycle
  fields = '__all__'

class AccUpdate(LoginRequiredMixin, UpdateView):
  model = Motorcycle
  fields = ['motorcycle', 'color']

class AccDelete(LoginRequiredMixin, DeleteView):
  model = Motorcycle
  success_url = '/motorcycles/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user'form object
    # that include the data form browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)