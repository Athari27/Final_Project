from django.db import models 
from django.contrib.auth.models import User

# Create your models here. 

class Training(models.Model):
    company_name = models.CharField(max_length=1024)
    training_title =  models.CharField(max_length=1024)
    city =  models.CharField(max_length=1024)


class Contact(models.Model):
    name = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"


class JobApplication(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    file = models.FileField(upload_to="media/file")

    def __str__(self) -> str:
        return f"{self.name}"




   
