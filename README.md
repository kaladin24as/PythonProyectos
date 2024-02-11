# Sistema de gestión, versión 0.1

## Componentes del proyecto

### Interfaz de Usuario (UI)
La parte visual del proyecto está hecha con archivos .ui generados en Qt Designer y luego convertidos a código Python con PyQt6. Hay varias ventanas que permiten al usuario interactuar con el sistema, desde el inicio de sesión hasta la realización de transacciones.

### Clases de Datos (Data Classes)
Estas clases manejan la interacción con la base de datos SQLite, desde la creación de tablas hasta la inserción y consulta de datos. Tenemos clases para usuarios, depósitos, transferencias y también una para la lista de países.

### Modelos de Datos (Data Models)
Representan los objetos que usamos en la aplicación, como Usuarios, Depósitos y Transferencias.

### Conexión a la Base de Datos
Una clase que establece la conexión con SQLite y crea las tablas necesarias.

### Clase Principal y Ejecución
Una clase que inicia la aplicación y muestra la ventana de inicio de sesión.

## Funcionalidades principales

- **Inicio de Sesión**: Los usuarios pueden ingresar con su nombre de usuario y contraseña.
- **Registro de Usuarios**: Se pueden crear nuevas cuentas de usuario.
- **Depósitos**: Los usuarios pueden agregar fondos a sus cuentas.
- **Transferencias**: Permiten enviar dinero entre cuentas bancarias.

## Consideraciones técnicas

- Utilizamos el patrón Modelo-Vista-Controlador (MVC) para organizar nuestro código.
- La base de datos SQLite nos brinda portabilidad y facilidad de mantenimiento.
- PyQt6 nos ayuda a crear una interfaz amigable.

## Posibles Mejoras

- Mejorar la apariencia de la interfaz.
- Encriptar las contraseñas para mayor seguridad.
- Agregar funciones avanzadas como transferencias internacionales.
- Validar los datos de entrada de forma más robusta.
- Implementar un sistema de registro de auditoría.

## Lecciones Aprendidas

- Aprender sobre interfaces gráficas con PyQt6.
- Experiencia en desarrollo de aplicaciones con Python y SQLite.
- Entender el patrón MVC para una arquitectura de software sólida.
- Buenas prácticas de seguridad en la gestión de contraseñas y protección contra ataques SQL.
- Importancia de pruebas y depuración para un sistema confiable.

## Vulnerabilidad a Inyección SQL

Hemos identificado una posible vulnerabilidad en el método de inicio de sesión debido a la construcción de consultas SQL sin parámetros. 


