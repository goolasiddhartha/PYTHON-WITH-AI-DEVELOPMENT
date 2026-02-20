from django.shortcuts import render
from application1.models import Employees
from application1.serializers import Employee_serializers
from rest_framework.viewsets import ModelViewSet
class Employee_Curd_operations(ModelViewSet):
    queryset=Employees.objects.all()
    serializer_class=Employee_serializers

