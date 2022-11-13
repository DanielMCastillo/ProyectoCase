Característica: Alta de un nuevo administrador
    Como administrador del sistema
    quiero dar de alta un administrador
    para tener control de los nuevos usuarios.

        Escenario: Datos correctos de administrador
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "Armandito",
            Y correo "admincase3@gmail.com", contraseña "Admincase123." y confirmar "Admincase123."
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
        
        Escenario: Contraseña incorrecta de registro
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de registro agrego los datos nombre "Armandito2",
            Y correo "admincase6@gmail.com", contraseña "aaa." y confirmar "aaa."
            Cuando presiono el botón Registrar
            Entonces puedo ver un mensaje de error "Ya existe un usuario con ese nombre."