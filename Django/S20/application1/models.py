from django.db import models

class Employees(models.Model):
    Eid=models.IntegerField()
    Ename=models.CharField(max_length=21)
    Esal=models.FloatField()
    Design=models.CharField(max_length=21)
    Company=models.CharField(max_length=21)
    Email=models.EmailField()
    J_date=models.DateField()
