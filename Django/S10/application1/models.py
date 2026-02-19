from django.db import models

class Students(models.Model):
    Sid=models.IntegerField()
    Sname=models.CharField(max_length=25)
    Marks=models.FloatField()
    
