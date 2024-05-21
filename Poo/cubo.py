class Cubo:
    def __init__(self,ancho,alto,profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcul_volumen(self):
        return self.ancho * self.alto * self.profundo

ancho = float(input('ancho'))
alto = float(input('alto'))
profundo = float(input('profundo'))

cubo = Cubo(ancho,alto,profundo)
print(cubo.calcul_volumen())
