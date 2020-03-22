import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'coronachaser'
SESSION = boto3.Session(profile_name='coronachaser')

def profile(request):
    return render(request, 'profile.html')

def country_index(request):
    return render(request, 'countries/index.html')

def country(request):
    return render(request, 'countries/country.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = RegistrationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
