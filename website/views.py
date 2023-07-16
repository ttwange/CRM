from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .forms import *
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    context = {'records':records}

    #checking for log in
    if request.method == 'POST':
      username =  request.POST['username']
      password = request.POST['password']  
      #authenticate
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          messages.success(request, "Successful log in!!")
          return redirect('home')
      else:
          messages.success(request,'Error loggin in!!')
          return redirect('home')
    else:
        return render(request, 'home.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "Successful Log out!!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successful Registered!!")
            return redirect('home')
    else:
        form = SignUpForm
        context = {'form':form}
        return render(request, 'register.html', context)
    return render(request, 'register.html', context)
