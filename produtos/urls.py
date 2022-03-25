from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('curso/<int:id>', views.curso, name = 'curso'),
]