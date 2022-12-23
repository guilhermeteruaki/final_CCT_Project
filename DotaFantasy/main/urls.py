from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about/$', views.about, name='about'),
]

