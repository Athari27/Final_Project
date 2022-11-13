from django.urls import path
from . import views

app_name = "CooperativeTrainingApp"

urlpatterns = [
    path("Home/", views.Home, name="Home"),


    path("profile/", views.ViewProfile, name="Profile"),

    path("AddCompany/", views.Company, name="Add_Company"),
    path("Company/", views.ViewCompany, name="Company"),

    path("AboutSite/", views.AboutSite, name="About_Site"),
    
   
]