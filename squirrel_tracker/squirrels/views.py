from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def index(request):
    return HttpResponse("Hi This is a  squirrels tracker app.")

def map(request):
    location = list()
    for i in Squirrel.objects.all():
        location_dict = {}
        location_dict['latitude'] = i.latitude
        location_dict['longitude'] = i.longitude
        location.append(location_dict)
    return render(request, 'squirrels/map.html', {'location':location})
        

# Create your views here.
