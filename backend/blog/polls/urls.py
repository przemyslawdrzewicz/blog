from django.urls import path
from polls import views
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.index, name='index'),
    path('polls/add_article/', views.add_article),
    path('polls/get_articles/', views.get_articles),
    path('polls/update_article/', views.update_article),
    path('polls/delete_article/', views.delete_article),
    path('polls/register/', views.register),
    path('polls/login/', views.login),
     path('polls/change_image/', views.change_image),
     path('polls/get_url/', views.get_url),
]

urlpatterns = format_suffix_patterns(urlpatterns)