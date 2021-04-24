from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Boyband, Award, Photo
from .forms import SongForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'boybandcollector'
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def boybands_index(request):
    boybands = Boyband.objects.filter(user=request.user)
    # You could also retrieve the logged in user's cats like this
    # boybands = request.user.boyband_set.all()
    context = {'boybands': boybands}
    return render(request, 'boybands/index.html', context)

@login_required
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

@login_required
def add_song(request, boyband_id):
    form = SongForm(request.POST)
    if form.is_valid():
        new_song = form.save(commit=False)
        new_song.boyband_id = boyband_id
        new_song.save()
    return redirect('detail', boyband_id=boyband_id)

@login_required
def awards_index(request):
    awards = Award.objects.all()
    context = {'awards' : awards}
    return render(request, 'award/index.html', context)

@login_required
def assoc_award(request, boyband_id, award_id):
    Boyband.objects.get(id=boyband_id).awards.add(award_id)
    return redirect('detail', boyband_id=boyband_id)

@login_required
def remove_award(request, boyband_id, award_id):
    Boyband.objects.get(id=boyband_id).awards.remove(award_id)
    return redirect('detail', boyband_id=boyband_id)

@login_required
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
            # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class BoybandCreate(LoginRequiredMixin, CreateView):
    model = Boyband
    fields = ['name', 'decade', 'albums_sold', 'no_of_members']

    # This inherited method is called when a
    # valid boyband form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)



class BoybandUpdate(LoginRequiredMixin, UpdateView):
    model = Boyband
    fields = ['decade', 'albums_sold', 'no_of_members']

class BoybandDelete(LoginRequiredMixin, DeleteView):
    model = Boyband
    success_url = '/boybands/'

class AwardCreate(LoginRequiredMixin, CreateView):
    model = Award
    fields = '__all__'
    success_url = '/awards/'

class Update_Award(LoginRequiredMixin, UpdateView):
    model = Award
    fields = '__all__'

class Delete_Award(LoginRequiredMixin, DeleteView):
    model = Award
    success_url = '/awards/'