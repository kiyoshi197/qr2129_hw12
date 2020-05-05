from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('map/',views.map, name = "map"),
    path('sightings/', views.list_sightings, name = 'list_sightings'),
    path('sighintgs/<slug:squirrel_id>', views.get_sighting, name = 'get_sighting'),
]
