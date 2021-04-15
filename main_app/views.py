from django.shortcuts import render
from django.http import HttpResponse
from .models import Boyband
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def boybands_index(request):
    boybands = Boyband.objects.all()
    return render(request, 'boybands/index.html', {'boybands': boybands})