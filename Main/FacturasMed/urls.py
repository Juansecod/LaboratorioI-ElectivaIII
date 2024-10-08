from django.urls import path
from . import views

urlpatterns = [
    path("", views.template_base, name="template_base"),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
]