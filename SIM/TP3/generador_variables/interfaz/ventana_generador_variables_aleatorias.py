from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from dominio.controlador_generador_variables_aleatorias import ControladorGeneradorVariablesAleatorias
from soporte.validador_enteros import ValidadorEnteros
from soporte.validador_decimales import ValidadorDecimales
from soporte.ruta import Ruta


class VentanaGeneradorVariablesAleatorias(QMainWindow):

    """ Atributos """

    controlador = None
    variables_aleatorias = []
    parametros_variables_aleatorias = {}

    """ Constructor """

    def __init__(self):

        # Genero ventana a partir de ui y creo controlador
        QMainWindow.__init__(self)
        uic.loadUi(Ruta.generar_ruta("interfaz/ventana_generador_variables_aleatorias.ui"), self)
        self.controlador = ControladorGeneradorVariablesAleatorias()

        # Agrego validadores a los campos
        validador_decimales_negativos = ValidadorDecimales(12, 4, True)
        validador_decimales = ValidadorDecimales(12, 4)
        validador_enteros = ValidadorEnteros(12)
        self.txt_a.setValidator(validador_decimales_negativos)
        self.txt_b.setValidator(validador_decimales_negativos)
        self.txt_mu.setValidator(validador_decimales_negativos)
        self.txt_sigma.setValidator(validador_decimales)
        self.txt_lambda.setValidator(validador_decimales)
        self.txt_cantidad_variables.setValidator(validador_enteros)

        # Conecto los botones con los eventos
        self.cmb_distribucion.currentIndexChanged.connect(self.accion_seleccionar_distribucion)
        self.btn_generar_variables.clicked.connect(self.accion_generar_variables)
        self.btn_generar_histograma.clicked.connect(self.accion_generar_histograma)
        self.btn_limpiar.clicked.connect(self.accion_limpiar)

    """ Acciones """

    def accion_seleccionar_distribucion(self):

        # Activo o desactivo inputs dependiendo de la distribucion seleccionada
        distribucion = self.cmb_distribucion.itemData(self.cmb_distribucion.currentIndex())
        if distribucion == 0:
            self.txt_a.setEnabled(True)
            self.txt_b.setEnabled(True)
            self.txt_mu.clear()
            self.txt_mu.setEnabled(False)
            self.txt_sigma.clear()
            self.txt_sigma.setEnabled(False)
            self.txt_lambda.clear()
            self.txt_lambda.setEnabled(False)
        elif distribucion == 1:
            self.txt_a.clear()
            self.txt_a.setEnabled(False)
            self.txt_b.clear()
            self.txt_b.setEnabled(False)
            self.txt_mu.setEnabled(True)
            self.txt_sigma.setEnabled(True)
            self.txt_lambda.clear()
            self.txt_lambda.setEnabled(False)
        else:
            self.txt_a.clear()
            self.txt_a.setEnabled(False)
            self.txt_b.clear()
            self.txt_b.setEnabled(False)
            self.txt_mu.clear()
            self.txt_mu.setEnabled(False)
            self.txt_sigma.clear()
            self.txt_sigma.setEnabled(False)
            self.txt_lambda.clear()
            self.txt_lambda.setEnabled(True)

    def accion_generar_variables(self):

        # Obtengo distribución
        distribucion = self.cmb_distribucion.itemData(self.cmb_distribucion.currentIndex())

        # Obtengo parametros verificando que no sean vacios
        a = None
        b = None
        mu = None
        sigma = None
        lambd = None
        cantidad_variables = None
        if self.txt_a.text() != "":
            a = float(self.txt_a.text().replace(",", "."))
        if self.txt_b.text() != "":
            b = float(self.txt_b.text().replace(",", "."))
        if self.txt_mu.text() != "":
            mu = float(self.txt_mu.text().replace(",", "."))
        if self.txt_sigma.text() != "":
            sigma = float(self.txt_sigma.text().replace(",", "."))
        if self.txt_lambda.text() != "":
            lambd = float(self.txt_lambda.text().replace(",", "."))
        if self.txt_cantidad_variables.text() != "":
            cantidad_variables = int(self.txt_cantidad_variables.text())

        # Valido parametros dependiendo de la distribución
        if distribucion == 0:
            if a is None:
                self.mostrar_mensaje("Error", "El parámetro \"a\" no puede ser vacío")
                return
            if b is None:
                self.mostrar_mensaje("Error", "El parámetro \"b\" no puede ser vacío")
                return
            if a >= b:
                self.mostrar_mensaje("Error", "El parámetro \"a\" no puede ser mayor o igual al parámetro \"b\"")
                return
            if cantidad_variables is None or cantidad_variables <= 0:
                self.mostrar_mensaje("Error", "La cantidad de variables tiene que ser mayor a cero")
                return
        elif distribucion == 1:
            if mu is None:
                self.mostrar_mensaje("Error", "El parámetro \"mu\" no puede ser vacío")
                return
            if sigma is None or sigma <= 0:
                self.mostrar_mensaje("Error", "El parámetro \"sigma\" tiene que ser mayor a cero")
                return
            if cantidad_variables is None or cantidad_variables <= 0:
                self.mostrar_mensaje("Error", "La cantidad de variables tiene que ser mayor a cero")
                return
        elif distribucion == 2:
            if lambd is None or lambd <= 0:
                self.mostrar_mensaje("Error", "El parámetro \"lambda\" tiene que ser mayor a cero")
                return
            if cantidad_variables is None or cantidad_variables <= 0:
                self.mostrar_mensaje("Error", "La cantidad de variables tiene que ser mayor a cero")
                return

        # Limpio datos
        self.limpiar_datos()

        # Genero variables aleatorias dependiendo de la distribución seleccionada
        if distribucion == 0:
            self.variables_aleatorias = self.controlador.generar_variables_aleatorias_uniforme(cantidad_variables, a, b)
            self.parametros_variables_aleatorias = {
                "distribucion": distribucion,
                "a": a,
                "b": b
            }
        elif distribucion == 1:
            self.variables_aleatorias = self.controlador.generar_variables_aleatorias_normal(cantidad_variables, mu,
                                                                                             sigma)
            self.parametros_variables_aleatorias = {
                "distribucion": distribucion,
                "mu": mu,
                "sigma": sigma
            }
        elif distribucion == 2:
            self.variables_aleatorias = self.controlador.generar_variables_aleatorias_exponencial(cantidad_variables,
                                                                                                  lambd)
            self.parametros_variables_aleatorias = {
                "distribucion": distribucion,
                "lambda": lambd
            }

        # Limpio tablas
        self.limpiar_tablas()

        # Cargo tabla
        self.cargar_tabla_variables_aleatorias()

    def accion_generar_histograma(self):

        # Valido que se hayan generado variables aleatorias con anterioridad
        if len(self.variables_aleatorias) == 0:
            self.mostrar_mensaje("Error", "Primero debe generar las variables aleatorias")
            return

        # Obtengo parametros
        cantidad_intervalos = self.cmb_cantidad_intervalos.itemData(self.cmb_cantidad_intervalos.currentIndex())

        # Ordeno lista de variables aleatorias y obtengo el mínimo y el máximo
        self.variables_aleatorias = self.controlador.ordenar_variables_aleatorias(self.variables_aleatorias)
        if self.parametros_variables_aleatorias.get("distribucion") == 0:
            minimo = self.parametros_variables_aleatorias.get("a")
            maximo = self.parametros_variables_aleatorias.get("b")
        elif self.parametros_variables_aleatorias.get("distribucion") == 1:
            minimo = self.variables_aleatorias[0] - 0.0001
            maximo = self.variables_aleatorias[len(self.variables_aleatorias) - 1] + 0.0001
        else:
            minimo = 0
            maximo = self.variables_aleatorias[len(self.variables_aleatorias) - 1] + 0.0001

        # Obtengo intervalos
        intervalos = self.controlador.obtener_intervalos(cantidad_intervalos, minimo, maximo)

        # Genero y muestro histograma
        self.controlador.generar_histograma(self.variables_aleatorias, intervalos, minimo, maximo)

        # Genero y muestro tabla de frecuencias
        frecuencias_x_intervalo = self.controlador.obtener_frecuencias_por_intervalos(
            self.variables_aleatorias, self.parametros_variables_aleatorias, intervalos)
        self.cargar_tabla_frecuencias(frecuencias_x_intervalo)

    def accion_limpiar(self):

        # Limpio datos y elementos de interfaz
        self.limpiar_datos()
        self.limpiar_formulario()
        self.limpiar_tablas()

    """ Metodos """

    def preparar_interfaz(self):

        # Cargo combo box de distribuciones
        self.cmb_distribucion.clear()
        self.cmb_distribucion.addItem("Uniforme", 0)
        self.cmb_distribucion.addItem("Normal", 1)
        self.cmb_distribucion.addItem("Exponencial", 2)

        # Cargo combo box de metodo de generacion
        self.cmb_cantidad_intervalos.clear()
        self.cmb_cantidad_intervalos.addItem("10", 10)
        self.cmb_cantidad_intervalos.addItem("15", 15)
        self.cmb_cantidad_intervalos.addItem("20", 20)

        # Preparo tabla de variables generadas
        self.grid_variables_generadas.setColumnCount(2)
        self.grid_variables_generadas.setHorizontalHeaderLabels(["N° de orden", "Variable aleatoria"])

        # Preparo tabla frecuencias
        self.grid_frecuencias.setColumnCount(5)
        self.grid_frecuencias.setHorizontalHeaderLabels(["Intervalo", "fo", "fo (AC)", "fe", "fe (AC)"])

    def limpiar_datos(self):

        self.variables_aleatorias = []
        self.parametros_variables_aleatorias = {}

    def limpiar_formulario(self):

        # Limpio txts
        self.txt_a.clear()
        self.txt_b.clear()
        self.txt_mu.clear()
        self.txt_sigma.clear()
        self.txt_lambda.clear()
        self.txt_cantidad_variables.clear()

        # Activo txts
        self.txt_a.setEnabled(True)
        self.txt_b.setEnabled(True)
        self.txt_mu.setEnabled(False)
        self.txt_sigma.setEnabled(False)
        self.txt_lambda.setEnabled(False)

        # Selecciono opcion por defecto en combo boxs
        self.cmb_distribucion.setCurrentIndex(0)
        self.cmb_cantidad_intervalos.setCurrentIndex(0)

    def limpiar_tablas(self):

        # Limpio grilla de numeros generados
        self.grid_variables_generadas.clearSelection()
        self.grid_variables_generadas.setCurrentCell(-1, -1)
        self.grid_variables_generadas.setRowCount(0)

        # Limpio grilla de test de chi cuadrado
        self.grid_frecuencias.clearSelection()
        self.grid_frecuencias.setCurrentCell(-1, -1)
        self.grid_frecuencias.setRowCount(0)

    def mostrar_mensaje(self, titulo, mensaje):

        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def cargar_tabla_variables_aleatorias(self):

        self.grid_variables_generadas.setRowCount(len(self.variables_aleatorias))
        index = 0
        for variable_aleatoria in self.variables_aleatorias:

            # Obtengo datos en formato conveniente
            nro_orden_str = str(index + 1)
            variable_aleatoria_str = str(variable_aleatoria).replace(".", ",")

            # Agrego fila a tabla
            self.grid_variables_generadas.setItem(index, 0, QTableWidgetItem(nro_orden_str))
            self.grid_variables_generadas.setItem(index, 1, QTableWidgetItem(variable_aleatoria_str))
            index += 1

    def cargar_tabla_frecuencias(self, frecuencias_x_intervalo):

        self.grid_frecuencias.setRowCount(len(frecuencias_x_intervalo))
        index = 0
        for frecuencias_intervalo in frecuencias_x_intervalo:

            # Obtengo datos en formato conveniente
            if frecuencias_intervalo.get("intervalo")[0] >= 0:
                minimo_intervalo = str(frecuencias_intervalo.get("intervalo")[0]).replace(".", ",")
            else:
                minimo_intervalo = "(" + str(frecuencias_intervalo.get("intervalo")[0]).replace(".", ",") + ")"
            if frecuencias_intervalo.get("intervalo")[1] >= 0:
                maximo_intervalo = str(frecuencias_intervalo.get("intervalo")[1]).replace(".", ",")
            else:
                maximo_intervalo = "(" + str(frecuencias_intervalo.get("intervalo")[1]).replace(".", ",") + ")"
            intervalo_str = minimo_intervalo + " - " + maximo_intervalo
            fo_str = str(frecuencias_intervalo.get("fo")).replace(".", ",")
            fo_acum_str = str(frecuencias_intervalo.get("fo_acum")).replace(".", ",")
            fe_str = str(frecuencias_intervalo.get("fe")).replace(".", ",")
            fe_acum_str = str(frecuencias_intervalo.get("fe_acum")).replace(".", ",")

            # Agrego fila a tabla
            self.grid_frecuencias.setItem(index, 0, QTableWidgetItem(intervalo_str))
            self.grid_frecuencias.setItem(index, 1, QTableWidgetItem(fo_str))
            self.grid_frecuencias.setItem(index, 2, QTableWidgetItem(fo_acum_str))
            self.grid_frecuencias.setItem(index, 3, QTableWidgetItem(fe_str))
            self.grid_frecuencias.setItem(index, 4, QTableWidgetItem(fe_acum_str))
            index += 1

    """ Eventos """

    # Evento show
    def showEvent(self, QShowEvent):
        self.preparar_interfaz()
        self.limpiar_datos()
