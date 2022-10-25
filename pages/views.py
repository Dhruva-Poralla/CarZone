from django.shortcuts import render
from .models import Team
from cars.models import car


# Create your views here.
def Home(request):
    team=Team.objects.all()
    featured_cars=car.objects.order_by('-created_date').filter(is_feautered=True)
    all_cars=car.objects.order_by('-created_date')
    data={
        'team':team,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
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
