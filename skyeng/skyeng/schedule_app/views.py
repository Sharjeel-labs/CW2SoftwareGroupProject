from django.shortcuts import render


def schedule(request):
    return render(request, 'schedule_app/schedule.html')
