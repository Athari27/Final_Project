from django.contrib import admin
from .models import Training,Contact,JobApplication

# Register your models here.
admin.site.register(Training)
admin.site.register(JobApplication)
admin.site.register(Contact)

