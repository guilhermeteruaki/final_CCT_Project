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
    id = models.BigIntegerField(primary_key=True)
    player = models.ForeignKey('Players', models.DO_NOTHING)
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
        unique_together = (('player', 'game'))

class PlayerScore(models.Model):
    id = models.BigAutoField(primary_key=True)
    player = models.ForeignKey('Players', models.DO_NOTHING, blank=True, null=True)
    league = models.ForeignKey('LeagueDetails', models.DO_NOTHING, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_score'

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
    league_name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    is_finished = models.IntegerField()
    participants = models.JSONField(blank=True, null=True)
    tier = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'league_details'





        








