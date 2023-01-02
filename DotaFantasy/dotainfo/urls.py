from django.urls import re_path
from . import views

urlpatterns = [
  re_path(r'^panel/players_list/$', views.players_list, name='players_list'),
  re_path(r'^panel/players_list/players_details/(?P<pk>\d+)/$', views.players_details, name='players_details'),
  re_path(r'^panel/updatedb/$', views.updatedb, name='updatedb'),
  re_path(r'^panel/league_lists/$', views.league_lists, name='league_lists'),
  re_path(r'^panel/league_lists/league_details/(?P<pk>\d+)/$', views.league_details, name='league_details'),
  re_path(r'^panel/active_league_list/$', views.active_league_list, name='active_league_list'),
  re_path(r'^panel/activate_league/(?P<lid>\d+)/$', views.activate_league, name='activate_league'),

]