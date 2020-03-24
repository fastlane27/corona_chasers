from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, CommentForm
from .models import Comment, Country, Global, Province, Profile
from .scraper import pop_database


# pop_database()


def home(request):
    world = Global.objects.first()
    return render(request, 'home.html', {'world': world})


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

@login_required
def add_comment(request, country_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.posted_at = datetime.now()
        new_comment.created_by = request.user
        new_comment.country_id = country_id
        new_comment.save()
    return redirect('countries_detail', pk=country_id)

@login_required
def delete_comment(request, country_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user.id == comment.created_by.id:
        comment.delete()
    return redirect('countries_detail', pk=country_id)

@login_required
def update_comment(request, country_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user.id == comment.created_by.id:
        comment.content = request.POST['content']
        comment.save()
    return redirect('countries_detail', pk=country_id)


def profiles_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html', {'profile_user': user})


def update_avatar(request, user_id):
    avatar = Profile.objects.get(user_id=request.user.id).avatar
    print(avatar)
    return redirect('profiles_detail', user_id=user_id)


def assoc_country(request, country_id):
    country = Country.objects.get(id=country_id)
    country.related_user.add(request.user.id)
    return redirect('countries_detail', pk=country_id)


def unassoc_country(request, country_id):
    country = Country.objects.get(id=country_id)
    country.related_user.remove(request.user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



class ProfileList(ListView):
    model = User
    template_name = 'main_app/profile_list.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return User.objects.filter(username__icontains=query)
        else:
            return User.objects.all()

class CountryList(ListView):
    model = Country

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Country.objects.filter(name__icontains=query)
        else:
            return Country.objects.all()

class CountryDetail(DetailView):
    model = Country

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class ProvinceList(ListView):
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Province.objects.filter(country=self.kwargs['pk'], name__icontains=query)
        else:
            return Province.objects.filter(country=self.kwargs['pk'])
