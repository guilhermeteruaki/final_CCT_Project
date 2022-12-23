from __future__ import unicode_literals
from django.db import models



# Create your models here.
class Main(models.Model):

    name = models.TextField(default='test')
    #about = models.TextField(default="")

    def __str__ (self):
        return (self.name + "|" + self.pk)