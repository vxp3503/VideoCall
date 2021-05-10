from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
import os

def sender(request):
    return render(request,'video/sender.html')#this is sachin

def receiver(request):
    return render(request,'video/receiver.html')#this is sachin
