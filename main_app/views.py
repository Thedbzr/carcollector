from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car , Mod
from .forms import TuneupForm


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
  tuneup_form = TuneupForm()
  return render(request, 'cars/details.html', { 
    'car': car ,
    'tuneup_form': tuneup_form
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
  fields = '__all__'
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