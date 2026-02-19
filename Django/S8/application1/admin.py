from django.contrib import admin
from application1.models import Product

class Product_Admin(admin.ModelAdmin):
    list_display=['id','Pid','Pname','Price','Company','M_date','Exp_date']
admin.site.register(Product,Product_Admin)