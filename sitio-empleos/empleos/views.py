from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Empleo, Categoria

def home(request):
    empleos_destacados = Empleo.objects.filter(activo=True)[:6]
    categorias = Categoria.objects.all()
    total_empleos = Empleo.objects.filter(activo=True).count()
    
    context = {
        'empleos_destacados': empleos_destacados,
        'categorias': categorias,
        'total_empleos': total_empleos,
    }
    return render(request, 'empleos/home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, '¡Bienvenido de vuelta!')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'empleos/login.html')