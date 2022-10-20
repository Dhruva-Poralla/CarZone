from django.shortcuts import render
from .models import Team

# Create your views here.
def Home(request):
    team=Team.objects.all()
    data={
        'team':team,
    }
    return render(request,'pages/Home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')


def contact(request):
    return render(request,'pages/contact.html')
