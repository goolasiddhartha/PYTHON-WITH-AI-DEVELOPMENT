from django.db import models

class Products(models.Model):
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=21)
    Price=models.FloatField()
    Company=models.CharField(max_length=21)
    M_date=models.DateField()
    Exp_date=models.DateField()
