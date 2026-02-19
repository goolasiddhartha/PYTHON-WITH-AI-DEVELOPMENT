from django.contrib import admin
from django.urls import path
from application_1 import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t1/', views.Test_case1),
    path('t2/', views.Test_case2),
    path('t3/', views.Test_case3),
]
