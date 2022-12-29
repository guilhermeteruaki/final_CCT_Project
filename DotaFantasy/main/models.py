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

