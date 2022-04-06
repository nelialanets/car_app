from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CAR_CATEGORY=(
        ('SUV','Sport Utility Vehicle'),
        ('MPV','Multi Purpose Vehicle'),
        ('ECO','Eco Car'),
        ('HEV','Hybrid Electric Vehicles'),
        ('EV', 'Electric Vehicles'),
        ('PU', 'Pick-Up Truck'),
        ('VAN', 'Van Car'),
        ('SED', 'Sedan'),
        ('SUP', 'Supercar'),
        ('COP','Coupe')

)

STATUS=(
        ('AVAILABLE','Available'),
        ('NO_AVAILABLE','Reserved'),
 )

class Car_Post(models.Model):
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    category=models.CharField(max_length=3, choices=CAR_CATEGORY)
    status=models.CharField(max_length=25, choices=STATUS)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.CharField(max_length=500)
    year=models.IntegerField()
    location=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    miles=models.IntegerField()
    price=models.IntegerField()
    about=models.CharField(max_length=200)
    model=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=100) 

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['name', 'location']