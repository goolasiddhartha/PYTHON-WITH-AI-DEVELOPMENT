from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class Test_case1(View):
    def get(self,request):
        return HttpResponse("<h1><tt>This Service using class component....</tt></h1>")
