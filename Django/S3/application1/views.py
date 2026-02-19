from django.shortcuts import render
from django.http import HttpResponse

def Test_case1(request):
    return HttpResponse("<h1><tt>This is Service one from Application1</tt></h1>")