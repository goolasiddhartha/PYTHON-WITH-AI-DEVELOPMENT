from django.contrib import admin

from application1.models import Products
class Products_Admin(admin.ModelAdmin):
    list_display=['Pid','Pname','Price','Company','M_date','Exp_date']
admin.site.register(Products,Products_Admin)