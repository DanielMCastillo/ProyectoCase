Característica: Alta de un nuevo alumno
    Como administrador del sistema
    quiero dar de alta un alumno
    para tener control de los nuevos usuarios.

    Escenario: Datos correctos de alumno
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31122878", correo "danielalejandromoralescastillo@gmail.com"
            Y nombre "Daniel", segundo nombre "Alejandro", primer apellido "Morales", segundo apellido "Castillo", telefono "4922190147"
            Y con los datos contraseña "Daniel123." y confirmar "Daniel123."
            Cuando oprimo el botón Guardar Alumno
            Entonces redirige a la url "http://localhost:8000/home"

    
    Escenario: Usuario ya registrado
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31122878", correo "danielalejandromoralescastillo@gmail.com"
            Y nombre "Daniel", segundo nombre "Alejandro", primer apellido "Morales", segundo apellido "Castillo", telefono "4922190147"
            Y con los datos contraseña "Daniel123." y confirmar "Daniel123."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "Ya existe un usuario con ese nombre."
    
    Escenario: Matricula corta
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "123", correo "alumno1@gmail.com"
            Y nombre "Jesus", segundo nombre "Manuel", primer apellido "Juarez", segundo apellido "Pasillas", telefono "4921337599"
            Y con los datos contraseña "Alumno.123" y confirmar "Alumno.123"
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "La matrícula debe contener exactamente 8 dígitos"

    Escenario: Matricula con letras
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "123abc78", correo "alumno1@gmail.com"
            Y nombre "Armando", segundo nombre "Alejandro", primer apellido "Robles", segundo apellido "Perez", telefono "4921456787"
            Y con los datos contraseña "Armando1." y confirmar "Armando1."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "La matrícula debe contener solo números"
    
    Escenario: Contraseña sin el formato correcto en caracteres
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145678", correo "juanito32@gmail.com"
            Y nombre "Juan", segundo nombre "Manuel", primer apellido "Marquez", segundo apellido "Lopez", telefono "4921456789"
            Y con los datos contraseña "Juanito" y confirmar "Juanito"
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "La contraseña debe contener al menos 8 caracteres"

    Escenario: Contraseña sin el formato correcto caracter especial
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145678", correo "juanito32@gmail.com"
            Y nombre "Juan", segundo nombre "Manuel", primer apellido "Marquez", segundo apellido "Lopez", telefono "4921456789"
            Y con los datos contraseña "Juanitoo" y confirmar "Juanitoo"
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "La contraseña debe contener al menos un caracter especial"
    
    Escenario: Contraseña sin el formato correcto letra mayuscula
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145679", correo "juanito32@gmail.com"
            Y nombre "Juan", segundo nombre "Manuel", primer apellido "Ramirez", segundo apellido "Lopez", telefono "4921456790"
            Y con los datos contraseña "juanitoo1." y confirmar "juanitoo1."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "La contraseña debe contener al menos una letra mayuscula"
        
    Escenario: Contraseña sin el formato correcto letra minuscula
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145679", correo "juanito32@gmail.com"
            Y nombre "Juan", segundo nombre "Manuel", primer apellido "Ramirez", segundo apellido "Lopez", telefono "4921456790"
            Y con los datos contraseña "JUANITOO1." y confirmar "JUANITOO1."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "La contraseña debe contener al menos una letra minuscula"
    
    Escenario: Campo Matricula obligatorio
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "", correo "juanito32@gmail.com"
            Y nombre "Juan", segundo nombre "Manuel", primer apellido "Ramirez", segundo apellido "Lopez", telefono "4921456790"
            Y con los datos contraseña "Juanito1." y confirmar "Juanito1."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "Este campo es obligatorio."

    Escenario: Campo Nombre obligatorio
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145680", correo "juanito32@gmail.com"
            Y nombre "", segundo nombre "Manuel", primer apellido "Ramirez", segundo apellido "Lopez", telefono "4921456790"
            Y con los datos contraseña "Manuelito1." y confirmar "Manuelito1."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "Este campo es obligatorio."

    Escenario: Campo Apellido Materno obligatorio
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145680", correo "danielito32@gmail.com"
            Y nombre "Daniel", segundo nombre "Alejandro", primer apellido "Mendez", segundo apellido "Lopez", telefono "4921456791"
            Y con los datos contraseña "Danielito2." y confirmar "Danielito2."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "Este campo es obligatorio."
    
    Escenario: Campo Apellido Paterno obligatorio
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145680", correo "danielito32@gmail.com"
            Y nombre "Daniel", segundo nombre "Alejandro", primer apellido "", segundo apellido "Lopez", telefono "4921456791"
            Y con los datos contraseña "Danielito2." y confirmar "Danielito2."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "Este campo es obligatorio."
    
    Escenario: Campo contraseña obligatorio
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145680", correo ""
            Y nombre "Daniel", segundo nombre "Alejandro", primer apellido "Mendez", segundo apellido "Lopez", telefono "4921456791"
            Y con los datos contraseña "" y confirmar "Danielito2."
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "Este campo es obligatorio."

    Escenario: Campo repetir contraseña obligatorio
            Dado que me dirijo a la url "http://localhost:8000/login"
            Y para iniciar sesión ingreso los datos "amcdanymx" y contra "Ronaldinho999."
            Y luego me dirijo a la url "http://localhost:8000/registro_alumno"
            Y en el registro agrego los datos matricula "31145680", correo ""
            Y nombre "Daniel", segundo nombre "Alejandro", primer apellido "Mendez", segundo apellido "Lopez", telefono "4921456791"
            Y con los datos contraseña "Danielito2." y confirmar ""
            Cuando oprimo el botón Guardar Alumno
            Entonces muestra un mensaje de error "Este campo es obligatorio."