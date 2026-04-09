from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  
    path('messages_app/', include('messages_app.urls')),
]