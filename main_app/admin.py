from django.contrib import admin

# Register your models here.
from .models import Boyband
from .models import Song
from .models import Award
from .models import Photo

admin.site.register(Boyband)
admin.site.register(Song)
admin.site.register(Award)
admin.site.register(Photo)