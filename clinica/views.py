from django.shortcuts import render, get_object_or_404
from .models import Cliente, Mascota

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clinica/lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clinica/detalle_cliente.html', {'cliente': cliente})

def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'clinica/detalle_mascota.html', {'mascota': mascota})
