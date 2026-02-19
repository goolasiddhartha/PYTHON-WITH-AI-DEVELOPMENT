from django.http import HttpResponse

def Test_case1(request):
    return HttpResponse("<h1><tt>This is Application service one</tt></h1>")

def Test_case2(request):
    return HttpResponse("<h1><tt>This is Application service two</tt></h1>")

def Test_case3(request):
    return HttpResponse("<h1><tt>This is Application service three</tt></h1>")
