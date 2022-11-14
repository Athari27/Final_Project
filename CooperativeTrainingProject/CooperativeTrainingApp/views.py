from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from Companies.models import AddCompany
from accounts.models import Profile






# Create your views here. 

def Home(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/Home.html")
    



 

def ViewCompany(request : HttpRequest):

    New = AddCompany.objects.all()

    return render(request, "CooperativeTrainingApp/view_company.html", {"New" : New}) 



def AboutSite(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/AboutSite.html")





def ViewProfile(request : HttpRequest):

    New = Profile.objects.all()

    return render(request, "CooperativeTrainingApp/profil.html", {"New" : New}) 

