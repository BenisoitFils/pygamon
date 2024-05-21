import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Clase base de Qt (PySide)
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Crear un objecto ventana
ventana = QMainWindow()
# Cambiar el titulo
ventana.setWindowTitle('Hola')
# Modificamos el tamaño de la ventana
ventana.resize(600, 400)
# Mostrar la ventana
ventana.show()
# Se ejecutar la aplicacion
sys.exit(app.exec())