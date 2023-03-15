from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Producto, Carrito, ItemCarrito
from .forms import LoginForm, RegistroForm, ProductoForm

def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def agregar_producto(request, producto_id):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    producto = Producto.objects.get(id=producto_id)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    item.cantidad += 1
    item.save()
    return redirect('carrito')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usuario = authenticate(request, email=email, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                form.add_error(None, 'Email o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            usuario = authenticate(request, email=email, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

def carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.itemcarrito_set.all()
    return render(request, 'carrito.html', {'items': items})