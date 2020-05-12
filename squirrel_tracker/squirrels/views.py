from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.db.models import Count, Q
from django.db.models import Avg

from .models import Sighting 

def index(request):
    return render(request, 'squirrels/index.html')

def map(request):
    sightings = list()
    for i in Sighting.objects.all().order_by('date'):
        sightings.append(i)
    return render(request, 'squirrels/map.html', {'sightings': sightings[-50:]})

def list_sightings(request):
    squirrels = Sighting.objects.all()
    return render(request, 'squirrels/sightings.html',{'squirrels': squirrels})

def get_sighting(request, squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_id = squirrel_id)
    return render(request, 'squirrels/detail.html',{'squirrel': squirrel})

def stats(request):
    a_count = Sighting.objects.filter(age = 'Adult').count()
    j_count = Sighting.objects.filter(age = 'Juvenile').count()
    am = Sighting.objects.filter(shift = 'am').count()
    pm = Sighting.objects.filter(shift = 'pm').count()
    average_longitude = Sighting.objects.all().aggregate(Avg('longitude'))
    average_latitude = Sighting.objects.all().aggregate(Avg('latitude'))

    return render(request, 'squirrels/stats.html', {'a_count': a_count,'j_count':j_count,'am': am ,'pm': pm, 'avg_longitude': average_longitude, 'avg_latitude': average_latitude})

def add_sighting(request, longitude, latitude,unique_squirrel_id,  shift, date, age):
    s = Sighting(latitude = float(latitude),
            longitude = float(longitude),
            unique_squirrel_id = float(unique_squirrel_id),
            shift = shift,
            date = date,
            age = age
            )

    return render(request, 'squirrels/sightings.html', {'squirrel':squirrel} )
