print('USER LOGIN NASA')
def solicitarContrasena(texto):
    contrasenaDelUsuario = input(texto)
    return contrasenaDelUsuario

def validarContrasena(contrasena, repetirContrasena):
    estadoContrasena = ""
    if contrasena == repetirContrasena:
        estadoContrasena = 'Ok'
    else:
        estadoContrasena = 'No coinciden'
    return print(estadoContrasena)


contrasena = solicitarContrasena('Ingresar nueva contraseña \r\n')
repetirContrasena = solicitarContrasena('Confirmar contraseña \r\n')

validarContrasena(contrasena,repetirContrasena)




