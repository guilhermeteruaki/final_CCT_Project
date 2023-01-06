from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^panel/users_list/$', views.users_list, name='users_list'),
    re_path(r'^panel/users_list/del/(?P<pk>\d+)/$', views.delete_user, name='delete_user'),
    re_path(r'^panel/users_groups/$', views.users_groups, name='users_groups'),
    re_path(r'^panel/users_groups/new_group/$', views.new_group, name='new_group'),
    re_path(r'^panel/users_groups/del/(?P<name>.*)/$', views.delete_group, name='delete_group'),
    re_path(r'^panel/users_list/user_details/(?P<pk>\d+)/$', views.user_details, name='user_details'),
    re_path(r'^panel/users_list/edit_user/(?P<pk>\d+)/$', views.edit_user, name='edit_user'),
    re_path(r'^panel/users_groups/group_members/(?P<name>.*)/$', views.group_members, name='group_members'),
    re_path(r'^panel/users_list/remove_user_from_group/(?P<pk>\d+)/(?P<gname>.*)/$', views.remove_user_from_group, name='remove_user_from_group'),
    re_path(r'^panel/profile_page/$', views.profile_page, name='profile_page'),
    re_path(r'^panel/create_team/(?P<lid>\d+)/(?P<uid>\d+)/$', views.create_user_team, name='create_user_team'),
    re_path(r'^panel/all_users_teams/$', views.list_all_user_teams, name='list_all_user_teams'),
    re_path(r'^panel/delete_user_team/(?P<pk>\d+)/$', views.delete_user_team, name='delete_user_team'),
    re_path(r'^panel/list_user_teams/$', views.list_user_teams, name='list_user_teams'),
    re_path(r'^panel/list_user_teams/team_details/(?P<pk>\d+)/$', views.team_details, name='team_details'),
     re_path(r'^panel/list_user_teams/edit_team/(?P<pk>\d+)/$', views.edit_user_team, name='edit_user_team'),
]