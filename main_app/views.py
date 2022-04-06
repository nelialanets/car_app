from django.shortcuts import render

from asyncio import subprocess
from dataclasses import field
from email.mime import audio
from pyexpat import model
# from nis import cat
from re import template
from sre_constants import SUCCESS
from urllib import response
from wsgiref.util import request_uri
from django.http import HttpResponse, HttpResponseRedirect # responses 
from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Car_Post
from .models import CarFeatures
#Auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Home(TemplateView):
    template_name='home.html'

class About(TemplateView):
    template_name='about.html'

class Car_List(TemplateView):
    template_name='car_list.html'
    def get_context_data(self, **kwargs):
         context=super().get_context_data(**kwargs)
         # to get the query parameter we have to acccess it in the request.GET dictionary object
         context['cars']=Car_Post.objects.all
         name = self.request.GET.get('name')
         if name != None:
             context['cars']=Car_Post.objects.filter(name_icontains=name)
             context['header'] = f"Searching for {name}"
         else:
             context["cars"] = Car_Post.objects.all()
            #  context ['header']='Cars List'
         return context


class Car_Detail(DetailView):
    model=Car_Post
    template_name='car_detail.html'
    def get_success_url(self):
     return reverse('car_detail', kwargs={'pk': self.object.pk})

class Car_Create(CreateView): #CREATE
    model=Car_Post
    fields=['name', 'color', 'category', 'status', 'image', 'year', 'location',  'miles', 'price', 'about', 'model', 'fuel_type', 'user']
    template_name ='car_create.html'
    success_url='/cars/'
    def get_success_url(self):
        return reverse ('car_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user = self.request.user # wehn we  make a request for the user that comes with the form of the created car== it will show who created a car 
        self.object.save()
        return HttpResponseRedirect('/cars')

class Car_Update(UpdateView):
    model=Car_Post
    fields=['name', 'color', 'category', 'status', 'image', 'year', 'location',  'miles', 'price', 'about', 'model', 'fuel_type']
    template_name ='car_update.html'
    # success_url='/cars/'
    def get_success_url(self):
     return reverse('car_detail', kwargs={'pk': self.object.pk}) 

class Car_Delete(DeleteView):
    model=Car_Post
    template_name="car_delete.html"
    success_url ='/cars/' #redirect

def Profile(request, username):
    user= User.objects.get(username=username)
    cars=Car_Post.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cars':cars})

    # M:M

def Car_Features_Index(request):
    car_features=CarFeatures.objects.all()
    return render(request,'features_index.html', {'car_features': car_features})

def Cartype_Show(request, car_features_id):
    car_feature=CarFeatures.objects.get(id=car_features_id)
    return render (request, 'car_features_show.html', {'car_feature=':car_feature}) # rendering out cartype=Car_Type.objects.get(id=cartype_id) object

