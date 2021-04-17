from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('boybands/', views.boybands_index, name="index"),
    path('boybands/<int:boyband_id>/', views.boybands_detail, name='detail'),
]