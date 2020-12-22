from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import TuneupForm
import uuid
import boto3
from .models import Car , Mod , Photo

# Add these "constant" variables below the imports
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'carcollector-seir-1026-alm'


# Define the home view
def home(request):
    return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })
def cars_details(request, car_id):
  car = Car.objects.get(id=car_id)
  mods_car_doesnt_have = Mod.objects.exclude(id__in = car.mods.all().values_list('id'))
  tuneup_form = TuneupForm()
  return render(request, 'cars/details.html', { 
    'car': car ,
    'tuneup_form': tuneup_form,
    'mods': mods_car_doesnt_have
    })
def add_tuneup(request, car_id):
	# create the ModelForm using the data in request.POST
  form = TuneupForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the car_id assigned
    new_service = form.save(commit=False)
    new_service.car_id = car_id
    new_service.save()
  return redirect('detail', car_id=car_id)

def assoc_mod(request, car_id, mod_id):
  # Note that you can pass a mod's id instead of the whole object
  Car.objects.get(id=car_id).mods.add(mod_id)
  return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
  model = Car
  fields = ['year', 'make', 'model', 'engine', 'vin']
class CarUpdate(UpdateView):
  model = Car
  fields = ['engine']
class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

class ModList(ListView):
  model = Mod

class ModDetail(DetailView):
  model = Mod

class ModCreate(CreateView):
  model = Mod
  fields = '__all__'

class ModUpdate(UpdateView):
  model = Mod
  fields = '__all__'

class ModDelete(DeleteView):
  model = Mod
  success_url = '/mods/'

def add_photo(request, car_id):
  photo_file = request.FILES.get('photo-file',None)
  if photo_file:
    s3 = boto3.client('s3')
    #need a unique key
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file,BUCKET,key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, car_id=car_id)
    except:
      print('An error occured uploading file to S3')
  return redirect('detail', car_id=car_id)