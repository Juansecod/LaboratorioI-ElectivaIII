from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Usuario

def template_base(request):
    return render(request, "template_base.html")
    
def registrarse(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        rol = request.POST['rol']

        # Validación básica (puedes expandir esto)
        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, "El correo ya está en uso.")
            return redirect('registrarse')

        # Crear el nuevo usuario
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            contrasena=make_password(contrasena),  # Encriptar la contraseña            
            rol=rol
        )
        nuevo_usuario.save()
        messages.success(request, "Registro exitoso. Puedes iniciar sesión.")
        return redirect('iniciar_sesion')

    return render(request, 'register.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']

        try:
            usuario = Usuario.objects.get(correo=correo)
            if check_password(contrasena, usuario.contrasena):
                # Aquí podrías iniciar sesión usando Django's auth system
                # pero para este caso, simplemente redirigimos
                messages.success(request, "Inicio de sesión exitoso.")
                return redirect('template_base')  # Cambia 'inicio' por tu URL de inicio
            else:
                messages.error(request, "Contraseña incorrecta.")
        except Usuario.DoesNotExist:
            messages.error(request, "El correo no está registrado.")

    return render(request, 'login.html')