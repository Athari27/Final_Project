from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#creating a profile for the user
class Profile(models.Model):
    level = models.TextChoices("level", [ "6" , "7" , "8" ])

    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)

    
    gender = models.BooleanField()
    university_name = models.CharField(max_length=2048)
    department = models.CharField(max_length=2048)

    level_choices  = models.CharField(max_length=64, choices = level.choices)


