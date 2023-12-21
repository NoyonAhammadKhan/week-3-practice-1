from django.contrib import admin
from django.urls import path, include
from .views import filter

urlpatterns = [
    path('', filter, name="filter"),
]
