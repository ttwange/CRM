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

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up records
        customer_record = Record.objects.get(id=pk)
    else:
        messages.success(request, "Log in to view page!")
        return redirect('home')
    
    context = {'customer_record':customer_record}
    return render(request, 'record.html', context)

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Dleted!")
        return redirect('home')
    else:
        messages.success(request, "Log in to view page!")
        return redirect('home')
        
def add_record(request):
    form = AddRecordForm(request.POST or None)
    context = {'form':form}
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added")
                return redirect('home')
        return render(request, 'add_record.html', context)
    else:
        messages.success(request, "you must log in")
        return redirect('home')
    
    return render(request, 'add_record.html', context)