from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Sighting 

def index(request):
    return render(request, 'squirrels/index.html')

def map(request):
    location = list()
    for i in Sighting.objects.all():
        location_dict = {}
        location_dict['latitude'] = i.latitude
        location_dict['longitude'] = i.longitude
        location.append(location_dict)
    return render(request, 'squirrels/map.html', {'location':location})

def list_sightings(request):
    squirrels = Sighting.objects.all()
    return render(request, 'squirrels/sightings.html',{'squirrels': squirrels})

def get_sighting(request, squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_id = squirrel_id)
    return render(request, 'squirrels/sightings.html', {'squirrel':squirrel})

def add_sighting(request, longitude, latitude,unique_squirrel_id,  shift, date, age):
    s = Sighting(latitude = float(latitude),
            longitude = float(longitude),
            unique_squirrel_id = float(unique_squirrel_id),
            shift = shift,
            date = date,
            age = age
            )

    return render(request, 'squirrels/sightings.html', {'squirrel':squirrel} )
