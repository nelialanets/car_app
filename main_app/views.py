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

class Home(TemplateView):
    template_name='home.html'

class About(TemplateView):
    template_name='about.html'