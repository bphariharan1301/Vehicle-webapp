
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_vehicle', views.add_vehicle, name='add_vehicle'),
    path('remove_vehicle', views.remove_vehicle, name='remove_vehicle'),
    path('list_vehicle', views.list_vehicle, name='list_vehicle'),
    path('vehicle_details/<int:id>', views.vehicle_details, name='vehicle_details'),
    # path('vehicle_details/', views.vehicle_details, name='vehicle_details'),
]
