from django.shortcuts import render, redirect
from .forms import SignupForm, CustomerModelForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Customer
from django.contrib.auth.decorators import login_required

def signup(request):
    form= SignupForm()
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    context = {
        'form' : form
    }
    return render(request, 'app/customerregistration.html', context)
        


def signin(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username/password...Try again!!!')
    return render(request, 'app/login.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def profilePage(request):
    form= CustomerModelForm()
    if request.method == 'POST':
        form= CustomerModelForm(request.POST)
        if form.is_valid():
            user= request.user
            Full_name= form.cleaned_data['Full_name']
            locality= form.cleaned_data['locality']
            city= form.cleaned_data['city']
            state= form.cleaned_data['state']
            zipcode= form.cleaned_data['zipcode']
            phone= form.cleaned_data['phone']
            c= Customer(user=user, Full_name=Full_name, locality=locality, city=city, 
                       state=state,  zipcode=zipcode, phone=phone)
            c.save()
            return redirect('address')
        else:
            messages.error(request, 'Error detected...Try Again!!!')
    context= {
        'form' : form,
         'active' : 'btn btn-primary'
    }
    return render(request, 'app/profile.html', context)

@login_required(login_url='signin')
def address(request):
    address_instance= Customer.objects.filter(user= request.user)
    context = {
        'address_instance' : address_instance,
        'active' : 'btn btn-primary'
    }
    return render(request, 'app/address.html', context)


