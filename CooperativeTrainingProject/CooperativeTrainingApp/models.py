
from django.db import models 

# Create your models here. 

class AddCompany(models.Model):
       name_company = models.CharField(max_length=1024)
       information = models.TextField()
       training = models.BooleanField()
       training_period = models.CharField(max_length=1024)
       






    


   
