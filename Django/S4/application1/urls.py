from django.contrib import admin
from django.urls import path
from application1 import views

urlpatterns = [
    path('t1/', views.Test_Case1),
    path('t2/', views.Test_Case2),
    path('t3/', views.Test_Case3),
]
