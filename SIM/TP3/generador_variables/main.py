import sys
from PyQt5.QtWidgets import QApplication
from interfaz.recursos import sim
from interfaz.ventana_generador_variables_aleatorias import VentanaGeneradorVariablesAleatorias


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = VentanaGeneradorVariablesAleatorias()
    window.show()
    app.exec_()



