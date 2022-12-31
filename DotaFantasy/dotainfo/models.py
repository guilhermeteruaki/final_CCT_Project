from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


    

class Players(models.Model):
    player_id = models.BigIntegerField(primary_key=True)
    player_personaname = models.CharField(max_length=45)
    player_nationality = models.CharField(max_length=45, blank=True, null=True)
    steam_id = models.BigIntegerField(unique=True)
    player_role = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players'

class PlayerResults(models.Model):
    player = models.OneToOneField('Players', models.DO_NOTHING, primary_key=True)
    game = models.ForeignKey('LeagueGames', models.DO_NOTHING)
    kills = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    last_hits = models.IntegerField(blank=True, null=True)
    gold_per_minute = models.IntegerField(blank=True, null=True)
    xp_per_minute = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_results'
        unique_together = (('player', 'game'),)

class LeagueGames(models.Model):
    game_id = models.BigIntegerField(primary_key=True)
    league = models.ForeignKey('LeagueDetails', models.DO_NOTHING)
    radiant_win = models.IntegerField(blank=True, null=True)
    radiant_team = models.IntegerField()
    dire_team = models.IntegerField()
    game_duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'league_games'

class LeagueDetails(models.Model):
    league_id = models.BigIntegerField(primary_key=True)
    league_name = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    is_finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'league_details'






        








