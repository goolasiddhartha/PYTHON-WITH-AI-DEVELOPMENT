from django.contrib import admin

from application1.models import Employees
class Employees_admin(admin.ModelAdmin):
    list_display=['Eid','Ename','Esal','Design','Company','Email','J_date']
admin.site.register(Employees,Employees_admin)
