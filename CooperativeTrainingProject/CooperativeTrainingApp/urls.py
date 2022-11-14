from django.urls import path
from . import views

app_name = "CooperativeTrainingApp"

urlpatterns = [
    path("Home/", views.Home, name="Home"),


    path("profile/<user_id>", views.ViewProfile, name="Profile"),

   
    path("Company/", views.ViewCompany, name="Company"),


    path("AboutSite/", views.AboutSite, name="About_Site"),

    path("Support/", views.TechnicalSupport, name="Support"),
    
   
]