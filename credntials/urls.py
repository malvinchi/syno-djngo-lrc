#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from credntials import views

urlpatterns = [
       path('', views.search_view, name = 'search'),
   ]
