from django.shortcuts import render
from django.http import HttpResponse

def Test_case3(request):
    return HttpResponse("<h1><tt>This is Service one from Application3</tt></h1>")