from .models import Curso
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    Cursos = Curso.objects.all()
    return render(request,'home.html',{'Cursos':Cursos})

def curso(request,id):
    curso=Curso.objects.get(id=id)
    return render(request,'curso.html',{'curso':curso})