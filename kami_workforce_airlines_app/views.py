from django.shortcuts import render
from django.http import HttpResponse
from .models import Airplane

def index(request):
    airlines_list = Airplane.objects.all()
    return HttpResponse(airlines_list)