import datetime
now = datetime.datetime.now()
print(now.strftime('%Y %M %D  %H:%M:%S'))
def marca(nombre,precio = '0',cantidad = 'no hay'):
    print(f'soy {nombre} mi costo {precio} y {cantidad}')
marca('puma',500,'100')
marca('nike',900,76)
marca('air',700)
marca('jordan',750)
marca('supra',469)
marca('tommy',)
# Bool true or false
dinero = True
producto = True
if dinero and producto:
    print('puedes comprar')
elif dinero or producto:
    print('falta uno de los dos')
else:
    print('no puede comprar')

#dic bagay male
Paulinainfo = {
    'nombreCompleto':'Paulina Valenzuela', #llave y valor
    'edad':'40 años',
    'nacionalidad':'Chilena',
    'idioma':'Espagnol y Ingles',
    'conocimiento':'Sabes mucho',
    'su vida':'Hercules'
}
print(Paulinainfo)
#base de donne
nombre = input('cual es tu nombre: \r\n')
print(f'hola {nombre}')
edad = input('cual es tu edad: \r\n')
#convertir edad en chif
edad = int(edad)
if edad >= 18:
    print('puedes entrar')
else:
    print('menor prohibido')

numero = input('añadir cualquier numero y te dire si es par o impar \r\n')
numero = int(numero)
if numero % 2 == 0:
    print(f'el numero {numero} es par')
else:
    print(f'el numero {numero} es impar')
