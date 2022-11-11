from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here. 

def Home(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/Home.html")
    


def RegisterUser(request : HttpRequest):

    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"], gender=request.POST["gender"], university_name=request.POST["university_name"], department=request.POST["department"], level=request.POST["level"])
        new_user.save()

    return render(request, "CooperativeTrainingApp/register.html")

    
def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("CooperativeTrainingApp:Home")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "CooperativeTrainingApp/login.html", {"msg" : msg})





def AddCompany(request : HttpRequest):

    if request.method == "POST":
        new_company = Company(name_company=request.POST["name_company"], information = request.POST["information"], training=request.POST["training"])
        new_company.save()

    
    return render(request, "CooperativeTrainingApp/Add_company.html")

 
def ViewCompany(request : HttpRequest):

    New = Company.objects.all()

    return render(request, "CooperativeTrainingApp/view_company.html", {"New" : New})










def AddStudent(request : HttpRequest):
   output2 = ""

   return render(request, "Clinic2/Add-company.html",{"output2" : output2}) 



def AboutSite(request : HttpRequest):
        
    return render(request, "CooperativeTrainingApp/AboutSite.html")




def LogoutUser(request: HttpRequest):

    logout(request)

    return redirect("Clinic2:Home")

