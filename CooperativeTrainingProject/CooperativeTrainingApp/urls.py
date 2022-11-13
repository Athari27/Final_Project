from django.urls import path
from . import views

app_name = "CooperativeTrainingApp"

urlpatterns = [
    path("Home/", views.Home, name="Home"),

    path("Register/", views.RegisterUser, name="Register_user"),
     path("Home/", views.login_user, name="login_user"),
    
    
    path("AddStudent/", views.AddStudent, name="Add_Student"),

    

    #path("Profile/", views., name="Profile"),

    path("AddCompany/", views.Company, name="Add_Company"),
    path("Company/", views.ViewCompany, name="Company"),

    path("AboutSite/", views.AboutSite, name="About_Site"),

    path("Logout/", views.LogoutUser, name="logout_user"),
    
   
]