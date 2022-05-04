from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

# Create your views here.

def index(request):
    return render(request, 'home.html')

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'home.html', {'error': 'User credentials are not exist.'})

    return render(request, '<h1>Unknown error occured</h1>')

def register_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'home.html', {'error': 'There is such an account with your username!'})
            if User.objects.filter(email=email).exists():
                return render(request, 'home.html', {'error': 'There is such an account with your email address.'})
            user = User.objects.create_user(username=username, email=email, first_name='Unknown', last_name='User', password=password)
            user.save()
            messages.success(request, 'You have created an account succesfully!')
            return login_request(request)
        else:
            return render(request, 'home.html', {'error': 'Passwords do not match!'})

def logout_request(request):
    logout(request)
    messages.success(request, 'You have logged out succesfully!')
    return render(request, 'home.html')