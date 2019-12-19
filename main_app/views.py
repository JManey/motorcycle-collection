from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
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