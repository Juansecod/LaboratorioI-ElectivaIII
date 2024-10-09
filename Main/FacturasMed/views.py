from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Usuario, Contrato, Servicio
from .utils import validar_sesion

def inicio(request):
    return render(request, "template_base.html", {"current_page":"inicio"})
    
def registrarse(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        rol = request.POST['rol']

        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, "El correo ya está en uso.")
            return redirect('registrarse')

        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            contrasena=make_password(contrasena),  # Encriptar la contraseña            
            rol=rol
        )
        nuevo_usuario.save()
        
        datos_usuario = {
            "id": nuevo_usuario.id,
            "nombre_completo": f"{nuevo_usuario.nombre} {nuevo_usuario.apellido}",
            "correo": nuevo_usuario.correo,
            "rol": nuevo_usuario.rol
        }
        request.session["usuario"] = datos_usuario
        
        messages.success(request, "Registro exitoso. Se ha inicado una sesión automaticamente")
        return redirect('iniciar_sesion')

    return render(request, 'register.html', {"current_page": "iniciar_sesion"})

def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']

        try:
            usuario = Usuario.objects.get(correo=correo)
            if check_password(contrasena, usuario.contrasena):
                datos_usuario = {
                    "id": usuario.id,
                    "nombre_completo": f"{usuario.nombre} {usuario.apellido}",
                    "correo": usuario.correo,
                    "rol": usuario.rol
                }
                request.session["usuario"] = datos_usuario
                messages.success(request, "Inicio de sesión exitoso.")
                return redirect('inicio')  
            else:
                messages.error(request, "Contraseña incorrecta.")
        except Usuario.DoesNotExist:
            messages.error(request, "El correo no está registrado.")

    return render(request, 'login.html', {"current_page": "iniciar_sesion"})

def cerrar_sesion(request):
    try:
        del request.session["usuario"]
        messages.success(request, "Regresa pronto!")
        return redirect("iniciar_sesion")
    except:
        messages.error(request, "Error. Algo salio mal...")
        return redirect("inicio")
    
def ver_contratos(request):
    sesion = validar_sesion(request)
    if sesion is not True:
        return sesion
    usuario = request.session.get("usuario")
    contratos = Contrato.objects.filter(usuario_id = usuario["id"])
    return render(request, "contratos.html", {"current_page":"contratos", "contratos": contratos})

def crear_contrato(request):
    sesion = validar_sesion(request)
    if sesion is not True:
        return sesion
    contexto = {"current_page": "contratos"}
    try:
        if request.method == 'POST':
            id_servicio = request.POST.get('servicio', None)
            if(id_servicio is None):
                messages.warning(request, "Selecciona un servicio valido")
                return redirect('crear_contrato')
            cliente = Usuario.objects.get(pk=request.session.get("usuario")["id"])
            servicio = Servicio.objects.get(pk=id_servicio)
            contrato = Contrato(usuario = cliente, servicio = servicio)
            contrato.save()
            return redirect('ver_contratos')
        contexto["servicios"] = Servicio.objects.all()
        return render(request, 'formulario_contrato.html', contexto)
    except Exception as e:
        print(e)
        messages.error(request, "Ups!, algo salio mal...")
        return redirect('crear_contrato')