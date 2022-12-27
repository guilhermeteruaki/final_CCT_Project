from django.shortcuts import render, get_object_or_404, redirect
from .models import Main, AuthUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

#views are how the site behaves


# Front methods.

def home(request):
    site = Main.objects.get(pk=3)
    
    return render(request, 'front/home.html', {'site':site})

def about(request):
    site = Main.objects.get(pk=3)
    return render(request, 'front/about.html',  {'site':site})




#back methods


def panel(request):
    #login check
    if not request.user.is_authenticated :
        return redirect(sign_in)
    #end login        
    site = Main.objects.get(pk=3)
    user = AuthUser.objects.filter()
    return render(request, 'back/controlPanel.html', {'site':site, 'user':user})

def sign_in(request):
    if request.method =="POST":
        uuser = request.POST.get('username')
        upass = request.POST.get('password')
        
        if uuser =="" or upass=="":
            messages.warning(request, "Please porvide a username and a Password!")

        if uuser !="" and upass !="":
            user =authenticate(username=uuser, password=upass)

            if user != None:
                login(request, user)
                return redirect(panel)
            else:
                messages.warning(request, "Username or password not match!")        

    site = Main.objects.get(pk=3)
    return render(request, 'back/sign-in.html',  {'site':site})

def sign_out(request):
    logout(request)
    return redirect(home)

def sign_up(request):

    site = Main.objects.get(pk=3)
    return render(request, 'back/sign-up.html',  {'site':site})        

def site_settings(request):

    #login check
    if not request.user.is_authenticated :
        return redirect(sign_in)
    #end login        

    site = Main.objects.get(pk=3)

    if request.method =="POST":
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        yt  = request.POST.get('yt')
        tw = request.POST.get('tw')
        about = request.POST.get('about')

        if fb == "" : fb = "#"
        if tw == "" : tw = "#"
        if yt == "" : yt = "#"
        if name == "":
            error = "All Fields Requirded: Name"
            return  messages.warning(request, error) 

        try : 

            myFile = request.FILES['myFile']
            fs = FileSystemStorage()
            filename = fs.save(myFile.name, myFile)
            url = fs.url(filename)

            favpicurl = url
            favpicname = filename

        except :

            favpicurl = "-"
            favpicname = "-"



    
        b = Main.objects.get(pk=3)
        b.name = name
        b.tell = tell
        b.fb = fb
        b.tw = tw
        b.yt = yt
        b.about = about
        
        if favpicurl != "-" : b.favpicurl = favpicurl
        if favpicname != "-" : b.favpicname = favpicname
        
        
        b.save()
        return redirect(panel)





    return render(request, 'back/site_settings.html', {'site':site})
