from django.db import models

class Reporters(models.Model):
    First_Name=models.CharField(max_length=25)
    Last_Name=models.CharField(max_length=25)
    UserName=models.CharField(max_length=25)
    P1=models.CharField(max_length=15)
    P2=models.CharField(max_length=15)
    Email_Address=models.EmailField()

class Article(models.Model):
    headline=models.CharField(max_length=25)
    content=models.CharField(max_length=100)
    public_date=models.DateField()
    reporters=models.ForeignKey(Reporters,on_delete=models.CASCADE)


