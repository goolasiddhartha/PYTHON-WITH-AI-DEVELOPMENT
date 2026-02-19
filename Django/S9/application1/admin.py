from django.contrib import admin

from application1.models import Employees
class Employee_Admin(admin.ModelAdmin):
    list_display=['id','Eid','Ename','Esal','Design','Company','J_date']
admin.site.register(Employees,Employee_Admin)