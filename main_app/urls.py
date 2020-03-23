from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('accounts/signup/', views.signup, name='signup'),
     path('countries/', views.CountryList.as_view(), name='countries_index'),
     path('countries/<int:pk>/',
         views.CountryDetail.as_view(), name='countries_detail'),
     path('countries/<int:country_id>/add_comment/', views.add_comment, name='add_comment'),
     path('countries/<int:country_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
     path('countries/<int:country_id>/update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
#     path('countries/<int:country_id>/comments/create/',
#          views.CommentCreate.as_view(), name='comments_create'),
#     path('countries/<int:country_id>/comments/<int:pk>/update/',
#          views.CommentUpdate.as_view(), name='comments_update'),
#     path('countries/<int:country_id>/comments/<int:pk>/delete/',
#          views.CommentDelete.as_view(), name='comments_delete'),
     path('countries/<int:pk>/provinces/', views.ProvinceList.as_view(), name='provinces_index'),
     path('profiles/', views.profiles_detail, name='profiles_detail'),
#     path('profiles/<int:profile_id>/assoc_country/<int:country_id>/',
#          views.assoc_country, name='assoc_country'),
#     path('profiles/<int:profile_id>/unassoc_country/<int:country_id>/',
#          views.unassoc_country, name='unassoc_country'),
]
