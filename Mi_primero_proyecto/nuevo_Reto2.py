def ingresar_contraseña(valor):
    contr = input(valor)
    return contr

entrar = '1'
while entrar == '1':
    c1 = ingresar_contraseña('Ingrese contraseña: ')
    c2 = ingresar_contraseña('Repita su contraseña: ')
    if c1 == c2:
        print('Ok')
        entrar = 0
    else:
        entrar = input('Contraseñas no coinciden. Ingrese 0 si quiere salir: ')