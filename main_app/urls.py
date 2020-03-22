from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('countries/index/', views.country_index, name='index'),
    path('countries/country/', views.country, name='country'),
    path('profile/', views.profile, name='profile'),
]
