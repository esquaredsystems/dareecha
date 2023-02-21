from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('baham/members', views.view_members, name='members'),
    path('baham/vehicles', views.view_vehicles, name='vehicles'),
    path('baham/aboutus', views.view_aboutus, name='aboutus'),
]