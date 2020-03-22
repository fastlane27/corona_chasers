import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as user_req
from urllib.request import urlopen
from .models import Global, Country, Province
import json
import os.path

# S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
# BUCKET = 'coronachaser'
# SESSION = boto3.Session(profile_name='coronachaser')

def create_models():
    # URL That I am scraping
    my_url = "https://coronavirus.m.pipedream.net/"

    # Saves the HTML
    user_client = user_req(my_url)
    page_html = user_client.read()
    user_client.close()

    # Turns HTML into an object/class
    page_soup = soup(page_html, "html.parser")

    # Parses data into Json
    page_dict = json.loads(page_soup.get_text())

    # Sets the values of the global stats
    global_object = Global(
        name='Earth',
        infected=page_dict['summaryStats']['global']['confirmed'],
        recovered=page_dict['summaryStats']['global']['recovered'],
        deaths=page_dict['summaryStats']['global']['deaths'],
        )
    global_object.save()

create_models()

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
