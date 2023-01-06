from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from django.template import Library, Node
from .models import *
from main.models import Main
from main.views import *
from dotainfo.views import *
from datetime import date


def all_user_info(pk):

    users = UserInfo.objects.filter(pk=pk)
    for u in users:
        
        pk = u.id.pk
        fname = u.id.first_name
        lname = u.id.last_name
        mname = u.midle_name
        email = u.id.email
        bday = u.birth_day
        uname = u.id.username
        group = u.id.groups.all()

        userinfo={"pk":pk, "bday":bday, "fname":fname, "lname":lname, "mname":mname, "email":email, "uname":uname, "group":group}

    return userinfo

def users_list(request):
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
    users = UserInfo.objects.all()
    ulist = []
    for u in users:
        
        pk = u.id.pk
        fname = u.id.first_name
        lname = u.id.last_name
        mname = u.midle_name
        email = u.id.email
        bday = u.birth_day
        uname = u.id.username
        ugroup = u.id.groups.all()

        userinfo={"pk":pk, "fname":fname, "lname":lname, "mname":mname, "email":email,"bday":bday, "uname":uname, "ugroup":ugroup}
        ulist.append(userinfo)
        
    return render(request, 'back/users_list.html',  {"site":site, 'ulist':ulist})

def delete_user(request,pk):
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
        

    email = UserInfo.objects.get(pk=pk).id.email
    b = User.objects.filter(email=email)
    UserInfo.objects.get(pk=pk).delete()
    b.delete()
    
    return redirect(users_list)

def users_groups(request):
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

    group = Group.objects.all().exclude(name="masteruser")

    return render(request, 'back/users_groups.html', {"site":site, "group":group})

def new_group(request):
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
        


    if request.method=="POST":
        gname = request.POST.get('group-name')

        if gname != "":
            if len(Group.objects.filter(name=gname)) == 0:

                g = Group(name=gname)
                g.save()
            else:
                error = "This name already exists"
                return render(request, 'back/error.html' , {'error':error})

    return redirect(users_groups)

def delete_group(request, name):
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
        

    b = Group.objects.filter(name=name).exclude(name="masteruser")
    b.delete()
    
    return redirect(users_groups)

def user_details(request,pk):
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
    userinfo=all_user_info(pk=pk)

      
        
   
   
    return render(request, 'back/user_details.html', {"site":site, 'userinfo':userinfo})

def edit_user(request,pk):
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
    

    
    userIn = UserInfo.objects.filter(pk=pk)

    for u in userIn:
        
        pk = u.id.pk
        fname = u.id.first_name
        lname = u.id.last_name
        mname = u.midle_name
        email = u.id.email
        bday = u.birth_day
        uname = u.id.username
        ugroup = u.id.groups.all()
        group = Group.objects.all().exclude(name="masteruser")

        userinfo={"pk":pk, "bday":bday, "fname":fname, "lname":lname, "mname":mname, "email":email, "uname":uname,"ugroup":ugroup, "group":group}

    
    u = User.objects.get(pk=pk)
    uinfo = UserInfo.objects.get(pk=pk)

    if request.method == 'POST':
    
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        bday = request.POST.get('bday')
        gname = request.POST.get("group")


        
        if fname == "" or lname == "" or bday == "" or uname == "" or email == "" :
            error = "All Fields Requirded"
            return render(request, 'back/error.html' , {'error':error})

        
        group = Group.objects.get(name=gname)
        u.first_name = fname
        u.last_name = lname
        if mname != "": uinfo.midle_name = mname
        else: uinfo.midle_name = "-"
        u.username = uname
        u.email = email
        uinfo.birth_day = bday
        u.groups.add(group)
        u.save()
        uinfo.save()

        return redirect(user_details, pk)

    return render(request, 'back/edit_user.html', {"site":site, "userinfo":userinfo})

def group_members(request, name):
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
    ulist =[]

    for u in User.objects.all().exclude(pk=1):
        print (u.groups.all())
        if u.groups.filter(name=name).exists():
            ulist.append({"pk":u.pk,"uname":u.username} )
            print(ulist)



    return render(request, 'back/group_members.html', {"site":site, "name":name, "ulist":ulist})

def remove_user_from_group(request, pk, gname):
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
        
        
    group = Group.objects.get(name=gname)
    user = User.objects.get(pk=pk)
    user.groups.remove(group)
    
    return redirect(user_details, pk)    

def profile_page(request):
    
    # login check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    # login check end
    accesslvl =2
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
        

    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
        

    site = Main.objects.get(pk=3)
    pk = request.user.pk
    if pk==1: redirect(panel)
    user = all_user_info(pk=pk)



    

    return render(request, 'back/profile_page.html', {"site":site, "user":user})

def create_user_team(request, lid, uid):
    # login check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    # login check end
    accesslvl =2
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
        
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})

    site = Main.objects.get(pk=3)
    
    user = User.objects.get(pk=uid)
    league = LeagueDetails.objects.get(league_id=lid)

    if request.method == 'POST':
    
        user_team_name = request.POST.get('user_team_name')
        
        if user_team_name == "" :
            error = "All Fields Requirded"
            return render(request, 'back/error.html' , {'error':error})

        if len(UsersTeam.objects.filter(user=user))!=0 and len(UsersTeam.objects.filter(league=league))!=0: 
            error = "You already have a team in this league"
            return render(request, 'back/error.html' , {'error':error})
        else:
            userteam = UsersTeam(user=user, league=league, user_team_name=user_team_name )
            userteam.save()
            TP =UsersTeamPlayers(team=userteam, league=league)
            TP.save()
           

        return redirect(list_user_teams)

    return render(request, 'back/user_create_team.html', {"site":site, "league":league})

def list_all_user_teams(request):
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

    result = UsersTeam.objects.all().order_by('user_team_id')
    
    paginator = Paginator(result, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except EmptyPage: 
        response = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        response = paginator.page(1)

    return render(request, 'back/list_all_user_teams.html',  {"site":site,"response":response})
 
def delete_user_team(request, pk):
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
        

    team = UsersTeam.objects.get(pk=pk)
    print(team)
    team.delete()
    
    
    return redirect(list_all_user_teams)

def list_user_teams(request):
    # login check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    # login check end
    accesslvl =2
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
        
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})

    site = Main.objects.get(pk=3)

    result = UsersTeam.objects.filter(user=request.user).order_by('league')
    
    paginator = Paginator(result, 10)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except EmptyPage: 
        response = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        response = paginator.page(1)

    return render(request, 'back/list_user_teams.html',  {"site":site,"response":response})
 
def team_details(request,pk):
    # login check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    # login check end
    accesslvl =2
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
        

    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})
        

    site = Main.objects.get(pk=3)
    userteam=UsersTeam.objects.get(user_team_id=pk)
    teamP = UsersTeamPlayers.objects.get(team=userteam)
    score = 0
    teamplayers = {
        "player_1": Players.objects.get(player_id = teamP.player_1) ,
        "player_2":Players.objects.get(player_id = teamP.player_2) ,
        "player_3":Players.objects.get(player_id=teamP.player_3) ,
        "player_4":Players.objects.get(player_id=teamP.player_4) ,
        "player_5":Players.objects.get(player_id=teamP.player_5) ,
        "player_6":Players.objects.get(player_id=teamP.player_6) }
    
    for p in range(1,6):
        PS = PlayerScore.objects.filter(Q(player=teamplayers.get('player_'+str(p))) & Q(league=userteam.league))
        for s in PS:
            score += s.score
    
    userteam.team_score = score
    userteam.save()
    partiID = LeagueDetails.objects.get(league_id=userteam.league.league_id).participants
    all_players_of_league = []
    for i in partiID:
        playes_of_team = Players.objects.filter(team_id=i)
        for p in playes_of_team:
            all_players_of_league.append({"playerid":p.player_id, "playerrole": p.player_role, "playerusername":p.player_personaname,
                                            "playerteam":i})
        
    
    return render(request, 'back/team_details.html', {"site":site,"all_players_of_league":all_players_of_league, "teamplayers":teamplayers, 'userteam':userteam})

def edit_user_team(request, pk):
    # login check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    # login check end
    accesslvl =2
    perm = 10
    for i in request.user.groups.all():
        if i.name == "user":perm = 2
        if i.name == "admin":perm = 1
    if perm>accesslvl: 
        error = "Acess denied! Log-in with the correct account"
        return render(request, 'back/error.html' , {'error':error})

    site = Main.objects.get(pk=3)
    # mon =0 tue=1 wed=2 thur=3 fri=4 sat=5 sun=6
    today = date.weekday(date.today())
    
    if today == 0 or today == 2 or today == 4:
        

        u = UsersTeam.objects.get(user_team_id=pk)
        partiID = LeagueDetails.objects.get(league_id=u.league.league_id).participants
        all_players_of_league = []
        for i in partiID:
            playes_of_team = Players.objects.filter(team_id=i)
            for p in playes_of_team:
                all_players_of_league.append({"playerid":p.player_id, "playerrole": p.player_role, "playerusername":p.player_personaname,
                                                "playerteam":i})

        teamP = UsersTeamPlayers.objects.get(team=u)
        
        teamplayers = {
            "player_1": Players.objects.get(player_id = teamP.player_1) ,
            "player_2":Players.objects.get(player_id = teamP.player_2) ,
            "player_3":Players.objects.get(player_id=teamP.player_3) ,
            "player_4":Players.objects.get(player_id=teamP.player_4) ,
            "player_5":Players.objects.get(player_id=teamP.player_5) ,
            "player_6":Players.objects.get(player_id=teamP.player_6) }

        if request.method == 'POST':
        
            player_1 = request.POST.get('player_1')
            player_2 = request.POST.get('player_2')
            player_3 = request.POST.get('player_3')
            player_4 = request.POST.get('player_4')
            player_5 = request.POST.get('player_5')
            player_6 = request.POST.get('player_6')


            
            
            teamP.player_1 = player_1
            teamP.player_2 = player_2
            teamP.player_3 = player_3
            teamP.player_4 = player_4
            teamP.player_5 = player_5
            teamP.player_6 = player_6
            teamP.save()

            return redirect(team_details, pk)

        return render(request, 'back/edit_user_team.html', {"site":site,"teamplayers":teamplayers, "all_players_of_league":all_players_of_league})
    else:
        error = "Sorry, you can only edit your team on a Monday, Wednesday or Friday"
        return render(request, 'back/error.html' , {'error':error})



    teamP = UsersTeamPlayers.objects.get(team=tid)
    
    multipliers = {"kill":5, "death":-2, "assist":3, "lasthit": 0.2, "gpm":2, "xpm":2}
    games = LeagueGames.objects.filter(league_id=lid)
    p1t=p2t=p3t=p4t=p5t=p6t=0

    
    for g in games:
        print(g)
        
        p1 = PlayerResults.objects.get(player_id=teamP.player_1, game_id=g )


        p1s = (multipliers.get('kill')*p1.kills+multipliers.get('death')*p1.deaths+multipliers.get('assist')*p1.assists+
            multipliers.get('lasthit')*p1.last_hits+multipliers.get('gpm')*p1.gold_per_minute+multipliers.get('xpm')*p1.xp_per_minute)
        p1 = PlayerResults.objects.get(player_id=teamP.player_1, game_id=g )
        p2s = (multipliers.get('kill')*p1.kills+multipliers.get('death')*p1.deaths+multipliers.get('assist')*p1.assists+
            multipliers.get('lasthit')*p1.last_hits+multipliers.get('gpm')*p1.gold_per_minute+multipliers.get('xpm')*p1.xp_per_minute)
        p3s = (multipliers.get('kill')*p1.kills+multipliers.get('death')*p1.deaths+multipliers.get('assist')*p1.assists+
            multipliers.get('lasthit')*p1.last_hits+multipliers.get('gpm')*p1.gold_per_minute+multipliers.get('xpm')*p1.xp_per_minute)
        p4s = (multipliers.get('kill')*p1.kills+multipliers.get('death')*p1.deaths+multipliers.get('assist')*p1.assists+
            multipliers.get('lasthit')*p1.last_hits+multipliers.get('gpm')*p1.gold_per_minute+multipliers.get('xpm')*p1.xp_per_minute)
        p5s = (multipliers.get('kill')*p1.kills+multipliers.get('death')*p1.deaths+multipliers.get('assist')*p1.assists+
            multipliers.get('lasthit')*p1.last_hits+multipliers.get('gpm')*p1.gold_per_minute+multipliers.get('xpm')*p1.xp_per_minute)
        p6s = (multipliers.get('kill')*p1.kills+multipliers.get('death')*p1.deaths+multipliers.get('assist')*p1.assists+
            multipliers.get('lasthit')*p1.last_hits+multipliers.get('gpm')*p1.gold_per_minute+multipliers.get('xpm')*p1.xp_per_minute)
        p1t += p1s
        p2t += p2s
        p3t += p3s
        p4t += p4s
        p5t += p5s
        p6t += p6s
        print("ok")

    print(p1t,p2t,p3t,p4t,p5t,p6t)