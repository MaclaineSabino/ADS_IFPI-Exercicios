from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Alô, Mundo!")
# Create your views here.
