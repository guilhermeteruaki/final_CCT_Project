from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from main.models import Main
from main.views import *
from django.contrib.auth.models import User, Group, Permission
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import requests
import textwrap
import pycountry
import time


# Create your views here.
def connect_to_API(info):

    DotaAPI = 'https://api.opendota.com/api/'
 
    return requests.get(DotaAPI+info).json()

def players_list(request):
    # login and permission check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    accesslvl =1
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
    # login check end
    site = Main.objects.get(pk=3)

    result = Players.objects.all()
    paginator = Paginator(result, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except EmptyPage: 
        response = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        response = paginator.page(1)


    return render(request, 'back/players_list.html',  {"site":site,"response":response})

def players_details(request, pk):
    # login check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    # login check end
    accesslvl =1
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
        

    site = Main.objects.get(pk=3)
    players = Players.objects.filter(player_id=pk)
   
    for u in players:
        pk = u.player_id
        player_personaname = u.player_personaname
        steam_id = u.steam_id
        player_role = u.player_role
        team_id = u.team_id
        if u.player_nationality :
            player_nationality = pycountry.countries.get(alpha_2=u.player_nationality).name
        else: player_nationality="-"
        playerinfo={"pk":pk, "player_personaname":player_personaname, "steam_id":steam_id, "player_role":player_role,
                    "team_id":team_id, "player_nationality":player_nationality}
        
    return render(request, 'back/players_details.html',  {"site":site,"playerinfo":playerinfo})
    
def league_lists(request):
    # login and permission check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    accesslvl =1
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
    # login check end

    site = Main.objects.get(pk=3)

    result = LeagueDetails.objects.all().order_by('league_id')
    
    paginator = Paginator(result, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except EmptyPage: 
        response = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        response = paginator.page(1)

    return render(request, 'back/league_lists.html',  {"site":site,"response":response})

def league_details(request,pk):
    
    # login check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    # login check end
    accesslvl =1
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
        
    
    site = Main.objects.get(pk=3)
    leagues = LeagueDetails.objects.filter(league_id=pk)

    for u in leagues:
        pk = u.league_id
        league_name = u.league_name
        start_date = u.start_date
        is_finished = u.is_finished
        participants = u.participants
        tier = u.tier
        is_active = u.is_active


        response={"pk":pk, "league_name":league_name, "start_date":start_date, "is_finished":is_finished,
                    "participants":participants, "tier":tier, "is_active":is_active}
        
    return render(request, 'back/league_details.html',  {"site":site,"response":response})

def activate_league(request, lid):
    # login and permission check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    accesslvl =1
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
    # login check end

    league = LeagueDetails.objects.get(league_id=lid)
    if league.is_active==1:
        error = "This league is already active"
        return render(request, 'back/error.html' , {'error':error})
    else:
        league.is_active=1
        league.save()
    return redirect(active_league_list)
    
    
def active_league_list(request):
    # login and permission check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    accesslvl =2
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
    # login check end
    site = Main.objects.get(pk=3)


    league = LeagueDetails.objects.filter(is_active=1).order_by('league_id')
    paginator = Paginator(league, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except EmptyPage: 
        response = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        response = paginator.page(1)


    return render(request, 'back/active_league_list.html',  {"site":site,"response":response})
    
#update database with API requests
def updatedb(request):

    if not request.user.is_authenticated :
        return redirect(sign_in)
    accesslvl =1
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
    # login check end
   
    count = 1
    id =[14268]
    for j in id:
        league = LeagueGames.objects.filter(league=j)
        update_league_games(j)
        print (j)
        for i in league :
            result = update_player_results(i.game_id)
            # reduce frequency of calls so not to reach the API limit of 60 calls per minute
            
            time.sleep(1.15)
            
            print(count)
            count +=1
    return render(request, 'back/test.html' ,  {"result":result})

def update_players():

    response = connect_to_API("proPlayers")

    for p in response:
        player_id=p.get('account_id')
        player_personaname= textwrap.shorten(p.get('personaname'), width=44, placeholder='~')
        player_nationality=p.get('country_code')
        steam_id=p.get('steamid')
        player_role=p.get('fantasy_role')
        team_id=p.get('team_id')

        
        b = Players(player_id=player_id, player_personaname=player_personaname, 
                                player_nationality=player_nationality, steam_id=steam_id, player_role=player_role,
                                team_id=team_id)
        b.save()
                  

    return Players.objects.all()

def update_leagues():

    response = connect_to_API("leagues")

    for p in response:
        league_id=p.get('leagueid')
        league_name=p.get('name')
        is_finished=0
        tier = p.get('tier')

        if (tier=="professional" or tier =="premium"):
            b = LeagueDetails(league_id=league_id, league_name=league_name, is_finished=is_finished,
                            tier=tier)
            b.save()
    return LeagueDetails.objects.all()

def update_league_participants(leagueID):

    response = connect_to_API("leagues/" +str(leagueID)+"/teams")
    
    teams=[]
    
    for i in response:
        teams.append(i.get('team_id'))
    
    b = LeagueDetails.objects.get(league_id=leagueID)
    b.participants = teams
    b.save()
    return LeagueDetails.objects.get(league_id=leagueID)

def update_league_games(leagueID):

    response = connect_to_API("leagues/" +str(leagueID)+"/matches")
    
    for i in response:
        if leagueID==i.get('leagueid'):

            game_id = i.get('match_id')
            league = LeagueDetails.objects.get(pk=leagueID)
            radiant_win = i.get('radiant_win')
            radiant_team = i.get('radiant_team_id')
            dire_team = i.get('dire_team_id')
            game_duration =i.get('duration')
        else: print ('leaguid no match')
    
        b = LeagueGames(game_id=game_id, league=league, radiant_win=radiant_win, radiant_team=radiant_team,
                     dire_team=dire_team,game_duration=game_duration)
        b.save()

   
    return LeagueGames.objects.all()

def update_player_results(gameID):
    #multipliers
    m = {"kills":5, "deaths":-2, "assists":3, "lasthit": 0.2, "gpm":2, "xpm":2}
    response = connect_to_API("matches/"+str(gameID))
    
    for i in response.get('players'):
        
        player = Players.objects.get(pk=i.get('account_id'))
        game = LeagueGames.objects.get(pk=gameID)
        kills = i.get('kills')
        deaths = i.get('deaths')
        assists = i.get('assists')
        last_hits = i.get('last_hits')
        gold_per_minute = i.get('gold_per_min')
        xp_per_minute = i.get('xp_per_min')
        score = (kills*m.get('kills')+deaths*m.get('deaths')+assists*m.get('assists')+
                    last_hits*m.get('lasthit')+gold_per_minute*m.get('gpm')+xp_per_minute*m.get('xpm'))
                    

         #Q operator https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query
        if PlayerResults.objects.filter(Q(player=player) & Q(game=game)).exists():
            q = PlayerResults.objects.filter(Q(player=player) & Q(game=game))
            
            for b in q: 
                
                b.kills=kills
                b.deaths=deaths
                b.xp_per_minute=xp_per_minute
                b.assists=assists
                b.last_hits=last_hits
                b.gold_per_minute=gold_per_minute
                b.save() 
            S = PlayerScore.objects.filter(Q(player=player.player_id) & Q(league=game.league))
            for s in S:
                s.score += score
                s.save()
            

        else:
                      
            b = PlayerResults(player=player, game=game, kills=kills, deaths=deaths, xp_per_minute=xp_per_minute,
                        assists=assists,last_hits=last_hits, gold_per_minute=gold_per_minute)
            b.save()
            S = PlayerScore(player=player, league = game.league, score = score)
            S.save()
            
                   

   
    return LeagueGames.objects.all()





