from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.db.models import Count, Q

from .models import Sighting 

def index(request):
    return render(request, 'squirrels/index.html')

def map(request):
    sightings = list()
    for i in Sighting.objects.all():
        sightings.append(i)
    return render(request, 'squirrels/map.html', {'sightings': sightings})

def list_sightings(request):
    squirrels = Sighting.objects.all()
    return render(request, 'squirrels/sightings.html',{'squirrels': squirrels})

def get_sighting(request, squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_id = squirrel_id)
    return render(request, 'squirrels/detail.html',{'squirrel': squirrel})

def stats(request):
    data = Sighting.objects.annotate(id_count = Count('unique_squirrel_id'),adult_count = Count('age', filter = Q(age = 'Adult')))
    return render(request, 'squirrels/stats.html', {'data': data})


def add_sighting(request, longitude, latitude,unique_squirrel_id,  shift, date, age):
    s = Sighting(latitude = float(latitude),
            longitude = float(longitude),
            unique_squirrel_id = float(unique_squirrel_id),
            shift = shift,
            date = date,
            age = age
            )

    return render(request, 'squirrels/sightings.html', {'squirrel':squirrel} )
