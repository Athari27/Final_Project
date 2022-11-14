from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from Companies.models import AddCompany
from accounts.models import Profile
from django.contrib.auth.models import User







# Create your views here. 

def Home(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/Home.html")
    



 

def ViewCompany(request : HttpRequest):

     if "search" in request.GET:
        New = AddCompany.objects.filter(title__contains=request.GET["search"])
     else:
        New = AddCompany.objects.all()


     #New = AddCompany.objects.all()

     return render(request, "CooperativeTrainingApp/view_company.html", {"New" : New}) 



def AboutSite(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/AboutSite.html")





def ViewProfile(request : HttpRequest , user_id : int):

    user = User.objects.get(id = user_id)
  
    
    return render(request, "CooperativeTrainingApp/profil.html", {"user" : user}) 



def TechnicalSupport(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/Support.html")    

