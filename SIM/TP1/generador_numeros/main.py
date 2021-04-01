import sys
from PyQt5.QtWidgets import QApplication
from interfaz.recursos import sim
from interfaz.ventana_generador_numeros_pseudoaleatorios import VentanaGeneradorNumerosPseudoaleatorios


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = VentanaGeneradorNumerosPseudoaleatorios()
    window.show()
    app.exec_()



