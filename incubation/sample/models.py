from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    Needed =(('Physical_Incubation','Physical_Incubation'),('Virtual_Incubation ' ,'Virtual_Incubation' ))
    Process =(('Registration_Approved','Registration_Approved'),('Under_Process ','Under_Process' ,),('Approved','Approved',))

    name = models.CharField(max_length=200)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Address = models.TextField()
    city =models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    compay_logo = models.ImageField(upload_to ='uploads/')
    team_background =  models.TextField()
    about_companyProducts  = models.TextField()
    problems = models.TextField()
    uniqueSolution = models.TextField()
    valueProposition = models.TextField()
    competativeAdvantage = models.TextField()
    revenue = models.CharField(max_length=200)
    marketsize = models.CharField(max_length=200)
    marketplan =  models.TextField()
    incubationtype = models.CharField(max_length=100, choices=Needed)
    detailProposal = models.TextField()
    AppProcess =  models.CharField(max_length=100, choices=Process,null=True,default='Registration Approved')

    def __str__(self):
        return self.name 