from django.shortcuts import render
from application1.forms import Product_Forms
def Test_case1(request):
    data=Product_Forms()
    return render(request,"application1/S1.html",{'data':data})