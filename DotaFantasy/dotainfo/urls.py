from django.urls import re_path
from . import views

urlpatterns = [
  re_path(r'^panel/players_list/$', views.players_list, name='players_list'),
  re_path(r'^panel/players_list/players_details/(?P<pk>.\d+)/$', views.players_details, name='players_details'),
]