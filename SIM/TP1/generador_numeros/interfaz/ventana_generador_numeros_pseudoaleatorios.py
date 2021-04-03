from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from dominio.controlador_generador_numeros_pseudoaleatorios import ControladorGeneradorNumerosPseudoaleatorios
from soporte.validador_decimales import ValidadorDecimales
from soporte.validador_enteros import ValidadorEnteros
from soporte.ruta import Ruta


class VentanaGeneradorNumerosPseudoaleatorios(QMainWindow):

    """ Atributos """

    controlador = None
    numeros_pseudoaleatorios = []

    """ Constructor """

    def __init__(self):

        # Genero ventana a partir de ui y creo controlador
        QMainWindow.__init__(self)
        uic.loadUi(Ruta.generar_ruta("interfaz/ventana_generador_numeros_pseudoaleatorios.ui"), self)
        self.controlador = ControladorGeneradorNumerosPseudoaleatorios()

        # Agrego validadores a los campos
        validador_decimales = ValidadorDecimales(12, 4)
        validador_enteros = ValidadorEnteros(12)
        self.txt_semilla.setValidator(validador_decimales)
        self.txt_a.setValidator(validador_decimales)
        self.txt_c.setValidator(validador_decimales)
        self.txt_m.setValidator(validador_decimales)
        self.txt_cantidad_numeros.setValidator(validador_enteros)

        # Conecto los botones con los eventos
        self.cmb_metodo_generacion.currentIndexChanged.connect(self.accion_seleccionar_metodo)
        self.btn_generar_numeros.clicked.connect(self.accion_generar_numeros)
        self.btn_generar_histograma.clicked.connect(self.accion_generar_histograma)
        self.btn_test_chi_cuadrado.clicked.connect(self.accion_test_chi_cuadrado)
        self.btn_limpiar.clicked.connect(self.accion_limpiar)

    """ Acciones """

    def accion_seleccionar_metodo(self):

        # Activo o desactivo inputs dependiendo del metodo elegido
        metodo = self.cmb_metodo_generacion.itemData(self.cmb_metodo_generacion.currentIndex())
        if metodo == 0:
            self.txt_semilla.setEnabled(True)
            self.txt_a.setEnabled(True)
            self.txt_c.setEnabled(True)
            self.txt_m.setEnabled(True)
        elif metodo == 1:
            self.txt_semilla.setEnabled(True)
            self.txt_a.setEnabled(True)
            self.txt_c.clear()
            self.txt_c.setEnabled(False)
            self.txt_m.setEnabled(True)
        else:
            self.txt_semilla.clear()
            self.txt_semilla.setEnabled(False)
            self.txt_a.clear()
            self.txt_a.setEnabled(False)
            self.txt_c.clear()
            self.txt_c.setEnabled(False)
            self.txt_m.clear()
            self.txt_m.setEnabled(False)

    def accion_generar_numeros(self):

        # Obtengo metodo
        metodo = self.cmb_metodo_generacion.itemData(self.cmb_metodo_generacion.currentIndex())

        # Obtengo parametros verificando que no sean vacios
        semilla = None
        a = None
        c = None
        m = None
        cantidad_numeros = None
        if self.txt_semilla.text() != "":
            semilla = float(self.txt_semilla.text().replace(",", "."))
        if self.txt_a.text() != "":
            a = float(self.txt_a.text().replace(",", "."))
        if self.txt_c.text() != "":
            c = float(self.txt_c.text().replace(",", "."))
        if self.txt_m.text() != "":
            m = float(self.txt_m.text().replace(",", "."))
        if self.txt_cantidad_numeros.text() != "":
            cantidad_numeros = int(self.txt_cantidad_numeros.text())

        # Valido parametros dependiendo del metodo
        if metodo == 0:
            if semilla is None or semilla < 0:
                self.mostrar_mensaje("Error", "La semilla tiene que ser mayor o igual a cero")
                return
            if a is None or a <= 0:
                self.mostrar_mensaje("Error", "La constante \"a\" tiene que ser mayor a cero")
                return
            if c is None or c <= 0:
                self.mostrar_mensaje("Error", "La constante \"c\" tiene que ser mayor a cero")
                return
            if m is None or m <= 0:
                self.mostrar_mensaje("Error", "La constante \"m\" tiene que ser mayor a cero")
                return
            if semilla >= m:
                self.mostrar_mensaje("Error", "La semilla tiene que ser menor a la constante \"m\"")
                return
            if a >= m:
                self.mostrar_mensaje("Error", "La constante \"a\" tiene que ser menor a la constante \"m\"")
                return
            if c >= m:
                self.mostrar_mensaje("Error", "La constante \"c\" tiene que ser menor a la constante \"m\"")
                return
            if cantidad_numeros is None or cantidad_numeros <= 0:
                self.mostrar_mensaje("Error", "La cantidad de números tiene que ser mayor a cero")
        elif metodo == 1:
            if semilla is None or semilla < 0:
                self.mostrar_mensaje("Error", "La semilla tiene que ser mayor o igual a cero")
                return
            if a is None or a <= 0:
                self.mostrar_mensaje("Error", "La constante \"a\" tiene que ser mayor a cero")
                return
            if m is None or m <= 0:
                self.mostrar_mensaje("Error", "La constante \"m\" tiene que ser mayor a cero")
                return
            if semilla >= m:
                self.mostrar_mensaje("Error", "La semilla tiene que ser menor a la constante \"m\"")
                return
            if a >= m:
                self.mostrar_mensaje("Error", "La constante \"a\" tiene que ser menor a la constante \"m\"")
                return
            if cantidad_numeros is None or cantidad_numeros <= 0:
                self.mostrar_mensaje("Error", "La cantidad de números tiene que ser mayor a cero")
        elif metodo == 2:
            if cantidad_numeros is None or cantidad_numeros <= 0:
                self.mostrar_mensaje("Error", "La cantidad de números tiene que ser mayor a cero")

        # Limpio datos
        self.limpiar_datos()

        # Genero numeros pseusoaleatorios dependiendo del metodo seleccionado
        if metodo == 0:
            self.numeros_pseudoaleatorios = self.controlador.generar_numeros_pseudoaleatorios_congruencial_lineal(
                cantidad_numeros, semilla, a, c, m)
        elif metodo == 1:
            self.numeros_pseudoaleatorios = self.controlador.generar_numeros_pseudoaleatorios_congruencial_multiplicativo(
                cantidad_numeros, semilla, a, m)
        elif metodo == 2:
            self.numeros_pseudoaleatorios = self.controlador.generar_numeros_pseudoaleatorios_provisto_por_lenguaje(
                cantidad_numeros)

        # Limpio tablas
        self.limpiar_tablas()

        # Cargo tabla
        self.cargar_tabla_numeros_pseudoaleatorios()

    def accion_generar_histograma(self):

        # Valido que se hayan generado numeros pseusoaleatorios con anterioridad
        if len(self.numeros_pseudoaleatorios) == 0:
            self.mostrar_mensaje("Error", "Primero debe generar los números pseusoaleatorios")
            return

        # Obtengo parametros
        cantidad_intervalos = self.cmb_cantidad_intervalos.itemData(self.cmb_cantidad_intervalos.currentIndex())

        # Obtengo intervalos
        intervalos = self.controlador.obtener_intervalos(cantidad_intervalos)

        # Genero y muestro histograma
        self.controlador.generar_histograma(self.numeros_pseudoaleatorios, intervalos)

    def accion_test_chi_cuadrado(self):

        # Valido que se hayan generado numeros pseusoaleatorios con anterioridad
        if len(self.numeros_pseudoaleatorios) == 0:
            self.mostrar_mensaje("Error", "Primero debe generar los números pseusoaleatorios")
            return

        # Obtengo parametros
        cantidad_intervalos = self.cmb_cantidad_intervalos.itemData(self.cmb_cantidad_intervalos.currentIndex())

        # Obtengo intervalos
        intevalos = self.controlador.obtener_intervalos(cantidad_intervalos)

        # Realizo prueba de chi cuadrado
        chi_cuadrado_x_intervalo, chi_cuadrado = self.controlador.realizar_test_chi_cuadrado(
            self.numeros_pseudoaleatorios, intevalos)

        # Muestro resultados de prueba de chi cuadrado
        self.cargar_tabla_test_chi_cuadrado(chi_cuadrado_x_intervalo, chi_cuadrado)

    def accion_limpiar(self):

        # Limpio datos y elementos de interfaz
        self.limpiar_datos()
        self.limpiar_formulario()
        self.limpiar_tablas()

    """ Metodos """

    def preparar_interfaz(self):

        # Cargo combo box de metodo de generacion
        self.cmb_metodo_generacion.clear()
        self.cmb_metodo_generacion.addItem("Congruencial lineal", 0)
        self.cmb_metodo_generacion.addItem("Congruencial multiplicativo", 1)
        self.cmb_metodo_generacion.addItem("Provisto por el lenguaje", 2)

        # Cargo combo box de metodo de generacion
        self.cmb_cantidad_intervalos.clear()
        self.cmb_cantidad_intervalos.addItem("10", 10)
        self.cmb_cantidad_intervalos.addItem("15", 15)
        self.cmb_cantidad_intervalos.addItem("20", 20)

        # Preparo tabla de numeros generados
        self.grid_numeros_generados.setColumnCount(2)
        self.grid_numeros_generados.setHorizontalHeaderLabels(["N° de orden", "Número aleatorio"])

        # Preparo tabla de test de chi cuadrado
        self.grid_test_chi_cuadrado.setColumnCount(5)
        self.grid_test_chi_cuadrado.setHorizontalHeaderLabels(["Intervalo", "fo", "fe", "C", "C (AC)"])

    def limpiar_datos(self):

        self.numeros_pseudoaleatorios = []

    def limpiar_formulario(self):

        # Limpio txts
        self.txt_semilla.clear()
        self.txt_a.clear()
        self.txt_c.clear()
        self.txt_m.clear()
        self.txt_cantidad_numeros.clear()

        # Activo txts
        self.txt_semilla.setEnabled(True)
        self.txt_a.setEnabled(True)
        self.txt_c.setEnabled(True)
        self.txt_m.setEnabled(True)

        # Selecciono opcion por defecto en combo boxs
        self.cmb_metodo_generacion.setCurrentIndex(0)
        self.cmb_cantidad_intervalos.setCurrentIndex(0)

    def limpiar_tablas(self):

        # Limpio grilla de numeros generados
        self.grid_numeros_generados.clearSelection()
        self.grid_numeros_generados.setCurrentCell(-1, -1)
        self.grid_numeros_generados.setRowCount(0)

        # Limpio grilla de test de chi cuadrado
        self.grid_test_chi_cuadrado.clearSelection()
        self.grid_test_chi_cuadrado.setCurrentCell(-1, -1)
        self.grid_test_chi_cuadrado.setRowCount(0)

    def mostrar_mensaje(self, titulo, mensaje):

        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def cargar_tabla_numeros_pseudoaleatorios(self):

        self.grid_numeros_generados.setRowCount(len(self.numeros_pseudoaleatorios))
        index = 0
        for numero_pseudoaleatorio in self.numeros_pseudoaleatorios:

            # Obtengo datos en formato conveniente
            nro_orden_str = str(index + 1)
            numero_pseudoaleatorio_str = str(numero_pseudoaleatorio).replace(".", ",")

            # Agrego fila a tabla
            self.grid_numeros_generados.setItem(index, 0, QTableWidgetItem(nro_orden_str))
            self.grid_numeros_generados.setItem(index, 1, QTableWidgetItem(numero_pseudoaleatorio_str))
            index += 1

    def cargar_tabla_test_chi_cuadrado(self, chi_cuadrado_x_intervalo, chi_cuadrado):

        self.grid_test_chi_cuadrado.setRowCount(len(chi_cuadrado_x_intervalo))
        index = 0
        for chi_cuadrado_intervalo in chi_cuadrado_x_intervalo:

            # Obtengo datos en formato conveniente
            intervalo_str = str(chi_cuadrado_intervalo.get("intervalo")[0]).replace(".", ",") + " - " + \
                            str(chi_cuadrado_intervalo.get("intervalo")[1]).replace(".", ",")
            fo_str = str(chi_cuadrado_intervalo.get("fo")).replace(".", ",")
            fe_str = str(chi_cuadrado_intervalo.get("fe")).replace(".", ",")
            c_str = str(chi_cuadrado_intervalo.get("c")).replace(".", ",")
            c_acum_str = str(chi_cuadrado_intervalo.get("c_acum")).replace(".", ",")

            # Agrego fila a tabla
            self.grid_test_chi_cuadrado.setItem(index, 0, QTableWidgetItem(intervalo_str))
            self.grid_test_chi_cuadrado.setItem(index, 1, QTableWidgetItem(fo_str))
            self.grid_test_chi_cuadrado.setItem(index, 2, QTableWidgetItem(fe_str))
            self.grid_test_chi_cuadrado.setItem(index, 3, QTableWidgetItem(c_str))
            self.grid_test_chi_cuadrado.setItem(index, 4, QTableWidgetItem(c_acum_str))
            index += 1

        self.mostrar_mensaje("Test de Chi Cuadrado",
                             "El estadístico de prueba obtenido es %s. El mismo debe ser menor o igual al obtenido por "
                             "tabla para que la hipótesis no se rechace"
                             % str(chi_cuadrado).replace(".", ","))

    """ Eventos """

    # Evento show
    def showEvent(self, QShowEvent):
        self.preparar_interfaz()
        self.limpiar_datos()
