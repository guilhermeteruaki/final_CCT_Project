from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from .models import *
from main.models import Main
from main.views import *
from dotainfo.views import *

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

        if len(UsersTeam.objects.filter(user_team_name=user_team_name))==0: 
            userteam = UsersTeam(user=user, league=league, user_team_name=user_team_name )
            userteam.save()
        else:
            error = "Name already in use"
            return render(request, 'back/error.html' , {'error':error})

        return redirect(list_user_team, userteam.user_team_id)

    return render(request, 'back/user_create_team.html', {"site":site, "league":league})


def list_user_team(request, tid):



    return




