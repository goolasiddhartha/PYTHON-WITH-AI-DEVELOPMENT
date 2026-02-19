from django.contrib import admin

from application1.models import Employee
class Employee_Admin(admin.ModelAdmin):
    list_display=['First_name','Last_name','Username','P1','P2','Mobile_number','Email_Address']
admin.site.register(Employee,Employee_Admin)
