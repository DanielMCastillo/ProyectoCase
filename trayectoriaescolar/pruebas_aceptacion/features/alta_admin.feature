Característica: Alta de un nuevo administrador
    Como administrador del sistema
    quiero dar de alta un administrador
    para tener control de los nuevos usuarios.

        Escenario: Datos correctos de administrador
            Dado que ingreso a la url "http://127.0.0.1:8000/login"
            Y en la sección de inicio de sesión agrego los datos "jesus1234" y contra "Jesus.1234"
            Y luego ingreso a la url "http://127.0.0.1:8000/registro_de_administrador"
            Y en la sección de registro agrego los datos nombre "jesusss",
            Y correo "jesusss@gmail.com", contraseña "Jesus.123" y confirmar "Jesus.123"
            Cuando presiono el botón Registrar
            Entonces la página me manda a la url "http://127.0.0.1:8000/login"

        Escenario: Nombre de usuario incorrecto de administrador
            Dado que ingreso a la url "http://127.0.0.1:8000/login"
            Y en la sección de inicio de sesión agrego los datos "jesus1234" y contra "Jesus.1234"
            Y luego ingreso a la url "http://127.0.0.1:8000/registro_de_administrador"
            Y en la sección de registro agrego los datos nombre "Arm",
            Y correo "admincase4@gmail.com", contraseña "Admincase123." y confirmar "Admincase123."
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "username" y "El usuario debe contener 8 o mas caracteres"
        
        Escenario: Nombre administrador repetido
            Dado que ingreso a la url "http://127.0.0.1:8000/login"
            Y en la sección de inicio de sesión agrego los datos "jesus1234" y contra "Jesus.1234"
            Y luego ingreso a la url "http://127.0.0.1:8000/registro_de_administrador"
            Y en la sección de registro agrego los datos nombre "Armandito",
            Y correo "admincase5@gmail.com", contraseña "Admincase123." y confirmar "Admincase123."
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "Ya existe un usuario con ese nombre."
        
        Escenario: Contraseña con menos de 8 caracteres
            Dado que ingreso a la url "http://127.0.0.1:8000/login"
            Y en la sección de inicio de sesión agrego los datos "jesus1234" y contra "Jesus.1234"
            Y luego ingreso a la url "http://127.0.0.1:8000/registro_de_administrador"
            Y en la sección de registro agrego los datos nombre "Avelardo",
            Y correo "avelardo@gmail.com", contraseña "avel" y confirmar "avel"
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "La contraseña debe contener al menos 8 caracteres"

        Escenario: Contraseña sin letras
            Dado que ingreso a la url "http://127.0.0.1:8000/login"
            Y en la sección de inicio de sesión agrego los datos "jesus1234" y contra "Jesus.1234"
            Y luego ingreso a la url "http://127.0.0.1:8000/registro_de_administrador"
            Y en la sección de registro agrego los datos nombre "Avelardo",
            Y correo "avelardo@gmail.com", contraseña "12345678" y confirmar "12345678"
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "La contraseña debe contener al menos una letra"

        Escenario: Contraseña sin numeros
            Dado que ingreso a la url "http://127.0.0.1:8000/login"
            Y en la sección de inicio de sesión agrego los datos "jesus1234" y contra "Jesus.1234"
            Y luego ingreso a la url "http://127.0.0.1:8000/registro_de_administrador"
            Y en la sección de registro agrego los datos nombre "Avelardo",
            Y correo "avelardo@gmail.com", contraseña "avelardo" y confirmar "avelardo"
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "La contraseña debe contener al menos una letra mayuscula"

        Escenario: Contraseña sin caracteres especiales
            Dado que ingreso a la url "http://127.0.0.1:8000/login"
            Y en la sección de inicio de sesión agrego los datos "jesus1234" y contra "Jesus.1234"
            Y luego ingreso a la url "http://127.0.0.1:8000/registro_de_administrador"
            Y en la sección de registro agrego los datos nombre "Avelardo",
            Y correo "avelardo@gmail.com", contraseña "Avelardo" y confirmar "Avelardo"
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "La contraseña debe contener al menos un caracter especial"