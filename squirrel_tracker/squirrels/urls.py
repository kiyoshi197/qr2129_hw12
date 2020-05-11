from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('map/',views.map, name = "map"),
    path('sightings/', views.list_sightings, name = 'list_sightings'),
    path('sightings/<str:squirrel_id>/', views.get_sighting, name = 'get_sighting'),
    path('sightings/add/', views.get_sighting, name = 'add_sighting'),
    path('stats/', views.stats, name ='stats'),
]
