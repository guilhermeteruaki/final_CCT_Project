from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$userpage/$', views.userinfo, name='userinfo'),
    
    
]