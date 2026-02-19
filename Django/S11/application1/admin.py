from django.contrib import admin

from application1.models import Place
from application1.models import Hotel
from application1.models import Waiters

class Place_Admin(admin.ModelAdmin):
    list_display=['name','address']
admin.site.register(Place,Place_Admin)

class Hotel_Admin(admin.ModelAdmin):
    list_display=['place']
admin.site.register(Hotel,Hotel_Admin)

class Waiters_Admin(admin.ModelAdmin):
    list_display=['name','mobile_number','email_address','hotel']
admin.site.register(Waiters,Waiters_Admin)