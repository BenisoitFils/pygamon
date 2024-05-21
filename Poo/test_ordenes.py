from Poo.Orden import Orden
from Poo.Producto import Producto

producto1 = Producto('camisa', 100.00)
producto2 = Producto('pantalón', 150.00)
producto3 = Producto('calcetines', 50.00)
producto4 = Producto('blusa', 70.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f'Total orden1: {orden1.calcular_total()}')
orden2 = Orden(productos2)
print(orden2)
print(f'Total orden2: {orden2.calcular_total()}')