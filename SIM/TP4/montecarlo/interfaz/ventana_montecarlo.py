from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
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
        validador_2_enteros = ValidadorEnteros(2)
        self.txt_cantidad_semanas.setValidator(validador_6_enteros)
        self.txt_semana_desde.setValidator(validador_6_enteros)
        self.txt_semana_hasta.setValidator(validador_6_enteros)
        self.txt_probabilidad_0_demanda.setValidator(validador_2_enteros)
        self.txt_probabilidad_1_demanda.setValidator(validador_2_enteros)
        self.txt_probabilidad_2_demanda.setValidator(validador_2_enteros)
        self.txt_probabilidad_3_demanda.setValidator(validador_2_enteros)
        self.txt_probabilidad_1_tiempo_entrega.setValidator(validador_2_enteros)
        self.txt_probabilidad_2_tiempo_entrega.setValidator(validador_2_enteros)
        self.txt_probabilidad_3_tiempo_entrega.setValidator(validador_2_enteros)
        self.txt_probabilidad_bicicleta_daniada.setValidator(validador_2_enteros)
        self.txt_costo_tenencia.setValidator(validador_4_enteros)
        self.txt_costo_pedido.setValidator(validador_4_enteros)
        self.txt_costo_agotamiento.setValidator(validador_4_enteros)
        self.txt_stock_minimo.setValidator(validador_4_enteros)

        # Conecto los botones con los eventos
        self.btn_limpiar.clicked.connect(self.accion_limpiar)
        self.btn_simular.clicked.connect(self.accion_simular)

    """ Acciones """

    def accion_limpiar(self):

        # Restauro valores por defecto de interfaz
        self.limpiar_interfaz()

    def accion_simular(self):
        pass

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

    def cargar_tabla_semanas_simuladas(self):
        pass

    """ Eventos """

    # Evento show
    def showEvent(self, QShowEvent):
        self.preparar_interfaz()
        self.limpiar_interfaz()
