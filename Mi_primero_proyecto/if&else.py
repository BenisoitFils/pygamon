import datetime
now = datetime.datetime.now()
print(now.strftime('%Y %m %D %H:%M:%S'))

def pre(vl):
   cont = input(vl)
   return cont

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
    pre1 = pre( '\033[1m 1) La semana tienes 7 dias: \r\n Respuesta...')
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
        #pree == False
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
        #pree == False
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
        #pree == False
        print(otra)

total = nota1 + nota2 + nota3 +nota4

print(f'\033[1;41m La nota total de su examen es {total} %')
