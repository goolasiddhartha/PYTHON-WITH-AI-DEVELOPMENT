from django import forms
class Product_Forms(forms.Form):
    Pid=forms.IntegerField(label="Pid")
    Pname=forms.CharField(max_length=21,label="Pname")
    Price=forms.FloatField(label="Price")
    Company=forms.CharField(max_length=21,label="Company")