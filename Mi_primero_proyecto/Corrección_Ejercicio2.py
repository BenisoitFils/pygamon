#     Generar una pequeña aplicación que tenga un menú, para que la persona elija la opción que necesita.
#     El menú debe tener las siguientes opciones.
# 1.  Sumar
# 2.  Restar
# 3.  Multiplicar
# 4.  Dividir
# 5.  Numero es par o impar
# 6.  Número es multiplo de 3 o 5
# 7.  Número es multiplo de 3 y 5
# 8.  Factorial de número
# 9.  Volumen de un cubo
# 10. Prueba tiennen 4 preguntas contestar por si o no
# 11. Para saber cuanto dia de un año al otro
# 12. Salir del menú.
#     Se debe pedir dos números para las opciones del 1 al 4 y solo 1 para las opciones 5 a la 8.
#from datetime import date

#f_date = date(2014, 7, 2)
#l_date = date(2023, 7, 11)
#delta = l_date - f_date
#print(delta.days)
import datetime

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print('bienvenido en el programa HERCULES\r\n MENÚ: \r\n1. Sumar 2. Restar 3. Multiplicar '
                      '4. Dividir 5. Numero es par o impar '
                      '6. Número es multiplo de 3 o 5\r\n'
                      '7. Número es multiplo de 3 y 5 '
                      '8. Factorial de número '
                      '9. Volumen en metros cubo '
                      '10. Prueba '
                      '11. Controlador del dia '
                      '12. Para saber area del rectangulo '
                      '13. Salir del applicación.\r\n')

def entre_menu():
    while True:
        try:
            menu = float(input(f' Porfavor ingresar el número del opción\r\n '))
            if menu >= 14:
                print('Error 0x0001 : el menu tienen 12 opciones,tu debes eligir de 1 a 12')
            return menu
            break
        except ValueError:
            print("Oops! error 0x0002 los opciónes no son de type'str' entantarlo de nuevo")


def innum(num):
    while True:
        try:
            savenum = float(input(num))
            return savenum
            break
        except ValueError:
            print("Oops ! error 0x0003 Los número son de 0 a 9  ")


def factorial(valor):
    if valor == 1:
        return 1
    else:
        return valor * factorial(valor - 1)

def pre(vl):
   cont = input(vl)
   return cont

option = 1

while option != 13:


    option = entre_menu()

    if option == 1:
        innum1 = innum('agregar primero numero para sumar \r\n')
        innum2 = innum('agregar segundo numero para sumar \r\n')
        suma = innum1
        suma += innum2
        print(f'la suma de los 2 numeros son: {suma : .2F} \r\n')

    if option == 2:
        innum1 = innum('agregar primero numero para restar \r\n')
        innum2 = innum('agregar segundo numero para restar \r\n')
        diferencia = innum1
        diferencia -= innum2
        print(f'la restar de los 2 numeros son: {diferencia} \r\n')

    if option == 3:
        innum1 = innum('agregar primero numero para multiplicar \r\n')
        innum2 = innum('agregar segundo numero para multiplicar \r\n')
        producto = innum1
        producto *= innum2
        print(f'el producto de los 2 numeros son: {producto : .2F} \r\n')

    if option == 4:
        while True:
            try:
                innum1 = innum('agregar primero numero para dividir \r\n')
                innum2 = innum('agregar segundo numero para dividir \r\n')
                cociente = innum1
                cociente /= innum2
                print(f'la  division de los 2 numeros son {cociente} \r\n')
                break
            except ZeroDivisionError:
                print("Oops ! Error 0x0004 No se puede con 0")

    if option == 5:
        innum1 = innum('agregar el unico numero para saber si es par o impar \r\n')
        if innum1 % 2 == 0:
            print('el numero es par')
        else:
            print('el numero es par')
    if option == 6:
        innum1 = innum('agregar el unico numero para saber si es multiplo de 3 o 5 \r\n')
        if innum1 % 3 == 0 or innum1 % 5 == 0:
            print('el numero es multiplo de 3 o 5')
        else:
            print('el numero no es multiplo de 3 o 5')

    if option == 7:
        innum1 = innum('agregar el unico numero para saber si es multiplo de 3 y 5 \r\n')
        if innum1 % 3 == 0 and innum1 % 5 == 0:
            print('el numero es multiplo de 3 y 5')
        else:
            print('el numero no es multiplo de 3 y 5')

    if option == 8:
        while True:
            try:
                valor = float(input('agregar el unico numero para saber su factorial\r\n'))
                print(f'el facttorial es: {factorial(valor):.2f}')
                break
            except ValueError:
                print("Oops ! error 0x0003 Los número son de 0 a 9  ")

    if option == 9:
        print('N.B: Para saber el volumen de un cubo tu debes ingresar el ancho el alto al final el profundo ')
        while True:
            try:
                ancho = float(input('agregar el ancho\r\n'))
                alto = float(input('agregar el alto\r\n'))
                profundo = float(input('agregar el profundo\r\n'))
                volumen = ancho * alto * profundo
                print(f'el volumen es: {volumen} metros cúbicos')
                break
            except ValueError:
                print("Oops ! error 0x0005 Los número son de 0 a 9")

    if option == 10:
        print('La pueba del anño 2023 tienen 4 preguntas cada uno a 25 puntos...contestar por si on no')

        pos = 'Bien hecho tienes 25 puntos eres muy inteligente buena suerte'
        neg = 'Respuesta incorrecta has perdido 25 puntos por ser estúpido (a)'
        otra = 'Tu debes contestar por si o no borrico idiota '
        pree = True
        nota1 = 0
        nota2 = 0
        nota3 = 0
        nota4 = 0

        while pree:
            pre1 = pre('\033[1m 1) La semana tienes 7 dias: \r\n Respuesta...')
            if pre1 == 'si':
                nota1 = 25
                print(pos)
                break
            elif pre1 == 'no':
                print(neg)
                break
            else:
                print(otra)

        while pree:
            pre2 = pre('\033[1m 2) Sumar de 27 + 11 = 37: \r\n Respuesta...')
            if pre2 == 'no':
                nota2 = 25
                print(pos)
                break
            elif pre2 == 'si':
                print(neg)
                break
            else:
                # pree == False
                print(otra)

        while pree:
            pre3 = pre('\033[1m 3) Paulina es la mujer mas bonita del mundo: \r\n Respuesta...')
            if pre3 == 'si':
                nota3 = 25
                print(pos)
                break
            elif pre3 == 'no':
                print(neg)
                break
            else:
                # pree == False
                print(otra)

        while pree:
            pre4 = pre('\033[1m 4) esc es la primera button del tecla: \r\n Respuesta...')
            if pre4 == 'si':
                nota4 = 25
                print(pos)
                break
            elif pre4 == 'no':
                print(neg)
                break
            else:
                # pree == False
                print(otra)

        total = nota1 + nota2 + nota3 + nota4

        print(f' La nota total de su examen es: {total} % LA FECHIA: {now.strftime("%Y-%m-%d %H:%M:%S")}')

    if option == 11:
        print('N.B: Para saber la cantidad de los dia tu debes ingresar las fechias pasada luego la otras')
        from datetime import date
        while True:
            try:
                f_date = date(year=int(input('Ingresar el año pasado\r\n')),month=int(input('Ingresar el mes pasado\r\n')),
                              day=int(input('Ingresar el dia pasado\r\n')))
                l_date = date(year=int(input('Ingresar el nuevo año\r\n')),month=int(input('Ingresar el nuevo mes\r\n')),
                              day=int(input('Ingresar el nuevo dia\r\n')))
                delta = l_date - f_date
                print(f' La cantidades de los dias son: {delta.days}')
                break
            except ValueError:
                print("Oops ! Error 0x0006 leer bien anter de ingresar  Las informationes")

    if option == 12:
        base = innum('Ingresar la base del rectangulo \r\n')
        altura = innum('Ingresar la altura del rectangulo\r\n')
        area = base
        area *= altura
        print(f'Área del rectángulo es: {area}\r\n')

    if option == 13:
        print('Hasta la vista')
