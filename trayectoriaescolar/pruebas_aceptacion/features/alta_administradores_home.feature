Característica: Alta de un nuevo administrador
    Como administrador del sistema
    quiero dar de alta un administrador
    para tener control de los nuevos usuarios.

        Escenario: Datos correctos de administrador
            Dado que entro a la url "http://127.0.0.1:8000/login"
            Y para iniciar sesión ingreso mis credenciales de usuario "jesus1234" y contraseña "Jesus.1234"
            Y luego me muevo a la url "http://127.0.0.1:8000/registro_admin_case"
            Y en el registro lleno los campos usuario "DanielitoXD", correo "danielitoxd@gmail.com"
            Y id_password "Daniel.123" y id_confirmar "Daniel.123"
            Cuando oprimo el botón Guardar Administrador
            Entonces redirige a la ruta "http://localhost:8000/home"

        Escenario: Administrador ya registrado
            Dado que entro a la url "http://127.0.0.1:8000/login"
            Y para iniciar sesión ingreso mis credenciales de usuario "jesus1234" y contraseña "Jesus.1234"
            Y luego me muevo a la url "http://127.0.0.1:8000/registro_admin_case"
            Y en el registro lleno los campos usuario "DanielitoXD", correo "danielitoxd@gmail.com"
            Y id_password "Daniel.123" y id_confirmar "Daniel.123"
            Cuando oprimo el botón Guardar Administrador
            Entonces muestra un mensaje de error "Ya existe un usuario con ese nombre."

        Escenario: Nombre de usuario incorrecto de administrador
            Dado que entro a la url "http://127.0.0.1:8000/login"
            Y para iniciar sesión ingreso mis credenciales de usuario "jesus1234" y contraseña "Jesus.1234"
            Y luego me muevo a la url "http://127.0.0.1:8000/registro_admin_case"
            Y en el registro lleno los campos usuario "aaa", correo "danielcastillo@gmail.com"
            Y id_password "Daniel.123" y id_confirmar "Daniel.123"
            Cuando oprimo el botón Guardar Administrador
            Entonces muestra un mensaje de error "El usuario debe contener 8 o mas caracteres"

        Escenario: Contraseña con menos de 8 caracteres
            Dado que entro a la url "http://127.0.0.1:8000/login"
            Y para iniciar sesión ingreso mis credenciales de usuario "jesus1234" y contraseña "Jesus.1234"
            Y luego me muevo a la url "http://127.0.0.1:8000/registro_admin_case"
            Y en el registro lleno los campos usuario "DanielAlejandroAdmin", correo "danielcastillo@gmail.com"
            Y id_password "Danie1." y id_confirmar "Danie1."
            Cuando oprimo el botón Guardar Administrador
            Entonces muestra un mensaje de error "La contraseña debe contener al menos 8 caracteres"
        
        Escenario: Contraseña sin formato adecuado en letras
            Dado que entro a la url "http://127.0.0.1:8000/login"
            Y para iniciar sesión ingreso mis credenciales de usuario "jesus1234" y contraseña "Jesus.1234"
            Y luego me muevo a la url "http://127.0.0.1:8000/registro_admin_case"
            Y en el registro lleno los campos usuario "DanielAlejandroAdmin", correo "danielcastillo@gmail.com"
            Y id_password "12345678" y id_confirmar "12345678"
            Cuando oprimo el botón Guardar Administrador
            Entonces muestra un mensaje de error "La contraseña debe contener al menos una letra"


        Escenario: Contraseña sin formato adecuado en letra mayuscula
            Dado que entro a la url "http://127.0.0.1:8000/login"
            Y para iniciar sesión ingreso mis credenciales de usuario "jesus1234" y contraseña "Jesus.1234"
            Y luego me muevo a la url "http://127.0.0.1:8000/registro_admin_case"
            Y en el registro lleno los campos usuario "DanielAlejandroAdmin", correo "danielcastillo@gmail.com"
            Y id_password "danielito1." y id_confirmar "danielito1."
            Cuando oprimo el botón Guardar Administrador
            Entonces muestra un mensaje de error "La contraseña debe contener al menos una letra mayuscula"
        
        Escenario: Contraseña sin formato adecuado en letra mayuscula
            Dado que entro a la url "http://127.0.0.1:8000/login"
            Y para iniciar sesión ingreso mis credenciales de usuario "jesus1234" y contraseña "Jesus.1234"
            Y luego me muevo a la url "http://127.0.0.1:8000/registro_admin_case"
            Y en el registro lleno los campos usuario "DanielAlejandroAdmin", correo "danielcastillo@gmail.com"
            Y id_password "DANIELITO1." y id_confirmar "DANIELITO1."
            Cuando oprimo el botón Guardar Administrador
            Entonces muestra un mensaje de error "La contraseña debe contener al menos una letra minuscula"