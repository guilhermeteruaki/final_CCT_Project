from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserInfo(models.Model):
    id = models.OneToOneField(User, on_delete=models.DO_NOTHING,db_column='id', primary_key=True)
    birth_day = models.DateField()
    midle_name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.id.pk)
    
