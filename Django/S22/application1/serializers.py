from rest_framework.serializers import ModelSerializer
from application1.models import Employees
class Employee_serializers(ModelSerializer):
    class Meta:
        model=Employees
        fields="__all__"