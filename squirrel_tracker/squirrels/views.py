from django.shortcuts import render
from django.http import Httpresponse


def index(request):
    return HttpResponse("Hi This is a  squirrels tracker app.")

# Create your views here.
