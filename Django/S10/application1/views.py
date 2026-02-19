from django.shortcuts import render
from application1.models import Students
from django.views import View
class Test_case1(View):
    def get(self,request):
        obj1=Students.objects.all()
        return render(render,"application1/S1.html",{'obj1':obj1}) 