Característica: Alta de un nuevo administrador
    Como administrador del sistema
    quiero dar de alta un administrador
    para tener control de los nuevos usuarios.

        Escenario: Datos correctos de administrador
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "jesussss",
            Y correo "jesussss@gmail.com", contraseña "Jesus123." y confirmar "Jesus123."
            Cuando presiono el botón Registrar
            Entonces la página me manda a la url "http://localhost:8000/entrar"

        Escenario: Nombre de usuario incorrecto de administrador
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "Arm",
            Y correo "admincase4@gmail.com", contraseña "Admincase123." y confirmar "Admincase123."
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "username" y "El usuario debe contener 8 o mas caracteres"
        
        Escenario: Nombre administrador repetido
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "Armandito",
            Y correo "admincase5@gmail.com", contraseña "Admincase123." y confirmar "Admincase123."
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "Ya existe un usuario con ese nombre."
        
        Escenario: Contraseña con menos de 8 caracteres
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "Avelardo",
            Y correo "avelardo@gmail.com", contraseña "avel" y confirmar "avel"
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "La contraseña debe contener al menos 8 caracteres"

        Escenario: Contraseña con menos de 8 caracteres
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "Avelardo",
            Y correo "avelardo@gmail.com", contraseña "12345678" y confirmar "12345678"
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "La contraseña debe contener al menos una letra"

        Escenario: Contraseña con menos de 8 caracteres
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "Avelardo",
            Y correo "avelardo@gmail.com", contraseña "avelardo" y confirmar "avelardo"
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "La contraseña debe contener al menos una letra mayuscula"

        Escenario: Contraseña con menos de 8 caracteres
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "Avelardo",
            Y correo "avelardo@gmail.com", contraseña "Avelardo" y confirmar "Avelardo"
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "La contraseña debe contener al menos un caracter especial"