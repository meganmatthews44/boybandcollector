from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Boyband
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def boybands_index(request):
    boybands = Boyband.objects.all()
    context = {'boybands': boybands}
    return render(request, 'boybands/index.html', context)

def boybands_detail(request, boyband_id):
    boyband = Boyband.objects.get(id=boyband_id)
    context = {'boyband': boyband}
    return render(request, 'boybands/detail.html', context)

class BoybandCreate(CreateView):
    model = Boyband
    fields = '__all__'

class BoybandUpdate(UpdateView):
    model = Boyband
    fields = ['decade', 'albums_sold', 'no_of_members']

class BoybandDelete(DeleteView):
    model = Boyband
    success_url = '/boybands/'