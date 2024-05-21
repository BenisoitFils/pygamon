equivocado = 'Las contraseña no coinciden. Intentelo de nuevo. Para salir ingresa 0, 1 para continuar: '
listo ='Contraseña confirmada, hasta la vista'
log = input('Escriba tu nueva contraseña \r\n')
log1 = input('Confirmar tu contraseña \r\n')

while log == log1:
    print(listo)
    break
if log != log1:
    print(equivocado)








