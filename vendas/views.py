from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def vendas(request):
    produtos =Produto.objects.all()
    return render(request,'vendas.html',{'produtos':produtos})

