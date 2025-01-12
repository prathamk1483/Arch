from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("data/",views.data,name="data"),
    path("invoice/",views.getInvoice,name="getInvoice"),
    path("print/",views.printInvoice,name="printInvoice"),
]
