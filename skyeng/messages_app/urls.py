from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('inbox/', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('sent/', views.sent, name='sent'),
    path('drafts/', views.drafts, name='drafts'),
    path('trash/', views.trash, name='trash'),
]