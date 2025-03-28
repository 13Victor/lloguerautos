from django.urls import path
from . import views

urlpatterns = [
    path('autos/', views.listar_automoviles, name='listar_automoviles'),
]
