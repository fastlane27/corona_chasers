from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from .scraper import create_models

create_models()

def home(request):
    return render(request, 'home.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = RegistrationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
