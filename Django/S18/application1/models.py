from django.db import models

class Employee(models.Model):
    First_name=models.CharField(max_length=21)
    Last_name=models.CharField(max_length=21)
    Username=models.CharField(max_length=21)
    P1=models.CharField(max_length=21)
    P2=models.CharField(max_length=21)
    Mobile_number=models.CharField(max_length=15)
    Email_Address=models.CharField(max_length=17)

    def __str__(self):
        return self.First_name+""+self.Last_name+""+self.Username+""+self.P1+""+self.P2+""+self.Mobile_number+""+self.Email_Address


