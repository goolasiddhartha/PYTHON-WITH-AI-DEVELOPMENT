from django.shortcuts import render

def Test_case1(request):
    response=render(request,"application1/S1.html")
    response.set_cookie('name','Medhansh_IT_Services')
    return response

def Test_case2(request):
    name=request.COOKIES.get('name','cookies are not found')
    return render(request,"application1/S2.html",{"name":name})

def Test_case3(request):
    response=render(request,'application1/S3.html')
    response.delete_cookie('name')
    return response
