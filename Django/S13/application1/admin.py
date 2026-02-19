from django.contrib import admin

from application1.models import Product
from application1.models import Customer

class Product_admin(admin.ModelAdmin):
    list_display=['Pid','Pname','Price','Company','M_date','Exp_date']
admin.site.register(Product,Product_admin)

class Customer_admin(admin.ModelAdmin):
    list_display=['Cid','Cname','Address','City']
admin.site.register(Customer,Customer_admin)