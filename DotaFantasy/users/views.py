from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from users import views
from .models import UserInfo

def userinfo(request):
    return render(request, 'middle/userpage.html')