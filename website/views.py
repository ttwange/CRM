from django.shortcuts import render
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages


# Create your views here.
def home(request):
    #checking for log in
    username =  request.POST['username']
    password = request.POST['password']  
    #authenticate
    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass