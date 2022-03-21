from django.shortcuts import render
from django.http import HttpResponse

def vendas(request):
    return render(request,'vendas.html')

def produtos(request):
    return HttpResponse('pagina de produtos')