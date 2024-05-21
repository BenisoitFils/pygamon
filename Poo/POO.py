class Restaurant:
    def agregar_restaurant(self,nombre):
        self.nombre = nombre #atributo
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
# instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant('pezzeria mexico')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('hamburguesas python')
restaurant2.mostrar_informacion()
# mostrar la informacion
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')