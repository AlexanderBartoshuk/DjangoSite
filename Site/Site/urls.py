"""
URL configuration for Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from asyncio import base_events
import base64
from email.mime import base
from itertools import product
from logging import info
from django import views
from django.contrib import admin
from django.urls import include, path
from APP.views import *
from django.urls import path





product_patterns = [
    path('product1/' , page1),
    path('product2/' , page2),
    path('product3/' , page3),
    path("", products_page)
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', hello_world),
    path('random/', random_page),
    path('', main_page , name='home'),
    path('pages/', include("APP.urls")),    
    path('products/', include(product_patterns)),
    path('pages/<path:id>/' , pages),
    path('user/' , user), 
    path('image/' , file_show),
    path('drift/' , file_1),                            
    path('smoke/' , file_2),
    path("competitions/" , file_3),
    path("file/<int:id>/" , files),
    path('json/' , json_work),
    path("info/" , info_page),
    path('products/' , products_page),
    path('work/' , work_page),
    path('course/' , course_page),
    path('hour/' , hour_page),
    path('materials/' , materials_page),
    path('payment/' , payment_page),
    path('person/' , person_page),
    path('work/' , work_page),
    path('client/create/', app_client, name='create_client'),

 
]
"""
str - любая пустая строка,  исключая символ /
ing - любое положительное число включая ноль 
slug - слаг , латиница, символы дефиса и подчеркивания
uuid - цифры, малые латинские символы и дефис 
path - любая не пустая строка, включая символ / 

"""