from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.vendas, name = 'vendas'),
    path('produtos/',views.produtos,name='produtos')
]