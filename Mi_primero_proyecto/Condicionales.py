#2. Ingresar una nota e indicar si está Reprobado, Examen o Aprobado

nota = int(input('Ingrese nota (del 1 al 7): '))
if nota < 4 :
    print('Reprobado')
elif nota == 4:
    print('Examen')
elif nota < 7:
    print('Aprobado')
else:
    print('Ud ingreso una nota invalida')



#3. Ingresar una opción del 1 al 5, yo te diré que opción elegiste

opc = int(input('Ingrese opcion entre 1 y 5: '))
if opc == 1:
    print('Ud seleccionó la opción 1')
elif opc ==2:
    print('Ud seleccionó la opción 2')
elif opc ==3:
    print('Ud seleccionó la opción 3')
elif opc == 4:
    print('Ud seleccionó la opción 4')
else:
    print('Ud seleccionó la opción 5')