from django.urls import path
from . import views

app_name = "CooperativeTrainingApp"

urlpatterns = [
    path("Home/", views.Home, name="Home"),

    path("profile/<user_id>", views.ViewProfile, name="Profile"),

   
    path("Company/", views.ViewCompany, name="Company"),
    path("Training/", views.TrainingAnnouncement, name="Training"),

    path("ViewTraining/", views.ViewTraining, name="View_training"),
    path("Apply/", views.Apply, name="Apply"),


    path("AboutUs/", views.AboutUs, name="About_us"),
    path("Contact/", views.Contact, name="Contact"),
    
   
]