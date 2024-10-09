from django.shortcuts import redirect
from django.contrib import messages

def validar_sesion(request):
    if(request.session.get("usuario", None) is None):
        messages.warning(request, "Para usar esta funcionalidad necestas inciar sesion")
        return redirect("iniciar_sesion")
    return True