from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Comment, Country


class CommentCreate(CreateView):
    model = Comment
    fields = '__all__'

class CommentUpdate(UpdateView):
  model = Comment
  fields = ['posted_at', 'content']

class CommentDelete(DeleteView):
  model = Comment
  success_url = '/countries/<int:country_id>/'


def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def countries_index(request):
  pass

def countries_detail(request, country_id):
  pass

def profile_index(request):
  pass

def assoc_country(request, profile, countryy_id):
  pass

def unassoc_country(request, profile, country_id):
  pass

class CountryList(ListView):
  model = Country

