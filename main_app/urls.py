from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('countries/', views.countries_index, name='countries_index'),
    path('countries/<int:country_id>/', views.countries_detail, name='countries_detail'),
    path('countries/<int:country_id>/comments/create', views.CommentCreate.as_view(), name='comments_create'),
    path('countries/<int:country_id>/comments/<int:pk>/update', views.CommentUpdate.as_view(), name='comments_update'),
    path('countries/<int:country_id>/comments/<int:pk>/delete', views.CommentDelete.as_view(), name='comments_delete'),
    path('profile/', views.profile_index, name='profile_index'),
    path('profile/assoc_country/<int:country_id>/', views.assoc_country, name='assoc_country'),
    path('profile/unassoc_country/<int:country_id>/', views.unassoc_country, name='unassoc_country'),
]
