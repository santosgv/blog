from .models import Posts
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    posts = Posts.objects.all()
    return render(request,'home.html',{'posts':posts})

def posts(request):
    return render(request,'posts.html')