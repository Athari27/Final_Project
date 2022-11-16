from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from Companies.models import AddCompany
from accounts.models import Profile
from .models import Training,JobApplication,Contact
from django.contrib.auth.models import User



# Create your views here. 

def Home(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/Home.html")
    

#view all the company
def ViewCompany(request : HttpRequest):

     if "search" in request.GET:
        New = AddCompany.objects.filter(city__contains=request.GET["search"])
     else:
        New = AddCompany.objects.all()

     return render(request, "CooperativeTrainingApp/view_company.html", {"New" : New})





#publication of training opportunities by companies
def TrainingAnnouncement(request : HttpRequest):
    #to add a company, the user must be logged in as acompany
    #user : User = request.user

    #if not (user.is_authenticated and user.has_perm("CooperativeTrainingApp.Training")):
        #return redirect("Companies:login_company") 
    

    if request.method == "POST":
    
        train1 = Training( company_name = request.POST["company_name"], training_title=request.POST["training_title"], city=request.POST["city"])
        train1.save()
        
    return render(request, "CooperativeTrainingApp/training.html",{"Training" : Training})



#show the training opportunities
def ViewTraining(request : HttpRequest):

    train2 = Training.objects.all()

    return render(request, "CooperativeTrainingApp/view_training.html", {"train" : train2}) 





#send requesting training by the student
def Apply(request : HttpRequest, train_id):
 
    if request.method == "POST":
        train = Training.objects.get(id=train_id)
        send = JobApplication(user=request.user, training=train, name = request.POST["name"], email=request.POST["email"], file=request.FILES["file"])
        send.save()
        
    return render(request, "CooperativeTrainingApp/apply.html")



#show the my requests
def my_requests(request : HttpRequest):

    requests = JobApplication.objects.all()

    return render(request, "CooperativeTrainingApp/my_requests.html", {"requests" : requests})     



#to view profile
def ViewProfile(request : HttpRequest , user_id : int):

    user = User.objects.get(id = user_id)
    
    return render(request, "CooperativeTrainingApp/profil.html", {"user" : user}) 






def AboutUs(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/about_us.html")

    


def contact(request : HttpRequest):
    
    if request.method == "POST":
    
        send = Contact( name = request.POST["name"], email=request.POST["email"], message=request.POST["message"])
        send.save()
        
    return render(request, "CooperativeTrainingApp/contact.html")    

