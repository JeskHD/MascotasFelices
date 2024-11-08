from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('mascota/<int:pk>/', views.detalle_mascota, name='detalle_mascota'),
]
