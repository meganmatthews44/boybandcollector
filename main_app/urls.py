from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('boybands/', views.boybands_index, name="index"),
    path('boybands/<int:boyband_id>/', views.boybands_detail, name='detail'),
    path('boybands/create/', views.BoybandCreate.as_view(), name='boybands_create'),
    path('boybands/<int:pk>/update/', views.BoybandUpdate.as_view(), name='boybands_update'),
    path('boybands/<int:pk>/delete/', views.BoybandDelete.as_view(), name='boybands_delete'),
]