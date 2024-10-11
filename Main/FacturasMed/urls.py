from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('registrarse', views.registrarse, name='registrarse'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', views.cerrar_sesion, name="cerrar_sesion"),
    path("contratos", views.ver_contratos, name="ver_contratos"),
    path("contratos/crear", views.crear_contrato, name="crear_contrato"),
    path("contratos/<int:id_contrato>/facturas", views.ver_facturas, name = 'ver_facturas'),
    path("contratos/<int:id_contrato>/facturas/<int:id_factura>/pagar", views.pagar_factura, name = 'pagar_factura')
]