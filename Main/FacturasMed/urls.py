from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('registrarse', views.registrarse, name='registrarse'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', views.cerrar_sesion, name="cerrar_sesion"),
    path("contratos", views.ver_contratos, name="ver_contratos"),
    path("ver_contratos", views.crear_contrato, name="crear_contrato")
]