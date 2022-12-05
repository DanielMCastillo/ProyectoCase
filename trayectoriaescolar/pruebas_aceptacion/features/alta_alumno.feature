Característica: Alta de un nuevo alumno
    Como administrador del sistema
    quiero dar de alta un alumno
    para tener control de los nuevos usuarios.

    Escenario: Datos correctos de alumno
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "jesus1234" y contra "Jesus.1234"
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "12345678", correo "alumno1@gmail.com"
            Y nombre "Nombre1", segundo nombre "Nombre2", primer apellido "primer_apellido", segundo apellido "segundo_apellido", telefono "1234567890"
            Y con los datos contraseña "Alumno.123" y confirmar "Alumno.123"
            Cuando oprimo el botón Guardar Alumno
            Entonces redirige a la url "http://localhost:8000/home"
        
    Escenario: Matricula corta
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "jesus1234" y contra "Jesus.1234"
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "123", correo "alumno1@gmail.com"
            Y nombre "Nombre1", segundo nombre "Nombre2", primer apellido "primer_apellido", segundo apellido "segundo_apellido", telefono "1234567890"
            Y con los datos contraseña "Alumno.123" y confirmar "Alumno.123"
            Cuando oprimo el botón Guardar Alumno
            Entonces me muestra el error "La matrícula debe contener exactamente 8 dígitos"

    Escenario: Matricula con una letra
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "jesus1234" y contra "Jesus.1234"
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "123abc78", correo "alumno1@gmail.com"
            Y nombre "Nombre1", segundo nombre "Nombre2", primer apellido "primer_apellido", segundo apellido "segundo_apellido", telefono "1234567890"
            Y con los datos contraseña "Alumno.123" y confirmar "Alumno.123"
            Cuando oprimo el botón Guardar Alumno
            Entonces me muestra el error "La matrícula debe contener solo números"

    Escenario: Contraseña sin formato pedido
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "jesus1234" y contra "Jesus.1234"
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "22345678", correo "alumno1@gmail.com"
            Y nombre "Nombre1", segundo nombre "Nombre2", primer apellido "primer_apellido", segundo apellido "segundo_apellido", telefono "1234567890"
            Y con los datos contraseña "Alumno" y confirmar "Alumno"
            Cuando oprimo el botón Guardar Alumno
            Entonces me muestra el error "La contraseña debe contener al menos 8 caracteres"