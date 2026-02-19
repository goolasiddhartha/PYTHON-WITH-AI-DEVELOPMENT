from django.db import models

class Employee(models.Model):
    Eid=models.IntegerField()
    Ename=models.CharField(max_length=21)
    Esal=models.FloatField()
    Design=models.CharField(max_length=21)
    Company=models.CharField(max_length=21)
    J_date=models.DateField()
    