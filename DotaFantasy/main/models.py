from __future__ import unicode_literals
from django.db import models



# Models are the connections to the database.

class Main(models.Model):

    name = models.CharField(max_length=30)
    about = models.TextField(default="-")    
    fb = models.CharField(default="-",max_length=30)
    tw = models.CharField(default="-",max_length=30)
    yt = models.CharField(default="-",max_length=30)
    tell = models.CharField(default="-",max_length=30)
    link = models.CharField(default="-",max_length=30)
    favpicname = models.TextField(default="")
    favpicurl = models.TextField(default="")
    
    def __str__ (self):
        return (self.name + "|" + str(self.pk))

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    birth_day = models.DateField()

    def __str__ (self):
        return (self.first_name + self.last_name + "|" + str(self.pk))