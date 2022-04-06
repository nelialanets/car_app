from django.urls import path
from . import views

urlpatterns=[
    path('', views.Home.as_view(), name='home'), # name = nameof the route
    path('about/', views.About.as_view(), name = 'about'),
   
    
    ]
