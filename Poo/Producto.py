class Producto:
    contador_productos =0

    def __init__(self,nombre,precio):
        Producto.contador_productos += 1
        self._id_productos = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id Producto: {self._id_productos}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('camisa', 100.00)
    print(producto1)
    producto2 = Producto('pantalón', 150.00)
    print(producto2)










