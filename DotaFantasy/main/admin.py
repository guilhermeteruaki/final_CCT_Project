from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission

admin.site.register(Main)
admin.site.register(Permission)
# Register your models here.
