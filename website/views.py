from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages


# Create your views here.
def home(request):
    #checking for log in
    username =  request.POST['username']
    password = request.POST['password']  
    #authenticate
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Successful log in!!")
        return redirect('home')
    else:
        messages.success('Error loggin in!!')
        return redirect('home')
    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass