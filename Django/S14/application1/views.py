from django.shortcuts import render
from django.http import HttpResponse
from application1.models import Employee
def Test_case1(request):
    try:
        data=Employee.objects.get(Eid=1010)
    except:
        return HttpResponse("<h1><tt>Exception Name: Employee Record is not found sorry....</tt></h1>")
    
    return HttpResponse(data)
