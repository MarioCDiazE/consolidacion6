from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    return render(request, 'vehiculo/index.html')


@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def addVehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = VehiculoForm()
    return render(request,'vehiculo/addVehiculo.html' , {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})

def userRegister(request):
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def listVehiculos(request):
    if request.user.is_authenticated and request.user.has_perm('vehiculo.visualizar_catalogo'):
        vehiculos = Vehiculo.objects.all()
        catPrecio = request.GET.get('precio')
        if catPrecio=='bajo':
            vehiculos = vehiculos.filter(precio__lt=10000)
        elif catPrecio=='medio':
            vehiculos = vehiculos.filter(precio__gte=10000, precio__lt=30000)
        elif catPrecio=='alto':
            vehiculos = vehiculos.filter(precio__gte=30000)
        return render(request, 'vehiculo/listVehiculos.html', {'vehiculos': vehiculos})
    else:
        return render(request, 'vehiculo/no_permiso.html')