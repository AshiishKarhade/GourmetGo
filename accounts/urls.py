from django.urls import path
from . import views

urlpatterns = [
    path('register_user', views.register_user, name='registerUser'),
    path('register_restaurant', views.register_restaurant, name='registerRestaurant'),
]