from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, year, make, model, engine, vin):
    self.year = year
    self.make = make
    self.model = model
    self.engine = engine
    self.vin = vin

cars = [
  Car('1998','Mazda','Rx-7 FD3S', '1.3 L (79 cu in) twin-turbocharged 13B-REW twin-rotor', '1HGFA16876L019518'),
  Car('1999','Honda','NSX-R', '3,179 cc (3.2 L; 194.0 cu in) Honda C32B V6','1N4AB41D8TC705337'),
  Car('2000','Toyota','Supra MKIV', '3.0 liter (2,997 cc, 182.89 cu-in) straight-six, four-stroke cycle twin-turbocharged 2JZ-GTE','1N4AB41D8TC705337'),
  Car('2001','Nissan','Skyline GT-R','2.6 L twin-turbocharged RB26DETT I6 2.8 L twin-turbocharged RB28DETT I6 (Z-Tune)','1N4AB41D8TC705337'),
]


# Define the home view
def home(request):
    return HttpResponse('<h1>2jz Power...RB26...LS...? Oh Hi there!</h1>')
def about(request):
  return render(request, 'about.html')
def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })