from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [  
   
        path("Register/", views.RegisterUser, name="Register_user"), 

        path("login/", views.LoginUser, name="login_user"),
        
        path("Logout/", views.LogoutUser, name="logout_user"),


]