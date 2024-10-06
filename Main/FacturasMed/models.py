from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 100, null = False, blank = False, verbose_name = "Nombre del Usuario")
    apellido = models.CharField(max_length = 100, null = False, blank = False, verbose_name = "Apellido del Usuario")
    correo = models.EmailField(verbose_name = "Correo")
    contrasena = models.CharField(max_length = 255, blank = False, null  = False, verbose_name = "Contraseña")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificiación")
    ROLES = (
        ("A", "Administrador"),
        ("C", "Cliente"),
    )
    
    rol = models.CharField(max_length = 1, choices = ROLES, default = "C")
    
    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}\nCorreo: {self.correo}\nRol: {self.rol}\nFecha Creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\nFecha Modificación: {self.fecha_modificacion.strftime('%Y-%m-%d %H:%M:%S')}"

class Servicio(models.Model):
    nombre = models.CharField(max_length = 45, null = False, blank = False, unique = True, verbose_name = "Nombre del Servicio")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    
    def __str__(self):
        return f"Servicio: {self.nombre}\nFecha Creación: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"

class Contrato(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación")
    servicio = models.ForeignKey(Servicio, on_delete = models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete = models.PROTECT)
    
    def __str__(self):
        return f"Contrato #: {id}\nUsuario: {self.usuario.nombre}\nTipo Servicio: {self.servicio.nombre}"

class Factura(models.Model):
    pass