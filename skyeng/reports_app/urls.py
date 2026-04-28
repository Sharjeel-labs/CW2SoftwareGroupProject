from django.urls import path

from . import views

urlpatterns = [
    path('', views.reports, name='reports'),
    path('test-pdf/', views.test_pdf, name='test_pdf')
]
