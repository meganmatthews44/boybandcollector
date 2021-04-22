from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Boyband, Award, Photo
from .forms import SongForm

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'boybandcollector'
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
    awards_boyband_doesnt_have = Award.objects.exclude(id__in = boyband.awards.all().values_list('id'))
    song_form = SongForm()
    context = {
        'boyband': boyband, 
        'song_form': song_form,
        'awards': awards_boyband_doesnt_have,
        }
    return render(request, 'boybands/detail.html', context)

def add_song(request, boyband_id):
    form = SongForm(request.POST)
    if form.is_valid():
        new_song = form.save(commit=False)
        new_song.boyband_id = boyband_id
        new_song.save()
    return redirect('detail', boyband_id=boyband_id)

def awards_index(request):
    awards = Award.objects.all()
    context = {'awards' : awards}
    return render(request, 'award/index.html', context)

def assoc_award(request, boyband_id, award_id):
    Boyband.objects.get(id=boyband_id).awards.add(award_id)
    return redirect('detail', boyband_id=boyband_id)

def remove_award(request, boyband_id, award_id):
    Boyband.objects.get(id=boyband_id).awards.remove(award_id)
    return redirect('detail', boyband_id=boyband_id)

def add_photo(request, boyband_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, boyband_id=boyband_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', boyband_id=boyband_id)

class BoybandCreate(CreateView):
    model = Boyband
    fields = ['name', 'decade', 'albums_sold', 'no_of_members']

class BoybandUpdate(UpdateView):
    model = Boyband
    fields = ['decade', 'albums_sold', 'no_of_members']

class BoybandDelete(DeleteView):
    model = Boyband
    success_url = '/boybands/'

class AwardCreate(CreateView):
    model = Award
    fields = '__all__'
    success_url = '/awards/'

class Update_Award(UpdateView):
    model = Award
    fields = '__all__'

class Delete_Award(DeleteView):
    model = Award
    success_url = '/awards/'