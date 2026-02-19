from django.shortcuts import render

from django.http import HttpResponse
from application1.models import Employee
def Test_case1(request):
    data=Employee.objects.create(First_name="Rakesh",Last_name="Chakli",Username="rakesh_12345",P1="RAK_12345",P2="RAK_12345",Mobile_number="6785436785",Email_Address="rakesh@gmail.com")
    data.save()
    return HttpResponse("<h1><tt>Record is created Successfully....</tt><h1>")