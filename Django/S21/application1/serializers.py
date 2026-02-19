from rest_framework import  serializers
class Product_serializers(serializers.Serializer):
    Pid=serializers.IntegerField()
    Pname=serializers.CharField(max_length=21)
    Price=serializers.FloatField()
    Company=serializers.CharField(max_length=21)
    M_date=serializers.DateField() 
    Exp_date=serializers.DateField()