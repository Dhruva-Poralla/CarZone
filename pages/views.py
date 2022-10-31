from django.shortcuts import render
from .models import Team
from cars.models import car
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


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
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']

        email_subject='you have a new message from CarZone website regarding '+subject
        message_body='Name:'+name+' .Email:'+email+'. Phone:'+phone+' .Message'+message

        admin_info=User.objects.get(is_superuser=True)
        admin_email=admin_info.email
        send_mail(
                email_subject,
                message_body,
                'gali_chirugali@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request,'Thank you for contacting us.we will get back to you shortly')
    return render(request,'pages/contact.html')
