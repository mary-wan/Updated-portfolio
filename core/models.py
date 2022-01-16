from django.db import models
from pyuploadcare.dj.models import ImageField


# About Model.
class About(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    profile = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    # short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


#Services Model

class Service(models.Model): 
    # image = models.ImageField(upload_to="service",null=True,blank=True)
    image= ImageField(manual_crop="",null=True,blank=True)
    name = models.CharField(max_length=200,verbose_name="Service Name",null=True,blank=True)
    description = models.TextField(verbose_name="Service Name",null=True,blank=True)

    def __str__(self):
        return self.name
#Recent work model

class RecentWork(models.Model):
    title = models.CharField(max_length=300,verbose_name = "Work title ")
    image = models.ImageField(upload_to="work")
    url = models.CharField(max_length=500,null=True,blank=True)
    

    def __str__(self):
        return  self.title

#Client model
class Client(models.Model):
    name = models.CharField(max_length = 200,verbose_name= "Client Name")
    description = models.TextField(verbose_name= "Client say")
    image = models.ImageField(upload_to="client",default="default.png")

    def __str__(self):
        return self.name
class Contact(models.Model):
    full_name = models.CharField(max_length=400)
    email = models.EmailField(null=True,blank=True)
    message = models.TextField(verbose_name= "contact message")