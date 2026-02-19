from application1.models import Employees
from django.forms import ModelForm

class Employees_Form(ModelForm):
    class Meta:
        model=Employees
        fields="__all__"