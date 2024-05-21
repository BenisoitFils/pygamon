salir = 1
while salir != 0:
    print('Creado tu contraseña')
    log = input('Escriba tu nueva contraseña \r\n')
    log1 = input('Confirmar tu contraseña \r\n')
    if log == log1:
        print('Contraseña confirmada, hasta la vista')
        salir = 0
    else:
        print('Las contraseña no coinciden. Intentelo de nuevo.')
        salir = int(input('Para salir ingresa 0: '))
