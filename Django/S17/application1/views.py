from django.shortcuts import render

def Test_case1(request):
    request.session['name']="AI/Agentic AI"
    return render(request,'application1/S1.html',)

def Test_case2(request):
    name=request.session.get('name',default='sessions are not found')
    return render(request,"application1/S2.html",{'name':name})

def Test_case3(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'application1/S3.html')