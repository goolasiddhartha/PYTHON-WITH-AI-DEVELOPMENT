from django.shortcuts import render

from application1.models import Employees
from application1.forms import Employees_Form

def Test_case1(request):
    form=Employees_Form()
    if request.method=="POST":
        form=Employees_Form(request.POST)
        if form.is_valid():     
            form.save()
    context={'form':form}
    return render(request,"application1/S1.html",context)
