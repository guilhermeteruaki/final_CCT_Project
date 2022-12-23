from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


# Create your views here.

def home(request):
    #pagename = Main.objects.get(name="My site")
    return render(request, 'front/home.html')

def about(request):
    pagename = Main.objects.get(name="My site")
    return render(request, 'front/about.html', {"pagename":pagename})