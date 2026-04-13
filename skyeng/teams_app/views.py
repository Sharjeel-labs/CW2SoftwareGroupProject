from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Team, Department

# Create your views here.
#def teams(request):
    #return render(request, 'teams_app/teams.html')

def teams(request):
    query = request.GET.get('search')
    
    if query:
        teams = Team.objects.filter(name__icontains=query)
    else:
        teams = Team.objects.all()



    context = {
        'teams' : teams,
        'total_teams' : Team.objects.count(),
        'total_departments' : Department.objects.count(),
        'active_teams' : Team.objects.filter(active=True).count(),
    }

    return render(request, 'teams_app/teams.html', context)