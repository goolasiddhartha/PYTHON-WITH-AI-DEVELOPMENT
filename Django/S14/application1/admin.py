from django.contrib import admin

from application1.models import Employee

class Employee_Admin(admin.ModelAdmin):
    list_display=['Eid','Ename','Esal','Design','Company','J_date']
admin.site.register(Employee,Employee_Admin)
