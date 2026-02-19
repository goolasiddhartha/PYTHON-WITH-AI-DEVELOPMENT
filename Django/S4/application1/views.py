from django.shortcuts import render
from django.http import HttpResponse
def Test_Case1(request):
    return HttpResponse("<h1><tt>This is Service one</tt><h1>")
def Test_Case2(request):
    return HttpResponse("<h1><tt>This is Service two</tt><h1>")
def Test_Case3(request):
    return HttpResponse("<h1><tt>This is Service three</tt><h1>")