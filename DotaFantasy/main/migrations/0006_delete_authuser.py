# Generated by Django 4.1.4 on 2022-12-29 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_main_favpicname_main_favpicurl'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]
