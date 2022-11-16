from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login, logout

# Create your views here. 


def RegisterUser(request : HttpRequest):

    if request.method == "POST":
        
        #create new user
        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()
        

        #creating the profile
        user_profile = Profile(user=new_user, gender=request.POST["gender"], university_name=request.POST["university_name"], department=request.POST["department"], level=request.POST["level"])
        user_profile.save()

    return render(request, "accounts/register.html") 





def LoginUser(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("CooperativeTrainingApp:Home")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "accounts/login.html", {"msg" : msg})  

 


def LogoutUser(request: HttpRequest):

    logout(request)

    return render(request, "CooperativeTrainingApp/Home.html")
    