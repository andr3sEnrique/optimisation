from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request, name):
    return HttpResponse("Bonjour depuis Django " + name)