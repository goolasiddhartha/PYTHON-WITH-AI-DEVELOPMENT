"""
URL configuration for S19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', views.Test_case1,name="web1"),
    path('a1/', views.Test_case2,name="web2"),
    path('a2/', views.Test_case3,name="web3"),
    path('a3/', views.Test_case4,name="web4"),
]
