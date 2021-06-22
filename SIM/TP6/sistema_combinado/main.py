import sys
from PyQt5.QtWidgets import QApplication
from interfaz.recursos import sim
from interfaz.ventana_sistema_combinado import VentanaSistemaCombinado


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = VentanaSistemaCombinado(app)
    window.show()
    app.exec_()
