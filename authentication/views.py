from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
  return render(request, 'home.html')

def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    first_name = request.POST['first_name']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
      if User.objects.filter(username=username).exists():
          print('Username already taken')
      elif User.objects.filter(email=email).exists():
          print('Email already registered')
      else:
          user = User.objects.create_user(
              username=username,
              first_name=first_name,
              email=email,
              password=password1
          )
          user.save()
          print('User registration successful')
          return redirect('index')
    else:
          print('Passwords do not match')

  return render(request, 'registerations.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)  # Rename login to auth_login
        print('Login successful')
        return redirect('index')
    else:
        print('Invalid login credentials')
        return redirect('login')

  return render(request, 'registerations.html')
