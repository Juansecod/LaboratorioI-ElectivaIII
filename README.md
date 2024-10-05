# Laboratorio 1: Sistema de Facturación de servicios públicos de Medellín

Construir un proyecto usando el framework **django** que permita realizar las siguientes acciones:

1. Permitir Registrar usuarios (Debe existir un super usuario previamente creado, que no se pueda eliminar). No deben haber usuario repetidos.

2. Los usuarios registrados pueden Iniciar Sesión en el sistema.

3. Cada usuario puede registrar varios contratos (servicios: agua, luz, gas, telefonía, etc.)

4. El administrador puede generar nuevas facturas a los usuarios registrados en cada uno de los contratos (servicios).

5. El usuario debe elegir un contrato y mostrar todas sus facturas históricas y mostrar las que no han sido pagadas de primero. Ordenar en por fecha.

6. Se debe poder cerrar sesión.

> [!NOTE] 
> 1. El rol del usuario debe tener una interfaz gráfica personalizada (Html, css y su propia programación). Ninguna de sus acciones se debe hacer desde el admin de Django.
>
> 2. El rol del administrador puede crear nuevas facturas desde el admin de django o también puede crear su propia interfaz gráfica.
>
> 3. El admin no puede eliminar un usuario si ya tiene contratos (servicios) registrado o con facturas pagas o pendientes por pagar.
>
> 4. No es obligatorio relacionar las tablas en su modelo, pero se recomienda.

Se entrega el proyecto en archivo comprimido en .zip o en link de repositorio en la nube público o libre. Usar sqlite3 que viene por defecto.

## Docente
Jorge Antonio García Cárdenas.

## Integrantes
- Sarah Murcia Prado([@sarah-mp](https://github.com/Juansecod)))
- Juan Sebastian Rios Valencia([@Juansecod](https://github.com/Juansecod))
- Sergio Vargas Marin([@](https://github.com/)))