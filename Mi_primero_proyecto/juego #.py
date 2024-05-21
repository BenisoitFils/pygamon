import datetime
now = datetime.datetime.now()
print(now.strftime(f'la fechia de hoy es %Y %m %d \r\n y la hora de hoy es %H:%M:%S'))

pre = 'agregar numero y te dire si par o impar  \r\n'
pre += 'para salir escribe "cerrar" \r\n'
pre1 = True

while pre1:
    #melange let ak chif
    numero = input(pre)
    if numero == 'cerrar':
        pre1 = False
    else:
        #conveti en chif
        numero = int(numero)
        if numero %2 == 0:
            print(f'el numero {numero} es par')
        else:
            print(f'el numero {numero} es impar')



