from django.contrib import admin
from django.urls import path, include
from .views import index, home

urlpatterns = [
    path("", index),
    path("home/", home),
]
