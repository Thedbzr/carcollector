from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
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

class CarCreate(CreateView):
  model = Car
  fields = '__all__'
class CarUpdate(UpdateView):
  model = Car
  fields = ['engine']
class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'