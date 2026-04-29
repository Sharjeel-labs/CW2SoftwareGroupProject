from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main dashboard (from main branch)
    path('', views.dashboard, name='dashboard'),

    # Student 3 - Messages app
    path('messages_app/', include('messages_app.urls')),

    # Teams app (from main branch)
    path('', include('teams_app.urls')),

    # Accounts/login (from main branch)
    path('', include('accounts.urls')),
]