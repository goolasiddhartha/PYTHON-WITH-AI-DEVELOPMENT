from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=25)
    address=models.CharField(max_length=25)

class Hotel(models.Model):
    place=models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)

class Waiters(models.Model): 
    name=models.CharField(max_length=25)
    mobile_number=models.CharField(max_length=25)
    email_address=models.EmailField()
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)

