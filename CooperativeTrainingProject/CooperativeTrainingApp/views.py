from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import AddCompany
from accounts.models import Profile
from django.contrib.auth.models import User





# Create your views here. 

def Home(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/Home.html")
    


def Company(request : HttpRequest):
    user : User = request.user
    

    if request.method == "POST":
        new_company = AddCompany(user = request.user, information = request.POST["information"], training=request.POST["training"], training_period=request.POST["training_period"])
        new_company.save()
        print(new_company)

    
    return render(request, "CooperativeTrainingApp/Add_company.html", {"AddCompany" : AddCompany})

 

def ViewCompany(request : HttpRequest):

    New = AddCompany.objects.all()

    return render(request, "CooperativeTrainingApp/view_company.html", {"New" : New}) 



def AboutSite(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/AboutSite.html")





def ViewProfile(request : HttpRequest):

    New = Profile.objects.all()

    return render(request, "CooperativeTrainingApp/profil.html", {"New" : New}) 

