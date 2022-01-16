from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from core.models import *
from .forms import *
from django.contrib import messages



class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(full_name,'//////////////////')
            print(email,'//////////////////')
            print(message,'//////////////////')
            
            return redirect('/')
        context = {
            "form":form,

        }
        return render(request,'home.html',locals())




# def save_contact(request):
#     if request.method == "GET":
#         form = ContactForm(request.GET)
#         if form.is_valid():
#             form.full_name = request.GET.get('full_name')
#             form.email = request.GET.get('email')
#             form.message = request.GET.get('message')
#             print(form.full_name,"rrrrrrrrrrrr")
#             print(form.email,"rrrrrrrrrrrr")
#             print(form.message,"rrrrrrrrrrrr")
#             form.save()
#             messages.success(request,"Message send successfully")
#             return render(request,'home.html')
#         else:
#             messages.success(request,"Message already send")
#             return render(request,'home.html')

