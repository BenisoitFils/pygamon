class Vehiculo:

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: '+ self.color +', Ruedas: ' + str(self.ruedas)

class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+',Velocidad (km/h):'+str(self.velocidad)

class Bicicleta(Vehiculo):

    def __init__(self,color,ruedas,tipo):
        super(Bicicleta, self).__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return super(Bicicleta, self).__str__() +',Tipo :'+self.tipo

# creamos un objeto de la clase Vehiculo
vehiculo = Vehiculo('rojo ',4)
print(vehiculo)

# creamos un objeto de la clase hija Coche
coche = Coche('azul ',4,150)
print(coche)

# creamos un objeto de la clase hija Bicicleta
bicicleta = Bicicleta('blanca ',2 ,'urbano')
print(bicicleta)