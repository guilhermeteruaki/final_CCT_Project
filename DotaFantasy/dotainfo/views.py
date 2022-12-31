from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from main.models import Main
from main.views import *
from django.contrib.auth.models import User, Group, Permission
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import textwrap
import pycountry


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




#update database with API requests

#def update_players():

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

#def update_leagues():


#def update_league_games():


#def  




