from django.db import models 

# Create your models here. 

class training(models.Model):
    company_name = models.CharField(max_length=1024)
    training_title =  models.CharField(max_length=1024)
    city =  models.CharField(max_length=1024)



    


   
