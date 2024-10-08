# Generated by Django 5.1.1 on 2024-10-07 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contrato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Servicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        max_length=45, unique=True, verbose_name="Nombre del Servicio"
                    ),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=100, verbose_name="Nombre del Usuario"),
                ),
                (
                    "apellido",
                    models.CharField(
                        max_length=100, verbose_name="Apellido del Usuario"
                    ),
                ),
                ("correo", models.EmailField(max_length=254, verbose_name="Correo")),
                (
                    "contrasena",
                    models.CharField(max_length=255, verbose_name="Contraseña"),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "fecha_modificacion",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de Modificiación"
                    ),
                ),
                (
                    "rol",
                    models.CharField(
                        choices=[("A", "Administrador"), ("C", "Cliente")],
                        default="C",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Factura",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("monto", models.FloatField(verbose_name="Contraseña")),
                (
                    "pagado",
                    models.BooleanField(default=False, verbose_name="Fue Pagada"),
                ),
                (
                    "fecha_emision",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Emisión"
                    ),
                ),
                (
                    "fecha_vencimiento",
                    models.DateTimeField(verbose_name="Fecha de Vencimiento"),
                ),
                (
                    "contrato",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="FacturasMed.contrato",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contrato",
            name="servicio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="FacturasMed.servicio"
            ),
        ),
        migrations.AddField(
            model_name="contrato",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="FacturasMed.usuario"
            ),
        ),
    ]
