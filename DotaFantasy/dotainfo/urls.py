from django.urls import re_path
from . import views

urlpatterns = [
  re_path(r'^panel/players_list/$', views.players_list, name='players_list'),
  re_path(r'^panel/players_list/players_details/(?P<pk>.\d+)/$', views.players_details, name='players_details'),
  re_path(r'^panel/updatedb/$', views.updatedb, name='updatedb'),
  re_path(r'^panel/league_lists/$', views.league_lists, name='league_lists'),
  re_path(r'^panel/league_lists/league_details/(?P<pk>.\d+)/$', views.league_details, name='league_details'),




]