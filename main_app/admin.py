from django.contrib import admin

# Register your models here.
from .models import Boyband
from .models import Song

admin.site.register(Boyband)
admin.site.register(Song)