from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from dominio.controlador_montecarlo import ControladorMontecarlo
from soporte.validador_enteros import ValidadorEnteros
from soporte.ruta import Ruta


class VentanaMontecarlo(QMainWindow):

    """ Atributos """

    controlador = None
    semanas_simuladas = {}

    """ Constructor """

    def __init__(self):

        # Genero ventana a partir de ui y creo controlador
        QMainWindow.__init__(self)
        uic.loadUi(Ruta.generar_ruta("interfaz/ventana_montecarlo.ui"), self)
        self.controlador = ControladorMontecarlo()

        # Agrego validadores a los campos
        validador_6_enteros = ValidadorEnteros(6)
        validador_4_enteros = ValidadorEnteros(4)
        validador_3_enteros = ValidadorEnteros(3)
        self.txt_cantidad_semanas.setValidator(validador_6_enteros)
        self.txt_semana_desde.setValidator(validador_6_enteros)
        self.txt_semana_hasta.setValidator(validador_6_enteros)
        self.txt_probabilidad_0_demanda.setValidator(validador_3_enteros)
        self.txt_probabilidad_1_demanda.setValidator(validador_3_enteros)
        self.txt_probabilidad_2_demanda.setValidator(validador_3_enteros)
        self.txt_probabilidad_3_demanda.setValidator(validador_3_enteros)
        self.txt_probabilidad_1_tiempo_entrega.setValidator(validador_3_enteros)
        self.txt_probabilidad_2_tiempo_entrega.setValidator(validador_3_enteros)
        self.txt_probabilidad_3_tiempo_entrega.setValidator(validador_3_enteros)
        self.txt_probabilidad_bicicleta_daniada.setValidator(validador_3_enteros)
        self.txt_costo_tenencia.setValidator(validador_4_enteros)
        self.txt_costo_pedido.setValidator(validador_4_enteros)
        self.txt_costo_agotamiento.setValidator(validador_4_enteros)
        self.txt_stock_minimo.setValidator(validador_4_enteros)

        # Conecto los botones con los eventos
        self.btn_limpiar.clicked.connect(self.accion_limpiar)
        self.btn_simular.clicked.connect(self.accion_simular)

    """ Acciones """

    def accion_limpiar(self):

        # Restauro valores por defecto de interfaz y limpio tabla
        self.semanas_simuladas = []
        self.limpiar_interfaz()
        self.limpiar_tabla()

    def accion_simular(self):

        # Obtengo parametros verificando que no sean vacios
        cantidad_semanas = None
        semana_desde = None
        semana_hasta = None
        probabilidad_0_demanda = None
        probabilidad_1_demanda = None
        probabilidad_2_demanda = None
        probabilidad_3_demanda = None
        probabilidad_1_tiempo_entrega = None
        probabilidad_2_tiempo_entrega = None
        probabilidad_3_tiempo_entrega = None
        probabilidad_bicicleta_daniada = None
        costo_tenencia = None
        costo_pedido = None
        costo_agotamiento = None
        stock_minimo = None
        if self.txt_cantidad_semanas.text() != "":
            cantidad_semanas = int(self.txt_cantidad_semanas.text())
        if self.txt_semana_desde.text() != "":
            semana_desde = int(self.txt_semana_desde.text())
        if self.txt_semana_hasta.text() != "":
            semana_hasta = int(self.txt_semana_hasta.text())
        if self.txt_probabilidad_0_demanda.text() != "":
            probabilidad_0_demanda = int(self.txt_probabilidad_0_demanda.text())
        if self.txt_probabilidad_1_demanda.text() != "":
            probabilidad_1_demanda = int(self.txt_probabilidad_1_demanda.text())
        if self.txt_probabilidad_2_demanda.text() != "":
            probabilidad_2_demanda = int(self.txt_probabilidad_2_demanda.text())
        if self.txt_probabilidad_3_demanda.text() != "":
            probabilidad_3_demanda = int(self.txt_probabilidad_3_demanda.text())
        if self.txt_probabilidad_1_tiempo_entrega.text() != "":
            probabilidad_1_tiempo_entrega = int(self.txt_probabilidad_1_tiempo_entrega.text())
        if self.txt_probabilidad_2_tiempo_entrega.text() != "":
            probabilidad_2_tiempo_entrega = int(self.txt_probabilidad_2_tiempo_entrega.text())
        if self.txt_probabilidad_3_tiempo_entrega.text() != "":
            probabilidad_3_tiempo_entrega = int(self.txt_probabilidad_3_tiempo_entrega.text())
        if self.txt_probabilidad_bicicleta_daniada.text() != "":
            probabilidad_bicicleta_daniada = int(self.txt_probabilidad_bicicleta_daniada.text())
        if self.txt_costo_tenencia.text() != "":
            costo_tenencia = int(self.txt_costo_tenencia.text())
        if self.txt_costo_pedido.text() != "":
            costo_pedido = int(self.txt_costo_pedido.text())
        if self.txt_costo_agotamiento.text() != "":
            costo_agotamiento = int(self.txt_costo_agotamiento.text())
        if self.txt_stock_minimo.text() != "":
            stock_minimo = int(self.txt_stock_minimo.text())

        # Valido parametros dependiendo de la distribución
        if cantidad_semanas is None or cantidad_semanas <= 0:
            self.mostrar_mensaje("Error", "La cantidad de semanas tiene que ser mayor a cero")
            return
        if semana_desde is None or semana_desde <= 0:
            self.mostrar_mensaje("Error", "La semana desde la cuál mostrar la simulación tiene que ser mayor a cero")
            return
        if semana_hasta is None or semana_hasta <= 0:
            self.mostrar_mensaje("Error", "La semana hasta la cuál mostrar la simulación tiene que ser mayor a cero")
            return
        if semana_desde > cantidad_semanas:
            self.mostrar_mensaje("Error", "La semana desde la cuál mostrar la simulación no puede ser mayor a la "
                                          "cantidad de semanas simuladas")
            return
        if semana_hasta > cantidad_semanas:
            self.mostrar_mensaje("Error", "La semana hasta la cuál mostrar la simulación no puede ser mayor a la "
                                          "cantidad de semanas simuladas")
            return
        if semana_hasta > semana_desde:
            self.mostrar_mensaje("Error", "La semana desde la cuál mostrar la simulación no puede ser mayor a la "
                                          "semana hasta la cuál mostrar la simulación")
            return
        if probabilidad_0_demanda is None:
            self.mostrar_mensaje("Error", "La probabilidad de que se demanden 0 bicicletas por semana no puede ser "
                                          "vacía")
            return
        if probabilidad_1_demanda is None:
            self.mostrar_mensaje("Error", "La probabilidad de que se demande 1 bicicleta por semana no puede ser vacía")
            return
        if probabilidad_2_demanda is None:
            self.mostrar_mensaje("Error", "La probabilidad de que se demanden 2 bicicletas por semana no puede ser "
                                          "vacía")
            return
        if probabilidad_3_demanda is None:
            self.mostrar_mensaje("Error", "La probabilidad de que se demanden 3 bicicletas por semana no puede ser "
                                          "vacía")
            return
        if (probabilidad_0_demanda + probabilidad_1_demanda + probabilidad_2_demanda + probabilidad_3_demanda) != 100:
            self.mostrar_mensaje("Error", "Las probabilidades de demanda de bicicletas deben sumar un 100%")
            return
        if probabilidad_1_tiempo_entrega is None:
            self.mostrar_mensaje("Error", "La probabilidad de que el tiempo de entrega sea de 1 semana no puede ser "
                                          "vacía")
            return
        if probabilidad_2_tiempo_entrega is None:
            self.mostrar_mensaje("Error", "La probabilidad de que el tiempo de entrega sea de 2 semanas no puede ser "
                                          "vacía")
            return
        if probabilidad_3_tiempo_entrega is None:
            self.mostrar_mensaje("Error", "La probabilidad de que el tiempo de entrega sea de 3 semanas no puede ser "
                                          "vacía")
            return
        if (probabilidad_1_tiempo_entrega + probabilidad_2_tiempo_entrega + probabilidad_3_tiempo_entrega) != 100:
            self.mostrar_mensaje("Error", "Las probabilidades de tiempo de entrega deben sumar un 100%")
            return
        if probabilidad_bicicleta_daniada is None:
            self.mostrar_mensaje("Error", "La probabilidad de que llegue una bicicleta dañanda en el pedido no puede "
                                          "ser vacía")
            return
        if costo_tenencia is None:
            self.mostrar_mensaje("Error", "El costo de tenencia de las bicicletas no puede ser vacío")
            return
        if costo_pedido is None:
            self.mostrar_mensaje("Error", "El costo de pedido de las bicicletas no puede ser vacío")
            return
        if costo_agotamiento is None:
            self.mostrar_mensaje("Error", "El costo de agotamiento de las bicicletas no puede ser vacío")
            return
        if stock_minimo is None:
            self.mostrar_mensaje("Error", "El stock mínimo de bicicletas que debe haber para verificar si debe "
                                          "realizarse o no un pedido no puede ser vacío")
            return

        # Realizo simulacion y obtengo semanas a mostrar
        self.semanas_simuladas = self.controlador.simular_semanas(cantidad_semanas, semana_desde, semana_hasta,
                                                                  probabilidad_0_demanda, probabilidad_1_demanda,
                                                                  probabilidad_2_demanda, probabilidad_3_demanda,
                                                                  probabilidad_1_tiempo_entrega,
                                                                  probabilidad_2_tiempo_entrega,
                                                                  probabilidad_3_tiempo_entrega,
                                                                  probabilidad_bicicleta_daniada, costo_tenencia,
                                                                  costo_pedido, costo_agotamiento, stock_minimo)

        # Cargo tabla
        self.cargar_tabla_semanas_simuladas()

    """ Metodos """

    def preparar_interfaz(self):

        # Preparo tabla de semanas simuladas
        self.grid_semanas_simuladas.setColumnCount(17)
        # self.grid_semanas_simuladas.setHorizontalHeaderLabels([])

    def limpiar_interfaz(self):

        # Limpio txts
        self.txt_cantidad_semanas.clear()
        self.txt_semana_desde.clear()
        self.txt_semana_hasta.clear()
        self.txt_probabilidad_0_demanda.clear()
        self.txt_probabilidad_1_demanda.clear()
        self.txt_probabilidad_2_demanda.clear()
        self.txt_probabilidad_3_demanda.clear()
        self.txt_probabilidad_1_tiempo_entrega.clear()
        self.txt_probabilidad_2_tiempo_entrega.clear()
        self.txt_probabilidad_3_tiempo_entrega.clear()
        self.txt_probabilidad_bicicleta_daniada.clear()
        self.txt_costo_tenencia.clear()
        self.txt_costo_pedido.clear()
        self.txt_costo_agotamiento.clear()
        self.txt_stock_minimo.clear()

        # Cargo valores por defecto en txts
        self.txt_probabilidad_0_demanda.setText("50")
        self.txt_probabilidad_1_demanda.setText("15")
        self.txt_probabilidad_2_demanda.setText("25")
        self.txt_probabilidad_3_demanda.setText("10")
        self.txt_probabilidad_1_tiempo_entrega.setText("30")
        self.txt_probabilidad_2_tiempo_entrega.setText("40")
        self.txt_probabilidad_3_tiempo_entrega.setText("30")
        self.txt_probabilidad_bicicleta_daniada.setText("30")
        self.txt_costo_tenencia.setText("3")
        self.txt_costo_pedido.setText("20")
        self.txt_costo_agotamiento.setText("5")
        self.txt_stock_minimo.setText("2")

    def limpiar_tabla(self):

        # Limpio grilla de semanas simuladas
        self.grid_semanas_simuladas.clearSelection()
        self.grid_semanas_simuladas.setCurrentCell(-1, -1)
        self.grid_semanas_simuladas.setRowCount(0)

    def mostrar_mensaje(self, titulo, mensaje):

        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def cargar_tabla_semanas_simuladas(self):
        pass

    """ Eventos """

    # Evento show
    def showEvent(self, QShowEvent):
        self.preparar_interfaz()
        self.limpiar_interfaz()
