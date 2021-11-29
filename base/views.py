from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from base.models import Vehicle

# Create your views here.

def home(request):
  return render(request, 'base/home.html')

def add_vehicle(request):
  if request.method == 'POST':
    name = request.POST['name']
    speed = request.POST['speed']
    avg_speed = request.POST['avg_speed']
    temp = request.POST['temp']
    fuel_level = request.POST['fuel_level']
    engine_status = request.POST['engine_status']

    vehicle = Vehicle(name=name, speed=speed, avg_speed=avg_speed, temp=temp, fuel_level=fuel_level, engine_status=engine_status)

    vehicle.save()

    messages.success(request, 'The Vehicle has been added')

    return redirect('home')
  else: 
    return render(request, 'base/add_vehicle.html')

def remove_vehicle(request, id):
  
  vehicle = get_object_or_404(Vehicle, pk=id)

  vehicle.delete()

  return redirect('list_vehicle')

def list_vehicle(request):
  vehicles = Vehicle.objects.all()

  context = {
    'vehicles':vehicles,
  }

  return render(request, 'base/list_vehicle.html', context)


def vehicle_details(request, id):

  # vehicle = get_object_or_404(Vehicle, pk=id)
  vehicle_detail = get_object_or_404(Vehicle, pk=id)
  # listing = get_object_or_404(Vehicle, pk=id)

  # vehicle = get_object_or_404(Listing, pk=listing_id)

  # print(vehicle)

  context = {
    'vehicle_detail': vehicle_detail
  }


  return render(request, 'base/vehicle_details.html', context)


