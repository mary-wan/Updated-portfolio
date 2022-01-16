from django import forms
from .models import *

class ContactForm(forms.ModelForm):
   
        full_name = models.CharField(max_length=400)
        email = models.EmailField(null=True,blank=True)
        message = models.TextField(verbose_name= "contact message")

        class Meta:
            model = Contact
            fields = ['full_name','email','message']

