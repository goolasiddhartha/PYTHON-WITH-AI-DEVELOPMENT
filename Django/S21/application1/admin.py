from django.contrib import admin

from application1.models import Products

class Product_Admin(admin.ModelAdmin):
    list_display=['Pid','Pname','Price','Company','M_date','Exp_date']
admin.site.register(Products,Product_Admin)
