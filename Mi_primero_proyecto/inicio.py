def Comida(Nombre,Precio,Cantidad):
    return Nombre,Precio,Cantidad

def mostrar_nombre_completo(n,a):
    return n,a


Cereal = Comida('Cornflaks',200,111)
print(f'hay {Cereal[0]} que cuestan {Cereal[1]} pesos y tenemos {Cereal[2]} unidades')
nombre = 'Paulina'
apelli = 'Valenzuela'

nombre_completo = mostrar_nombre_completo('Paulina','Valenzuela')
print(nombre_completo[0])

def montrar_nombre(nombre, apellido):
    return f'te amo {nombre} , {apellido}'
print(montrar_nombre(nombre,apelli))