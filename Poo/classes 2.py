class Restaurant:
    def __init__(self,nombre, categoria,precio):
        self.nombre = nombre  # atributo
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre},categoria: {self.categoria}, precio: {self.precio}')
# instanciar la clase
restaurant = Restaurant('pezzeria mexico', 'comida italiana', 50)
#print(restaurant.precio)
restaurant.precio = 80
restaurant.mostrar_informacion()

restaurant2 = Restaurant('hamburguesas python', 'comida casual', 20)
#print(restaurant2.precio)
restaurant2.precio = 40
#restaurant2.mostrar_informacion()
