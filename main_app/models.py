from django.db import models

# Create your models here.

class Boyband(models.Model):
    name = models.CharField(max_length=100)
    decade = models.TextField(max_length=5)
    albums_sold = models.TextField(max_length=100)
    no_of_members = models.IntegerField()

    def __str__(self):
        return self.name