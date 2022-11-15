from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from Companies.models import AddCompany
from accounts.models import Profile
from .models import Training,JobApplication

from django.contrib.auth.models import User




# Create your views here. 

def Home(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/Home.html")
    

def ViewCompany(request : HttpRequest):

     if "search" in request.GET:
        New = AddCompany.objects.filter(city__contains=request.GET["search"])
     else:
        New = AddCompany.objects.all()

     return render(request, "CooperativeTrainingApp/view_company.html", {"New" : New})









def TrainingAnnouncement(request : HttpRequest):
    user : User = request.user

    if not (user.is_authenticated and user.has_perm("CooperativeTrainingApp.Training")):
        return redirect("Companies:login_company")

    if request.method == "POST":
    
        train1 = Training( company_name = request.POST["company_name"], training_title=request.POST["training_title"], city=request.POST["city"])
        train1.save()
        
    return render(request, "CooperativeTrainingApp/training.html")




def ViewTraining(request : HttpRequest):

    train2 = Training.objects.all()

    return render(request, "CooperativeTrainingApp/view_training.html", {"train" : train2}) 


def Apply(request : HttpRequest):
 
    if request.method == "POST":
    
        send = JobApplication( name = request.POST["name"], email=request.POST["email"], file=request.FILES["file"])
        send.save()
        
    return render(request, "CooperativeTrainingApp/apply.html")







def ViewProfile(request : HttpRequest , user_id : int):

    user = User.objects.get(id = user_id)
  
    
    return render(request, "CooperativeTrainingApp/profil.html", {"user" : user}) 






def AboutUs(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/AboutUs.html")

    


def Contact(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/contact.html")    

