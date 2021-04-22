from django.db import models
from django.urls import reverse

# Create your models here.

RATINGS = (
    ('G', 'Good'),
    ('O', 'Okay'),
    ('B', 'Bad')
)

class Award(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('all_awards')

class Boyband(models.Model):
    name = models.CharField(max_length=100)
    decade = models.TextField(max_length=5)
    albums_sold = models.TextField(max_length=100)
    no_of_members = models.IntegerField()
    awards = models.ManyToManyField(Award)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'boyband_id': self.id})

class Song(models.Model):
    date = models.DateField('release date')
    title = models.CharField(max_length=50)
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0])
    
    boyband = models.ForeignKey(Boyband, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Song:{self.title} released on {self.date} User rating:{self.get_rating_display()}"

    class Meta:
        ordering = ['date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    boyband = models.ForeignKey(Boyband, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for boyband_id: {self.boyband_id} @{self.url}'