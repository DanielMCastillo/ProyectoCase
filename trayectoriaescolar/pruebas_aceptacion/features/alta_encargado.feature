Característica: Alta de un nuevo responsable
    Como administrador del sistema
    quiero dar de alta un responsable
    para tener control de los nuevos usuarios.

    Escenario: Datos correctos de responsable
            Dado que me meto a la url "http://localhost:8000/login"
            Y en la sección de inicio de sesión ingreso los datos "jesus1234" y contra "Jesus.1234"
            Y luego me meto a la url "http://localhost:8000/registro_responsable"
            Y en el registro agrego los datos usuario "responsabla", correo "responsable1@gmail.com"
            Y nombre "Nombre1", segundo nombre "Nombre2", primer apellido "primer_apellido", segundo apellido "segundo_apellido", programa academico "Programa1", unidad academica "Unidad1"
            Y contraseña "Respon.123" y confirmar "Respon.123"
            Cuando oprimo el botón Guardar Responsable
            Entonces la página me envia a la url "http://localhost:8000/home"
        
    Escenario: Nombre de usuario corto
            Dado que me meto a la url "http://localhost:8000/login"
            Y en la sección de inicio de sesión ingreso los datos "jesus1234" y contra "Jesus.1234"
            Y luego me meto a la url "http://localhost:8000/registro_responsable"
            Y en el registro agrego los datos usuario "res", correo "responsable1@gmail.com"
            Y nombre "Nombre1", segundo nombre "Nombre2", primer apellido "primer_apellido", segundo apellido "segundo_apellido", programa academico "Programa1", unidad academica "Unidad1"
            Y contraseña "Respon.123" y confirmar "Respon.123"
            Cuando oprimo el botón Guardar Responsable
            Entonces puedo ver el error "El usuario debe contener 8 o mas caracteres"

    Escenario: contraseña de usuario sin formato pedido
            Dado que me meto a la url "http://localhost:8000/login"
            Y en la sección de inicio de sesión ingreso los datos "jesus1234" y contra "Jesus.1234"
            Y luego me meto a la url "http://localhost:8000/registro_responsable"
            Y en el registro agrego los datos usuario "responsabl", correo "responsable1@gmail.com"
            Y nombre "Nombre1", segundo nombre "Nombre2", primer apellido "primer_apellido", segundo apellido "segundo_apellido", programa academico "Programa1", unidad academica "Unidad1"
            Y contraseña "Respon" y confirmar "Respon"
            Cuando oprimo el botón Guardar Responsable
            Entonces puedo ver el error "La contraseña debe contener al menos 8 caracteres"