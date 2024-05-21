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
import datetime

now = datetime.datetime.now()
print(now.strftime('%Y,%M,%D  %H:%M:%S'))

print('1. Sumar 2. Restar 3. Multiplicar '
                               '4. Dividir 5. Numero es par o impar '
                               '6. Número es multiplo de 3 o 5\r\n'
                               '7. Número es multiplo de 3 y 5 '
                               '8. Factorial de número '
                               '9. Volumen en metros cubo '
                               '10. Prueba '
                               '11. Controlador del dia '
                               '12. Para saber area del rectangulo '
                               '13. Salir del menú.\r\n')

class Menu:
    def __init__(self):
        self.menu = float(input('eligir tu opcion'))




    def operacion(self):
        if menu == 1:
            pass
        return self.menu




menu = Menu()
print( menu.operacion())



