from django.urls import path
from . import views

urlpatterns=[
    path('', views.Home.as_view(), name='home'), # name = nameof the route
    path('about/', views.About.as_view(), name = 'about'),
    path('cars/', views.Car_List.as_view(), name='car_list'),
    path('cars/new/', views.Car_Create.as_view(), name='car_create'),
    path('cars/<int:pk>/', views.Car_Detail.as_view(), name='car_detail'), 
    path('cars/<int:pk>/update', views.Car_Update.as_view(), name='car_update'),
    path('cars/<int:pk>delete', views.Car_Delete.as_view(), name='car_delete'),
    path('user/<username>/', views.Profile, name='profile'),
    
    ]
