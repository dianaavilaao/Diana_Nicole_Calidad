from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Masaje
from .forms import MasajeForm

def home(request):
    return HttpResponse("¡Hola, Django!")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu_principal')
    return render(request, 'login.html')

def menu_principal(request):
    return render(request, 'menu_principal.html')

def mantenedor_masajes(request):
    masajes = Masaje.objects.all()
    return render(request, 'mantenedor_masajes.html', {'masajes': masajes})

def crear_masaje(request):
    if request.method == 'POST':
        form = MasajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mantenedor_masajes')
    else:
        form = MasajeForm()
    return render(request, 'crear_masaje.html', {'form': form})

def actualizar_masaje(request, pk):
    masaje = Masaje.objects.get(pk=pk)
    if request.method == 'POST':
        form = MasajeForm(request.POST, instance=masaje)
        if form.is_valid():
            form.save()
            return redirect('mantenedor_masajes')
    else:
        form = MasajeForm(instance=masaje)
    return render(request, 'actualizar_masaje.html', {'form': form})

def eliminar_masaje(request, pk):
    masaje = Masaje.objects.get(pk=pk)
    if request.method == 'POST':
        masaje.delete()
        return redirect('mantenedor_masajes')
    return render(request, 'eliminar_masaje.html', {'masaje': masaje})

def index(request):
    return render(request, 'index.html')