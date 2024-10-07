from django.contrib import admin
from .models import Usuario, Servicio, Contrato, Factura

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido", "correo", "rol", "fecha_creacion", "fecha_modificacion"]
    search_fields =["nombre", "apellido", "correo"]
    list_filter = ["rol", "fecha_creacion", "fecha_modificacion"]
    
admin.site.register(Usuario, UsuarioAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "fecha_creacion"]
    search_fields =["nombre"]
    list_filter = ["fecha_creacion"]

admin.site.register(Servicio, ServicioAdmin)

class ContratoAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "servicio", "fecha_creacion"]
    search_fields =[]
    list_filter = ["fecha_creacion"]

admin.site.register(Contrato, ContratoAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ["id", "monto", "pagado", "fecha_emision", "fecha_vencimiento", "contrato"]
    search_fields =[]
    list_filter = ["pagado", "fecha_emision", "fecha_vencimiento"]

admin.site.register(Factura, FacturaAdmin)