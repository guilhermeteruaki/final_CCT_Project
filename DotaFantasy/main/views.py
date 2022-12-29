from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

#views are how the site behaves



def home(request):
    site = Main.objects.get(pk=3)
    
    return render(request, 'front/home.html', {'site':site})

def about(request):
    site = Main.objects.get(pk=3)
    return render(request, 'front/about.html',  {'site':site})

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

def site_settings(request):

    #login check
    if not request.user.is_authenticated :
        return redirect(sign_in)
    #end login        

    site = Main.objects.get(pk=3)

    if request.method =="POST":
        b = Main.objects.get(pk=3)
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        yt  = request.POST.get('yt')
        tw = request.POST.get('tw')
        about = request.POST.get('about')

        if fb == "" : fb = "#"
        if tw == "" : tw = "#"
        if yt == "" : yt = "#"
        if name == "" or name== None or name == " ":
            error = "All of the following fields are Requirded: Name"
            return  render(request, 'back/error.html', {'site':site, 'error':error}) 

        try : 

            myFile = request.FILES['myFile']
            fs = FileSystemStorage()
            filename = fs.save(myFile.name, myFile)
            url = fs.url(filename)

            if str(myFile.content_type).startswith("image"):

                favpicurl = url
                favpicname = filename
            else:
                error = "Your file is not supported!"
                return  render(request, 'back/error.html', {'site':site, 'error':error})

        except :

            favpicurl = "-"
            favpicname = "-"



    
        
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

def change_pass(request):

    # login check start
    if not request.user.is_authenticated :
        return redirect(sign_in)
    # login check end

    if request.method == 'POST' :

        oldPass = request.POST.get('oldPass')
        newPass = request.POST.get('newPass')
        newPass2 = request.POST.get('newPass2')
        if oldPass == "" or newPass == "" or newPass2=="":
            error = "All Fields Requirded"
            return render(request, 'back/error.html' , {'error':error})

        user = authenticate(username=request.user, password=oldPass)

        if user != None :

            if len(newPass) < 8 :
                error = "Your Password Must Be At Less 8 Character"
                return render(request, 'back/error.html' , {'error':error})

            count1 = 0
            count2 = 0
            count3 = 0 
            count4 = 0

            for i in newPass :
                

                if i.isdigit():
                    count1 = 1
                if i.isupper():
                    count2 = 1
                if i.islower():
                    count3 = 1
                if i in "!@#$%^&*()-+?_=,<>/" :
                    count4 = 1
                 
            if count1 != 1:      
                error = "Passwords must contain numbers"
                return render(request, 'back/error.html' , {'error':error})
            if count2 != 1:      
                error = "Passwords must contain Capital Letters"
                return render(request, 'back/error.html' , {'error':error})
            if count3 != 1:      
                error = "Passwords must contain lowercase letters"
                return render(request, 'back/error.html' , {'error':error})
            if count4 != 1:      
                error = "Passwords must contain special characters"
                return render(request, 'back/error.html' , {'error':error})

            if newPass != newPass2:
                error = "Passwords didn't match"
                return render(request, 'back/error.html' , {'error':error})

                
            if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 :

                user = User.objects.get(username=request.user)
                user.set_password(newPass)
                user.save()
                return redirect(sign_out)

        else:

            error = "Your Password Is Not Correct"
            return render(request, 'back/error.html' , {'error':error})


    return render(request, 'back/change_pass.html')

def sign_up(request):
    
    if request.method == 'POST':

        fname = request.POST.get('firstName')
        lname = request.POST.get('lastName')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        bday = request.POST.get('bday')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print (fname, lname,uname, email,bday, password, password2)
        if fname == "" or lname == "":
            error = "Input Your Name"
            return render(request, 'back/error.html' , {'error':error})
        
           
        
        if password != password2 :
            error = "Your Pass Didn't Match"
            return render(request, 'back/error.html' , {'error':error})

        if len(password) < 8 :
                error = "Your Password Must Be At Less 8 Character"
                return render(request, 'back/error.html' , {'error':error})

        count1 = 0
        count2 = 0
        count3 = 0 
        count4 = 0

        for i in password :
            

            if i.isdigit():
                count1 = 1
            if i.isupper():
                count2 = 1
            if i.islower():
                count3 = 1
            if i in "!@#$%^&*()-+?_=,<>/" :
                count4 = 1
                
        if count1 != 1:      
            error = "Passwords must contain numbers"
            return render(request, 'back/error.html' , {'error':error})
        if count2 != 1:      
            error = "Passwords must contain Capital Letters"
            return render(request, 'back/error.html' , {'error':error})
        if count3 != 1:      
            error = "Passwords must contain lowercase letters"
            return render(request, 'back/error.html' , {'error':error})
        if count4 != 1:      
            error = "Passwords must contain special characters"
            return render(request, 'back/error.html' , {'error':error})

        if count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1 and len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0 :
            user = User.objects.create_user(username=uname,email=email,password=password)
            


    return render(request, 'back/sign-up.html')



def termsandcond(request):
    site = Main.objects.get(pk=3)
    msg = "By accepting these terms and conditions you agree to: If you are a teacher or evaluator from CCT to give Guilherme an A+ in this assignment."
    return render(request, 'front/termsandcond.html',  {'site':site, 'msg':msg})