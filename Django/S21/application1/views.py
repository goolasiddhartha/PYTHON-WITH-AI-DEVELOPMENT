from django.http import HttpResponse
from application1.models import Products
from application1.serializers import Product_serializers
from rest_framework.renderers import JSONRenderer

def Test_case1(request):
    data = Products.objects.get(Pid=1001)
    serializer = Product_serializers(data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")

def Test_case2(request):
    data = Products.objects.all()
    serializer = Product_serializers(data,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")

def Test_case3(request,id):
    data = Products.objects.get(id=id)
    serializer = Product_serializers(data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")
