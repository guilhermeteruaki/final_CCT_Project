from django.shortcuts import render, get_object_or_404, redirect
from .models import Main, AuthUser
from django.contrib.auth import authenticate, login, logout

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
    #login
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
        
        if uuser !="" and upass !="":
            user =authenticate(username=uuser, password=upass)

            if user != None:
                login(request, user)
                return redirect(panel)
                

    site = Main.objects.get(pk=3)
    return render(request, 'back/sign-in.html',  {'site':site})

def sign_out(request):
    logout(request)
    return redirect(home)

def sign_up(request):
    site = Main.objects.get(pk=3)
    return render(request, 'back/sign-up.html',  {'site':site})        