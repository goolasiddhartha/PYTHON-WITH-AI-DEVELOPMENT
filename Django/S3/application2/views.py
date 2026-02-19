from django.shortcuts import render
from django.http import HttpResponse

def Test_case2(request):
    return HttpResponse("<h1><tt>This is Service one from Application2</tt></h1>")