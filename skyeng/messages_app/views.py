# Create your views here.
from django.shortcuts import render

def inbox(request):
    return render(request, 'messages_app/inbox.html')