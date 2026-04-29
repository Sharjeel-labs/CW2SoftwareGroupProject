<<<<<<< HEAD
=======
from django.urls import path
>>>>>>> s5-reports
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.dashboard, name='dashboard'),
    path('', include('teams_app.urls')),
    path('', include('accounts.urls')),
    path('', include('schedule_app.urls')),
]
=======
    


    path('', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('reports/', include('reports_app.urls')),

]
#Allows for the reports page to view reports
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> s5-reports
