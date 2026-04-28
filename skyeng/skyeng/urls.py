from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    


    path('', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('reports/', include('reports_app.urls')),

]
#Allows for the reports page to view reports
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)