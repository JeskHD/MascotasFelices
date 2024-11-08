from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente, Mascota, HistorialMedico
from .forms import ClienteForm, MascotaForm, HistorialMedicoForm
from django.contrib.auth.models import User
from django.contrib.auth import login  # Importación necesaria
from django.contrib import messages  # Agregar esta línea si aún no está importado






def home(request):
    return render(request, 'clinica/home.html')

def portal(request):
    return render(request, 'clinica/portal.html')

def portal_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verificar las credenciales manualmente
        if (username == 'daniel' and password == '12345') or (username == 'kali' and password == 'umpalumpa28'):
            # Autenticar o crear el usuario si no existe
            user, created = User.objects.get_or_create(username=username)
            user.set_password(password)  # Asegurar que la contraseña esté configurada
            user.save()
            login(request, user)  # Iniciar sesión con el usuario autenticado
            
            # Redirigir al dashboard
            return redirect('dashboard')
        else:
            # Mostrar mensaje de error en caso de credenciales incorrectas
            messages.error(request, 'Credenciales no son válidas, intente de nuevo...')
            return redirect('portal')
    else:
        return render(request, 'clinica/portal.html')

@login_required
def home(request):
    return render(request, 'clinica/home.html')

@login_required
def administrar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clinica/administrar_clientes.html', {'clientes': clientes})



@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clinica/lista_clientes.html', {'clientes': clientes})

@login_required
def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clinica/detalle_cliente.html', {'cliente': cliente})

@login_required
def crear_cliente(request):
    cliente_form = ClienteForm(request.POST or None)
    mascota_form = MascotaForm(request.POST or None)
    historial_form = HistorialMedicoForm(request.POST or None)

    if request.method == 'POST':
        if cliente_form.is_valid():
            cliente = cliente_form.save()  # Guarda el cliente
            if mascota_form.is_valid():
                mascota = mascota_form.save(commit=False)
                mascota.cliente = cliente  # Asocia la mascota al cliente
                mascota.save()
                
                if historial_form.is_valid() and historial_form.cleaned_data.get('fecha_visita'):
                    historial = historial_form.save(commit=False)
                    historial.mascota = mascota  # Asocia el historial médico a la mascota
                    historial.save()
                
                return redirect('perfil_cliente', cliente_id=cliente.id)  # Redirige al perfil del cliente
        
    context = {
        'cliente_form': cliente_form,
        'mascota_form': mascota_form,
        'historial_form': historial_form,
    }
    return render(request, 'clinica/crear_cliente.html', context)

@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('detalle_cliente', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clinica/editar_cliente.html', {'form': form})

@login_required
def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'clinica/detalle_mascota.html', {'mascota': mascota})

@login_required
def dashboard(request):
    return render(request, 'clinica/dashboard.html')

@login_required
def registrar_mascota(request):
    # Lógica para registrar una mascota
    return render(request, 'clinica/registrar_mascota.html')


@login_required
def historial_medico(request):
    # Lógica para historial médico
    return render(request, 'clinica/historial_medico.html')

@login_required
def administrar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clinica/administrar_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        mascota_form = MascotaForm(request.POST)
        historial_form = HistorialMedicoForm(request.POST)

        if cliente_form.is_valid() and mascota_form.is_valid() and historial_form.is_valid():
            # Guardar el cliente
            cliente = cliente_form.save()

            # Asignar el cliente a la mascota y guardar la mascota
            mascota = mascota_form.save(commit=False)
            mascota.cliente = cliente
            mascota.save()

            # Asignar la mascota al historial médico y guardar el historial
            historial_medico = historial_form.save(commit=False)
            historial_medico.mascota = mascota
            historial_medico.save()

            return redirect('lista_clientes')  # Redirige a la lista de clientes u otra página que prefieras
    else:
        cliente_form = ClienteForm()
        mascota_form = MascotaForm()
        historial_form = HistorialMedicoForm()

    return render(request, 'clinica/crear_cliente.html', {
        'cliente_form': cliente_form,
        'mascota_form': mascota_form,
        'historial_form': historial_form,
    })

@login_required
def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    form = MascotaForm(request.POST or None, instance=mascota)

    if form.is_valid():
        form.save()
        return redirect('perfil_cliente', cliente_id=mascota.cliente.id)

    return render(request, 'clinica/editar_mascota.html', {'form': form})

@login_required
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('administrar_clientes')
    return render(request, 'clinica/eliminar_cliente.html', {'cliente': cliente})

@login_required
def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    mascota.delete()
    return redirect('administrar_clientes')  # Redirige a la lista de clientes o la vista adecuada

@login_required
def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('administrar_clientes')  # Redirige a la vista de administración de clientes
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'clinica/editar_mascota.html', {'form': form})

@login_required
def crear_mascota(request, cliente_id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        especie = request.POST['especie']
        raza = request.POST.get('raza', '')
        edad = request.POST.get('edad', '')

        cliente = get_object_or_404(Cliente, pk=cliente_id)
        Mascota.objects.create(cliente=cliente, nombre=nombre, especie=especie, raza=raza, edad=edad)

        return redirect('perfil_cliente', cliente_id=cliente.id)



def perfil_cliente(request, client_id):
    client = get_object_or_404(Cliente, id=client_id)
    pets = client.mascotas.all()
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.cliente = client
            pet.save()
            return redirect('perfil_cliente', client_id=client.id)
    else:
        form = MascotaForm()
    return render(request, 'clinica/perfil_cliente.html', {'client': client, 'pets': pets, 'form': form})
    

    

