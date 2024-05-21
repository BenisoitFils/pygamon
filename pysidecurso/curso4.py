import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QApplication


class VentanaPySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('POO con PySide')
        #self.resize(600, 400)
        # Colocamos los valores de ancho y alto de manera fija
        self.setFixedSize(QSize(600, 400))


if __name__== '__main__':
    app = QApplication([])
    # creamos un objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())