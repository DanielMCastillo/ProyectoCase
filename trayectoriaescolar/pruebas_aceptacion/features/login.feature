Característica: Login del sistema
    Como usuario del sistema
    Quiero entrar al sistema para realizar mi trabajo diario
    Para que me paguen

        Escenario: Credenciales válidas
            Dado que ingreso al sistema en el dominio "http://127.0.0.1:8000/login"
            Y escribo mi usuario "amcdanymx" y contraseña "Ronaldinho999."
            Cuando presiono el botón Ingresar
            Entonces puedo ver mi nombre de usuario "amcdanymx" en la página principal.
        
        
        Escenario: Credenciales invalidas
            Dado que ingreso al sistema en el dominio "http://127.0.0.1:8000/login"
            Y escribo mi usuario "amcdanymx" y contraseña "Juan22"
            Cuando presiono el botón Ingresar
            Entonces puedo ver el mensaje "Verifica tus datos de acceso."
        
        
