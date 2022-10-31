from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import contact
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user != None:
            auth.login(request,user)
            messages.success(request,'you have logged..in successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid login credentials!!!')
            return redirect('login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request,'password is not matched')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'username is already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'email is already exists')
            return redirect('register')
        else:
            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
            auth.login(request,user)
            messages.success(request,'you have logged..in successfully')

            user.save()
            return redirect('dashboard')

    return render(request,'accounts/register.html')

@login_required(login_url='login')
def dashboard(request):
    enquery=contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    data={
        'enquery':enquery,
    }
    return render(request,'accounts/dashboard.html',data)

def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return redirect('Home')
