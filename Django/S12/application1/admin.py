from django.contrib import admin

from application1.models import Reporters
from application1.models import Article

class Reporters_Admin(admin.ModelAdmin):
    list_display=['First_Name','Last_Name','UserName','P1','P2','Email_Address']
admin.site.register(Reporters,Reporters_Admin)

class Article_Admin(admin.ModelAdmin):
    list_display=['headline','content','public_date','reporters']
admin.site.register(Article,Article_Admin)