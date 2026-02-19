from django.shortcuts import render
from application1.models import Products

def Test_case1(request):
    return render(request,"application1/S1.html")

def Test_case2(request):
    return render(request,"application1/S2.html")

def Test_case3(request):
    return render(request,"application1/S3.html")

def Test_case4(request):
    data=Products.objects.all()
    return render(request,"application1/S4.html",{'data':data})