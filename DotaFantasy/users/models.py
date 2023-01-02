from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserInfo(models.Model):
    id = models.OneToOneField(User, on_delete=models.DO_NOTHING,db_column='id', primary_key=True)
    birth_day = models.DateField()
    midle_name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.id.pk)
    
class UsersTeamPlayers(models.Model):
    team = models.ForeignKey('UsersTeam', models.DO_NOTHING)
    league = models.OneToOneField('dotainfo.LeagueDetails', models.DO_NOTHING, primary_key=True)
    player_1 = models.IntegerField(db_column='player 1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    player_2 = models.IntegerField(db_column='player 2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    player_3 = models.IntegerField(db_column='player 3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    player_4 = models.IntegerField(db_column='player 4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    player_5 = models.IntegerField(db_column='player 5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    player_6 = models.IntegerField(db_column='player 6', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'users_team_players'
        unique_together = (('league', 'team'),)

class UsersTeam(models.Model):
    user_team_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    league = models.ForeignKey('dotainfo.LeagueDetails', models.DO_NOTHING)
    user_team_name = models.CharField(max_length=45)
    team_score = models.IntegerField(default=0)
    
    class Meta:
        managed = False
        db_table = 'users_team'





