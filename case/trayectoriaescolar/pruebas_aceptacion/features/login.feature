Característica: Login del sistema
    Como usuario del sistema
    Quiero entrar al sistema para realizar mi trabajo diario
    Para que me paguen

        Escenario: Credenciales válidas
            Dado que ingreso al sistema en el dominio "http://localhost:8000/"
            Y escribo mi usuario "Caseadmin" y contraseña "Case123."
            Cuando presiono el botón Ingresar
            Entonces puedo ver mi nombre de usuario "Caseadmin" en la página principal

        Escenario: Credenciales invalidas
            Dado que ingreso al sistema en el dominio "http://localhost:8000/"
            Y escribo mi usuario "Caseadmin2" y contraseña "caseadmin1234"
            Cuando presiono el botón Ingresar
            Entonces puedo ver el mensaje "Verifica tus datos de acceso."
