from django.shortcuts import render
from application1.models import Employees

def Test_case1(request):
    Data=Employees.objects.all()
    return render(request,"application1/S1.html",{"Data":Data})
