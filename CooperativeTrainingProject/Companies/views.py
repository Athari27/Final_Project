from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import AddCompany
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here. 



def Company(request : HttpRequest):
    user : User = request.user
    

    if request.method == "POST":
        new_company = AddCompany(user = request.user, information = request.POST["information"], training=request.POST["training"], training_period=request.POST["training_period"])
        new_company.save()
        print(new_company)

    
    return render(request, "Companies/Add_company.html", {"AddCompany" : AddCompany}) 





def LoginCompany(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("Companies:Home")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "Companies/login.html", {"msg" : msg})      
