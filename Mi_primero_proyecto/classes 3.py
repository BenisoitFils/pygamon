import datetime
now = datetime.datetime.now()
print(now.strftime('%Y %M %D %H:%M:%S'))

class Vehiculo:
    def __init__(self,nombre,categoria,marca,ano,color):
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.ano = ano
        self.color = color
    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, categoria: {self.categoria}, marca: {self.marca}, ano: {self.ano}, color: {self.color}')


vehiculo = Vehiculo('Nissan', 'Jeep', 'Xterra', 2008, 'Rojo')
vehiculo.mostrar_info()
vehiculo2 = Vehiculo('Toyota', 'Pickup', 'Tacoma', 2005, 'Azul')
vehiculo2.mostrar_info()


txt = "Hello World"
x = txt[2:5]

print(x)


txt = " Hello World "
x = txt.strip()
print(x)


txt = "Hello World"
txt = txt.upper()
print(x)


age = 36
año = 30
txt = "My name is John, and I am {} {}"
print(txt.format(age, año))


