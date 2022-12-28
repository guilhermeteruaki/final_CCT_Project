from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^panel/$', views.panel, name='Control Panel'), 
    re_path(r'^sign-in/', views.sign_in, name='sign-in'), 
    re_path(r'^sign-up/', views.sign_up, name='sign-up'), 
    re_path(r'^sign-out/', views.sign_out, name='sign_out'),
    re_path(r'^panel/site_settings/', views.site_settings, name='site_settings'),
    re_path(r'^panel/change_pass', views.change_pass, name='change_pass'),

]

