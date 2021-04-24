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
    path('boybands/<int:boyband_id>/add_song/', views.add_song, name="add_song"),

    path('awards/', views.awards_index, name='all_awards'),
    path('awards/create/', views.AwardCreate.as_view(), name='create_award'),
    path('awards/<int:pk>/update/', views.Update_Award.as_view(), name='update_award'),
    path('awards/<int:pk>/delete/', views.Delete_Award.as_view(), name='delete_award'),

    path('boybands/<int:boyband_id>/assoc_award/<int:award_id>/', views.assoc_award, name='assoc_award'),
    path('boybands/<int:boyband_id>/remove_award/<int:award_id>/', views.remove_award, name='remove_award'),
    path('boybands/<int:boyband_id>/add_photo/', views.add_photo, name='add_photo'),

    path('accounts/signup/', views.signup, name='signup'),
]