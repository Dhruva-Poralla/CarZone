from django.shortcuts import render,redirect
from .models import contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def enquery(request):

    if request.method=="POST":
        if request.user.is_authenticated:

            car_id=request.POST['car_id']
            user_id=request.POST['user_id']
            car_title=request.POST['car_title']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            city=request.POST['city']
            state=request.POST['state']
            mobile_no=request.POST['phone']
            consumer_needs=request.POST['customer_need']
            message=request.POST['message']
            email=request.POST['email']

            has_contacted=contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already submitted the request,kindly be patient we will shortly contact you!!')
                return redirect('/cars/'+car_id)

            contacts=contact(car_id=car_id,user_id=user_id,car_title=car_title,first_name=first_name,last_name=last_name,city=city,state=state,mobile_no=mobile_no,consumer_needs=consumer_needs,message=message,email=email)

            admin_info=User.objects.get(is_superuser=True)
            admin_email=admin_info.email
            send_mail(
                    'New car enquery',
                    'You have a new inquiry for the car '+car_title+' .Please login to admin panel for more info!!',
                    'gali_chirugali@gmail.com',
                    [admin_email],
                    fail_silently=False,
                )

            contacts.save()
            messages.success(request,'Your request has been submitted ,we will contact shortly!!!')
            return redirect('/cars/'+car_id)
        else:
            return redirect('login')
