Característica: Alta de un nuevo artículo
    Como administrador del sistema
    quiero dar de alta un artículo
    para contar con un invenario actualizado.

        Escenario: Datos correctos de administrador
            Dado que ingreso a la url "http://localhost:8000/registrar"
            Y en la sección de nombre de usuario agregó los datos nombre del administrador "AdminCase2",
            Y correo electronico  "admincase2@gmail.com", contraseña "AdminCase2123.", confirmar "AdminCase2123"
            Cuando presiono el botón "Registrar"
            Entonces puedo ver el mensaje de salida "se registró de manera exitosa."

