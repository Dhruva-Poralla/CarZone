from django.shortcuts import render
from .models import Team
from cars.models import car


# Create your views here.
def Home(request):
    team=Team.objects.all()
    featured_cars=car.objects.order_by('-created_date').filter(is_feautered=True)
    all_cars=car.objects.order_by('-created_date')
    model_search=car.objects.values_list('model',flat=True).distinct()
    year_search=car.objects.values_list('year',flat=True).distinct()
    state_search=car.objects.values_list('state',flat=True).distinct()
    body_style_search=car.objects.values_list('body_style',flat=True).distinct()

    data={
        'team':team,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'year_search':year_search,
        'state_search':state_search,
        'body_style_search':body_style_search,
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
