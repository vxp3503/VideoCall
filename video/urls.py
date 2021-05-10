from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.sender,name="sender"),
    path("receiver",views.receiver,name="receiver")
]
