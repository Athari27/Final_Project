from django.urls import path
from . import views

app_name = "Companies"

urlpatterns = [ 

    path("AddCompany/", views.Company, name="Add_Company"),

    path("login/", views.LoginCompany, name="login_company"),
        
    path("Logout/", views.LogoutCompany, name="logout_company"),


]