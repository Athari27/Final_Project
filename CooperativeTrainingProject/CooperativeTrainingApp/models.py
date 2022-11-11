from django.db import models

# Create your models here. 

class Company(models.Model):
    name_company = models.CharField(max_length=1024)
    information = models.TextField(null=True)
    training = models.BooleanField(null=True)

    


   
