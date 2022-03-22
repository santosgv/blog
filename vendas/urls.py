from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.vendas, name = 'vendas'),
]