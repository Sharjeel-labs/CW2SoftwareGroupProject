from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    


    path('', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('reports/', include('reports_app.urls')),
    


]