Característica: Login del sistema alumnos
    Como alumno de la UAZ
    Quiero entrar al sistema para consultar los servicios CASE
    Para poder solicitar los servicios que necesito

        Escenario: Credenciales válidas
            Dado que ingreso al portal de alumno "http://127.0.0.1:8000"
            Y escribo mi matricula "31122738" y contraseña "Ronaldinho999."
            Cuando le doy click al botón Ingresar
            Entonces puedo ver "SERVICIOS" en la página principal.
        
        Escenario: Credenciales invalidas
            Dado que ingreso al sistema en el dominio "http://127.0.0.1:8000"
            Y escribo mi matricula "31144556" y contraseña "Juan22"
            Cuando le doy click al botón Ingresar
            Entonces puedo ver un mensaje "Verifica tus datos de acceso."
        
        
