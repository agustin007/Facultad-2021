import sys
from PyQt5.QtWidgets import QApplication
from interfaz.recursos import sim
from interfaz.ventana_sistema_colas import VentanaSistemaColas


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = VentanaSistemaColas()
    window.show()
    app.exec_()



