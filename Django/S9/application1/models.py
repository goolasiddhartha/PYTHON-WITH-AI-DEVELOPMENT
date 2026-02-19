from django.db import models

class Employees(models.Model):
    Eid=models.IntegerField()
    Ename=models.CharField(max_length=25)
    Esal=models.FloatField()
    Design=models.CharField(max_length=25)
    Company=models.CharField(max_length=25)
    J_date=models.DateField()

