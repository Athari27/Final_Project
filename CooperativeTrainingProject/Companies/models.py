from django.db import models 
from django.contrib.auth.models import User


# Create your models here. 

class AddCompany(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)

       information = models.TextField()
       training = models.BooleanField()
       training_period = models.CharField(max_length=1024)
       city = models.CharField(max_length=1024)

       
       


class Comment(models.Model):

    company = models.ForeignKey(AddCompany, on_delete = models.CASCADE)
    name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
       return f"{self.name}"
