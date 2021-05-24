from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from dominio.controlador_sistema_colas import ControladorSistemaColas
from soporte.validador_enteros import ValidadorEnteros
from soporte.ruta import Ruta


class VentanaSistemaColas(QMainWindow):
    """ Atributos """

    controlador = None
    iteraciones_simuladas = {}

    """ Constructor """

    def __init__(self):

        # Genero ventana a partir de ui y creo controlador
        QMainWindow.__init__(self)
        uic.loadUi(Ruta.generar_ruta("interfaz/ventana_sistema_colas.ui"), self)
        self.controlador = ControladorSistemaColas()

        # Agrego validadores a los campos
        validador_6_enteros = ValidadorEnteros(6)
        validador_4_enteros = ValidadorEnteros(4)
        validador_3_enteros = ValidadorEnteros(3)
        self.txt_tiempo_simulacion.setValidator(validador_6_enteros)
        self.txt_tiempo_desde.setValidator(validador_6_enteros)
        self.txt_cantidad_iteraciones.setValidator(validador_6_enteros)
        self.txt_tiempo_autos.setValidator(validador_3_enteros)
        self.txt_probabilidad_chico_autos.setValidator(validador_3_enteros)
        self.txt_probabilidad_grande_autos.setValidator(validador_3_enteros)
        self.txt_probabilidad_utilitario_autos.setValidator(validador_3_enteros)
        self.txt_probabilidad_1_tiempo_estacionamiento.setValidator(validador_3_enteros)
        self.txt_probabilidad_2_tiempo_estacionamiento.setValidator(validador_3_enteros)
        self.txt_probabilidad_3_tiempo_estacionamiento.setValidator(validador_3_enteros)
        self.txt_probabilidad_4_tiempo_estacionamiento.setValidator(validador_3_enteros)
        self.txt_cantidad_cabinas_cobro.setValidator(validador_4_enteros)
        self.txt_tiempo_cobro.setValidator(validador_4_enteros)

        # Conecto los botones con los eventos
        self.btn_limpiar.clicked.connect(self.accion_limpiar)
        self.btn_simular.clicked.connect(self.accion_simular)

    """ Acciones """

    def accion_limpiar(self):

        # Restauro valores por defecto de interfaz y limpio tabla
        self.iteraciones_simuladas = []
        self.preparar_tabla()
        self.limpiar_interfaz()

    def accion_simular(self):

        # Obtengo parametros verificando que no sean vacios
        tiempo_simulacion = None
        tiempo_desde = None
        cantidad_iteraciones = None
        tiempo_autos = None
        probabilidad_chico_autos = None
        probabilidad_grande_autos = None
        probabilidad_utilitario_autos = None
        probabilidad_1_tiempo_estacionamiento = None
        probabilidad_2_tiempo_estacionamiento = None
        probabilidad_3_tiempo_estacionamiento = None
        probabilidad_4_tiempo_estacionamiento = None
        cantidad_cabinas_cobro = None
        tiempo_cobro = None
        if self.txt_tiempo_simulacion.text() != "":
            tiempo_simulacion = int(self.txt_tiempo_simulacion.text())
        if self.txt_tiempo_desde.text() != "":
            tiempo_desde = int(self.txt_tiempo_desde.text())
        if self.txt_cantidad_iteraciones.text() != "":
            cantidad_iteraciones = int(self.txt_cantidad_iteraciones.text())
        if self.txt_tiempo_autos.text() != "":
            tiempo_autos = int(self.txt_tiempo_autos.text())
        if self.txt_probabilidad_chico_autos.text() != "":
            probabilidad_chico_autos = int(self.txt_probabilidad_chico_autos.text())
        if self.txt_probabilidad_grande_autos.text() != "":
            probabilidad_grande_autos = int(self.txt_probabilidad_grande_autos.text())
        if self.txt_probabilidad_utilitario_autos.text() != "":
            probabilidad_utilitario_autos = int(self.txt_probabilidad_utilitario_autos.text())
        if self.txt_probabilidad_1_tiempo_estacionamiento.text() != "":
            probabilidad_1_tiempo_estacionamiento = int(self.txt_probabilidad_1_tiempo_estacionamiento.text())
        if self.txt_probabilidad_2_tiempo_estacionamiento.text() != "":
            probabilidad_2_tiempo_estacionamiento = int(self.txt_probabilidad_2_tiempo_estacionamiento.text())
        if self.txt_probabilidad_3_tiempo_estacionamiento.text() != "":
            probabilidad_3_tiempo_estacionamiento = int(self.txt_probabilidad_3_tiempo_estacionamiento.text())
        if self.txt_probabilidad_4_tiempo_estacionamiento.text() != "":
            probabilidad_4_tiempo_estacionamiento = int(self.txt_probabilidad_4_tiempo_estacionamiento.text())
        if self.txt_cantidad_cabinas_cobro.text() != "":
            cantidad_cabinas_cobro = int(self.txt_cantidad_cabinas_cobro.text())
        if self.txt_tiempo_cobro.text() != "":
            tiempo_cobro = int(self.txt_tiempo_cobro.text())

        # Valido parametros
        if tiempo_simulacion is None or tiempo_simulacion <= 0:
            self.mostrar_mensaje("Error", "El tiempo a simular tiene que ser mayor a cero")
            return
        if tiempo_desde is None or tiempo_desde <= 0:
            self.mostrar_mensaje("Error", "El tiempo desde el cuál mostrar la simulación tiene que ser mayor a cero")
            return
        if cantidad_iteraciones is None or cantidad_iteraciones <= 0:
            self.mostrar_mensaje("Error", "La cantidad de iteraciones a mostrar de la simulación tiene que ser mayor a "
                                          "cero")
            return
        if tiempo_desde > tiempo_simulacion:
            self.mostrar_mensaje("Error", "El tiempo desde el cuál mostrar la simulación no puede ser mayor a la "
                                          "cantidad de tiempo simulado")
            return
        if tiempo_autos is None or tiempo_autos <= 0:
            self.mostrar_mensaje("Error", "El tiempo de llegada medio entre autos tiene que ser mayor a cero")
            return
        if probabilidad_chico_autos is None:
            self.mostrar_mensaje("Error", "La probabilidad de que los autos que llegan sean chicos no puede ser vacía")
            return
        if probabilidad_grande_autos is None:
            self.mostrar_mensaje("Error", "La probabilidad de que los autos que llegan sean grandes no puede ser vacía")
            return
        if probabilidad_utilitario_autos is None:
            self.mostrar_mensaje("Error", "La probabilidad de que los autos que llegan sean utilitarios no puede ser "
                                          "vacía")
            return
        if (probabilidad_chico_autos + probabilidad_grande_autos + probabilidad_utilitario_autos) != 100:
            self.mostrar_mensaje("Error", "Las probabilidades de tamaños de los autos que llegan deben sumar un 100%")
            return
        if probabilidad_1_tiempo_estacionamiento is None:
            self.mostrar_mensaje("Error", "La probabilidad de que el tiempo de estacionamiento sea de 1 hora no puede "
                                          "ser vacía")
            return
        if probabilidad_2_tiempo_estacionamiento is None:
            self.mostrar_mensaje("Error", "La probabilidad de que el tiempo de estacionamiento sea de 2 horas no puede "
                                          "ser vacía")
        if probabilidad_3_tiempo_estacionamiento is None:
            self.mostrar_mensaje("Error", "La probabilidad de que el tiempo de estacionamiento sea de 3 horas no puede "
                                          "ser vacía")
        if probabilidad_4_tiempo_estacionamiento is None:
            self.mostrar_mensaje("Error", "La probabilidad de que el tiempo de estacionamiento sea de 4 horas no puede "
                                          "ser vacía")
        if (probabilidad_1_tiempo_estacionamiento + probabilidad_2_tiempo_estacionamiento +
                probabilidad_3_tiempo_estacionamiento + probabilidad_4_tiempo_estacionamiento) != 100:
            self.mostrar_mensaje("Error", "Las probabilidades de tiempo de estacionamiento deben sumar un 100%")
            return
        if cantidad_cabinas_cobro is None or cantidad_cabinas_cobro <= 0:
            self.mostrar_mensaje("Error", "La cantidad de cabinas de cobro tiene que ser mayor a cero")
            return
        if tiempo_cobro is None or tiempo_cobro <= 0:
            self.mostrar_mensaje("Error", "El tiempo de cobro de cobro tiene que ser mayor a cero")
            return

        # Realizo simulacion y obtengo semanas a mostrar
        self.iteraciones_simuladas = self.controlador.simular_iteraciones(tiempo_simulacion, tiempo_desde,
                                                                          cantidad_iteraciones, tiempo_autos,
                                                                          probabilidad_chico_autos,
                                                                          probabilidad_grande_autos,
                                                                          probabilidad_utilitario_autos,
                                                                          probabilidad_1_tiempo_estacionamiento,
                                                                          probabilidad_2_tiempo_estacionamiento,
                                                                          probabilidad_3_tiempo_estacionamiento,
                                                                          probabilidad_4_tiempo_estacionamiento,
                                                                          cantidad_cabinas_cobro, tiempo_cobro)

        # Cargo tabla
        self.cargar_tabla_iteraciones_simuladas()

    """ Metodos """

    def preparar_tabla(self):

        """
        # Preparo tabla de semanas simuladas
        self.grid_semanas_simuladas.setColumnCount(16)
        self.grid_semanas_simuladas.setHorizontalHeaderLabels(["Semana", "RND", "Demanda", "RND", "Tiempo de entrega",
                                                               "RND", "Bicicleta dañada", "S. próxima entrega",
                                                               "Stock actual", "Ventas perdidas", "Costo tenencia",
                                                               "Costo pedido", "Costo agotamiento", "Costo total",
                                                               "Costo total acum.", "Costo promedio"])
        """

    def limpiar_interfaz(self):

        # Limpio txts
        self.txt_tiempo_simulacion.clear()
        self.txt_tiempo_desde.clear()
        self.txt_cantidad_iteraciones.clear()
        self.txt_tiempo_autos.clear()
        self.txt_probabilidad_chico_autos.clear()
        self.txt_probabilidad_grande_autos.clear()
        self.txt_probabilidad_utilitario_autos.clear()
        self.txt_probabilidad_1_tiempo_estacionamiento.clear()
        self.txt_probabilidad_2_tiempo_estacionamiento.clear()
        self.txt_probabilidad_3_tiempo_estacionamiento.clear()
        self.txt_probabilidad_4_tiempo_estacionamiento.clear()
        self.txt_cantidad_cabinas_cobro.clear()
        self.txt_tiempo_cobro.clear()

        # Cargo valores por defecto en txts
        self.txt_tiempo_autos.setText("13")
        self.txt_probabilidad_chico_autos.setText("45")
        self.txt_probabilidad_grande_autos.setText("25")
        self.txt_probabilidad_utilitario_autos.setText("30")
        self.txt_probabilidad_1_tiempo_estacionamiento.setText("50")
        self.txt_probabilidad_2_tiempo_estacionamiento.setText("30")
        self.txt_probabilidad_3_tiempo_estacionamiento.setText("15")
        self.txt_probabilidad_4_tiempo_estacionamiento.setText("5")
        self.txt_cantidad_cabinas_cobro.setText("1")
        self.txt_tiempo_cobro.setText("2")

    def limpiar_tabla(self):

        # Limpio grilla de semanas simuladas
        self.grid_iteraciones_simuladas.clearSelection()
        self.grid_iteraciones_simuladas.setCurrentCell(-1, -1)
        self.grid_iteraciones_simuladas.setRowCount(0)

        # prepa

    def mostrar_mensaje(self, titulo, mensaje):

        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def cargar_tabla_iteraciones_simuladas(self):
        pass
        """
        self.grid_semanas_simuladas.setRowCount(len(self.semanas_simuladas))
        index = 0
        for semana_simulada in self.semanas_simuladas:
            # Obtengo datos en formato conveniente

            semana = str(semana_simulada.get("semana")) if semana_simulada.get("semana") is not None else ""
            rnd_demanda = str(semana_simulada.get("rnd_demanda")).replace(".", ",") if semana_simulada.get(
                "rnd_demanda") is not None else ""
            demanda = str(semana_simulada.get("demanda")) if semana_simulada.get("demanda") is not None else ""
            rnd_tiempo_entrega = str(semana_simulada.get("rnd_tiempo_entrega")).replace(".", ",") \
                if semana_simulada.get("rnd_tiempo_entrega") is not None else ""
            tiempo_entrega = str(semana_simulada.get("tiempo_entrega")) if semana_simulada.get("tiempo_entrega") \
                                                                           is not None else ""
            rnd_bicicleta_daniada = str(semana_simulada.get("rnd_bicicleta_daniada")).replace(".", ",") \
                if semana_simulada.get("rnd_bicicleta_daniada") is not None else ""
            bicicleta_daniada = "" if semana_simulada.get("bicicleta_daniada") is None else \
                "Si" if semana_simulada.get("bicicleta_daniada") else "No"
            semana_proxima_entrega = str(semana_simulada.get("semana_proxima_entrega")) \
                if semana_simulada.get("semana_proxima_entrega") is not None else ""
            stock = str(semana_simulada.get("stock")) if semana_simulada.get("stock") is not None else ""
            ventas_perdidas = str(semana_simulada.get("ventas_perdidas")) if semana_simulada.get("ventas_perdidas") \
                                                                             is not None else ""
            costo_tenencia = "$ " + str(semana_simulada.get("costo_tenencia"))
            costo_pedido = "$ " + str(semana_simulada.get("costo_pedido"))
            costo_agotamiento = "$ " + str(semana_simulada.get("costo_agotamiento"))
            costo_total = "$ " + str(semana_simulada.get("costo_total"))
            costo_total_acumulado = "$ " + str(semana_simulada.get("costo_total_acumulado"))
            costo_total_promedio = "$ " + str(semana_simulada.get("costo_total_promedio")).replace(".", ",")

            # Agrego fila a tabla
            self.grid_semanas_simuladas.setItem(index, 0, QTableWidgetItem(semana))
            self.grid_semanas_simuladas.setItem(index, 1, QTableWidgetItem(rnd_demanda))
            self.grid_semanas_simuladas.setItem(index, 2, QTableWidgetItem(demanda))
            self.grid_semanas_simuladas.setItem(index, 3, QTableWidgetItem(rnd_tiempo_entrega))
            self.grid_semanas_simuladas.setItem(index, 4, QTableWidgetItem(tiempo_entrega))
            self.grid_semanas_simuladas.setItem(index, 5, QTableWidgetItem(rnd_bicicleta_daniada))
            self.grid_semanas_simuladas.setItem(index, 6, QTableWidgetItem(bicicleta_daniada))
            self.grid_semanas_simuladas.setItem(index, 7, QTableWidgetItem(semana_proxima_entrega))
            self.grid_semanas_simuladas.setItem(index, 8, QTableWidgetItem(stock))
            self.grid_semanas_simuladas.setItem(index, 9, QTableWidgetItem(ventas_perdidas))
            self.grid_semanas_simuladas.setItem(index, 10, QTableWidgetItem(costo_tenencia))
            self.grid_semanas_simuladas.setItem(index, 11, QTableWidgetItem(costo_pedido))
            self.grid_semanas_simuladas.setItem(index, 12, QTableWidgetItem(costo_agotamiento))
            self.grid_semanas_simuladas.setItem(index, 13, QTableWidgetItem(costo_total))
            self.grid_semanas_simuladas.setItem(index, 14, QTableWidgetItem(costo_total_acumulado))
            self.grid_semanas_simuladas.setItem(index, 15, QTableWidgetItem(costo_total_promedio))
            index += 1

        """

    """ Eventos """

    # Evento show
    def showEvent(self, QShowEvent):
        self.preparar_tabla()
        self.limpiar_interfaz()
