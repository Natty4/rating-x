from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vote/<pk>/', views.vote, name='vote'),
    path('create/', views.create, name='create'),
    path('results/<pk>/', views.results, name='results'),
]