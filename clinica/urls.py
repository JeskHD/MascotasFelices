from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='clinica/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='portal'), name='logout'),
    # Otras rutas...
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('cliente/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('cliente/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('cliente/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('mascota/<int:pk>/', views.detalle_mascota, name='detalle_mascota'),
    path('portal/', views.portal_login, name='portal'),
    path('home/', views.home, name='home'),
    path('administrar_clientes/', views.administrar_clientes, name='administrar_clientes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registrar_mascota/', views.registrar_mascota, name='registrar_mascota'),
    path('historial-medico/', views.historial_medico, name='historial_medico'),
    path('administrar_clientes/', views.administrar_clientes, name='administrar_clientes'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('editar_cliente/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('eliminar_mascota/<int:pk>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('editar_mascota/<int:pk>/', views.editar_mascota, name='editar_mascota'),
    path('client/<int:client_id>/', views.perfil_cliente, name='perfil_cliente'),
    path('editar_mascota/<int:pk>/', views.editar_mascota, name='editar_mascota'),



]
