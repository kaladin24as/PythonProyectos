# PythonProyectos

---

# <span style="color:red">Sistema de Gestión, VERSION 0.1</span>

El proyecto consiste en el desarrollo de un Sistema de Gestión Bancaria utilizando el lenguaje de programación Python y la biblioteca PyQt6 para la interfaz gráfica de usuario (GUI). El objetivo principal del sistema es proporcionar funcionalidades básicas para la gestión de usuarios, depósitos y transferencias dentro de un banco.

## Componentes del proyecto

### Interfaz de Usuario (UI)
La interfaz de usuario se implementa utilizando archivos .ui que se crean con la herramienta Qt Designer y se convierten a código Python utilizando el módulo uic de PyQt6. La interfaz consta de varias ventanas que permiten al usuario acceder al sistema, registrar usuarios, realizar transferencias y realizar depósitos.

### Clases de Datos (Data Classes)
Estas clases se encargan de interactuar con la base de datos SQLite para realizar operaciones como la creación de tablas, inserción de datos y consultas. Incluye las siguientes clases:
- **UsuarioData**: Gestiona la creación y autenticación de usuarios.
- **DepositoData**: Administra los depósitos realizados por los usuarios.
- **TransferenciaData**: Gestiona las transferencias de fondos entre cuentas.
- **PaisesData**: Proporciona la lista de países para su selección en el formulario de depósito.

### Modelos de Datos (Data Models)
Estas clases representan los objetos de datos utilizados en la aplicación. Incluye los modelos `Usuario`, `Deposito` y `Transferencia`.

### Conexión a la Base de Datos
La clase `Conexion` se encarga de establecer la conexión con la base de datos SQLite y crear las tablas necesarias en caso de que no existan.

### Clase Principal y Ejecución
La clase `Banco` inicializa la aplicación PyQt6 y muestra la ventana de inicio de sesión (`Login`). Desde aquí, los usuarios pueden acceder al sistema y realizar diferentes operaciones bancarias.

## Funcionalidades principales

- **Inicio de Sesión**: Los usuarios pueden iniciar sesión utilizando un nombre de usuario y una contraseña. Se valida la autenticidad de las credenciales ingresadas antes de permitir el acceso al sistema.
- **Registro de Usuarios**: Los usuarios pueden registrarse en el sistema proporcionando un nombre de usuario único y una contraseña.
- **Registro de Depósitos**: Los usuarios pueden realizar depósitos de fondos en sus cuentas bancarias, especificando el monto, tipo de documento, motivo, entre otros datos relevantes.
- **Registro de Transferencias**: Los usuarios pueden transferir fondos entre cuentas bancarias, especificando el monto, tipo de documento, motivo, entre otros datos relevantes.

## Consideraciones técnicas

- El proyecto utiliza el patrón de diseño Modelo-Vista-Controlador (MVC) para separar la lógica de la aplicación de la interfaz de usuario.
- Se implementa una base de datos SQLite para el almacenamiento de datos, lo que facilita la portabilidad y el mantenimiento del sistema.
- La aplicación utiliza PyQt6 para la creación de la interfaz gráfica de usuario, lo que permite una experiencia de usuario intuitiva y amigable.

## Posibles Mejoras

- Mejorar la apariencia de las interfaces, para hacerlas mas amigables.
- Implementar encriptación de contraseñas para mayor seguridad.
- Agregar funcionalidades avanzadas como transferencias internacionales y pago de servicios.
- Mejorar la validación de datos en formularios para una experiencia de usuario más robusta.
- Implementar un sistema de registro de auditoría para el seguimiento de acciones realizadas por los usuarios.
- Integrar un sistema de notificaciones para informar a los usuarios sobre eventos importantes.

## Lecciones Aprendidas

- Aprendizaje sobre el diseño de interfaces gráficas de usuario utilizando PyQt6.
- Experiencia en el desarrollo de aplicaciones de gestión utilizando Python y SQLite.
- Comprensión de patrones de diseño como Modelo-Vista-Controlador (MVC) para una arquitectura de software escalable y mantenible.
- Conocimiento adquirido sobre buenas prácticas de seguridad, como la gestión adecuada de contraseñas y la protección contra inyecciones de SQL.
- Experiencia en la implementación de pruebas de unidad y depuración para garantizar el correcto funcionamiento del sistema.

