from django.shortcuts import render , redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        return
    else:
        return render(request, 'accounts/login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email Taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')
        messages.error(request,'Something went wrong.')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
