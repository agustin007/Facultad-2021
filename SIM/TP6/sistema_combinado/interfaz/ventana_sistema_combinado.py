from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from dominio.controlador_sistema_combinado import *
from soporte.validador_enteros import ValidadorEnteros
from soporte.validador_decimales import ValidadorDecimales
from soporte.ruta import Ruta


class VentanaSistemaCombinado(QMainWindow):

    """ Atributos """

    app = None
    controlador = None
    iteraciones_simuladas = None

    pagina_actual = None
    cantidad_paginas = None
    tamanio_pagina = 100

    """ Constructor """

    def __init__(self, app):

        # Guardo app
        self.app = app

        # Genero ventana a partir de ui y creo controlador
        QMainWindow.__init__(self)
        uic.loadUi(Ruta.generar_ruta("interfaz/ventana_sistema_combinado.ui"), self)
        self.controlador = ControladorSistemaCombinado(self)

        # Agrego validadores a los campos
        validador_7_enteros = ValidadorEnteros(7)
        validador_4_enteros = ValidadorEnteros(4)
        validador_3_enteros = ValidadorEnteros(3)
        validador_decimales = ValidadorDecimales(6, 6)
        self.txt_tiempo_simulacion.setValidator(validador_7_enteros)
        self.txt_tiempo_desde.setValidator(validador_7_enteros)
        self.txt_cantidad_iteraciones.setValidator(validador_7_enteros)
        self.txt_tiempo_autos.setValidator(validador_3_enteros)
        self.txt_probabilidad_chico_autos.setValidator(validador_3_enteros)
        self.txt_probabilidad_grande_autos.setValidator(validador_3_enteros)
        self.txt_probabilidad_utilitario_autos.setValidator(validador_3_enteros)
        self.txt_probabilidad_1_tiempo_estacionamiento.setValidator(validador_3_enteros)
        self.txt_probabilidad_2_tiempo_estacionamiento.setValidator(validador_3_enteros)
        self.txt_probabilidad_3_tiempo_estacionamiento.setValidator(validador_3_enteros)
        self.txt_probabilidad_4_tiempo_estacionamiento.setValidator(validador_3_enteros)
        self.txt_cantidad_lugares_estacionamiento.setValidator(validador_4_enteros)
        self.txt_cantidad_cabinas_cobro.setValidator(validador_4_enteros)
        self.txt_h.setValidator(validador_decimales)
        self.txt_t.setValidator(validador_decimales)

        # Conecto los botones con los eventos
        self.btn_pagina_anterior_1.clicked.connect(self.accion_volver_1_pagina)
        self.btn_pagina_anterior_10.clicked.connect(self.accion_volver_10_paginas)
        self.btn_pagina_siguiente_1.clicked.connect(self.accion_siguiente_1_pagina)
        self.btn_pagina_siguiente_10.clicked.connect(self.accion_siguiente_10_paginas)
        self.btn_limpiar.clicked.connect(self.accion_limpiar)
        self.btn_simular.clicked.connect(self.accion_simular)

    """ Acciones """

    def accion_volver_1_pagina(self):

        # verifico que se haya realizado una simulación
        if self.iteraciones_simuladas is not None:

            # Calculo nueva página controlando límites
            nueva_pagina = self.pagina_actual
            if (nueva_pagina - 1) < 1:
                nueva_pagina = 1
            else:
                nueva_pagina -= 1

            # Vuelvo a carga la tabla si corresponde
            if nueva_pagina != self.pagina_actual:
                self.pagina_actual = nueva_pagina
                self.cargar_tabla_iteraciones_simuladas()
                self.lbl_informacion_paginas.setText(str(self.pagina_actual) + "/" + str(self.cantidad_paginas))

    def accion_volver_10_paginas(self):

        # verifico que se haya realizado una simulación
        if self.iteraciones_simuladas is not None:

            # Calculo nueva página controlando límites
            nueva_pagina = self.pagina_actual
            if (nueva_pagina - 10) < 1:
                nueva_pagina = 1
            else:
                nueva_pagina -= 10

            # Vuelvo a carga la tabla si corresponde
            if nueva_pagina != self.pagina_actual:
                self.pagina_actual = nueva_pagina
                self.cargar_tabla_iteraciones_simuladas()
                self.lbl_informacion_paginas.setText(str(self.pagina_actual) + "/" + str(self.cantidad_paginas))

    def accion_siguiente_1_pagina(self):

        # verifico que se haya realizado una simulación
        if self.iteraciones_simuladas is not None:

            # Calculo nueva página controlando límites
            nueva_pagina = self.pagina_actual
            if (nueva_pagina + 1) > self.cantidad_paginas:
                nueva_pagina = self.cantidad_paginas
            else:
                nueva_pagina += 1

            # Vuelvo a carga la tabla si corresponde
            if nueva_pagina != self.pagina_actual:
                self.pagina_actual = nueva_pagina
                self.cargar_tabla_iteraciones_simuladas()
                self.lbl_informacion_paginas.setText(str(self.pagina_actual) + "/" + str(self.cantidad_paginas))

    def accion_siguiente_10_paginas(self):

        # verifico que se haya realizado una simulación
        if self.iteraciones_simuladas is not None:

            # Calculo nueva página controlando límites
            nueva_pagina = self.pagina_actual
            if (nueva_pagina + 10) > self.cantidad_paginas:
                nueva_pagina = self.cantidad_paginas
            else:
                nueva_pagina += 10

            # Vuelvo a carga la tabla si corresponde
            if nueva_pagina != self.pagina_actual:
                self.pagina_actual = nueva_pagina
                self.cargar_tabla_iteraciones_simuladas()
                self.lbl_informacion_paginas.setText(str(self.pagina_actual) + "/" + str(self.cantidad_paginas))

    def accion_limpiar(self):

        # Restauro valores por defecto de interfaz y limpio tabla
        self.limpiar_datos()
        self.limpiar_interfaz()
        self.limpiar_tabla()
        self.preparar_tabla()
        self.mostrar_porcentaje_simulacion()
        self.mostrar_porcentaje_datos()
        self.mostrar_cantidad_iteraciones_realizadas()

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
        cantidad_lugares_estacionamiento = None
        cantidad_cabinas_cobro = None
        h = None
        t = None
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
        if self.txt_cantidad_lugares_estacionamiento.text() != "":
            cantidad_lugares_estacionamiento = int(self.txt_cantidad_lugares_estacionamiento.text())
        if self.txt_cantidad_cabinas_cobro.text() != "":
            cantidad_cabinas_cobro = int(self.txt_cantidad_cabinas_cobro.text())
        if self.txt_h.text() != "":
            h = float(self.txt_h.text().replace(",", "."))
        if self.txt_t.text() != "":
            t = float(self.txt_t.text().replace(",", "."))

        # Valido parametros
        if tiempo_simulacion is None or tiempo_simulacion <= 0:
            self.mostrar_mensaje("Error", "El tiempo a simular tiene que ser mayor a cero")
            return
        if tiempo_desde is None:
            self.mostrar_mensaje("Error", "El tiempo desde el cuál mostrar la simulación no puede ser vacío")
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
        if cantidad_lugares_estacionamiento is None or cantidad_lugares_estacionamiento <= 0:
            self.mostrar_mensaje("Error", "La cantidad de lugares de estacionamiento tiene que ser mayor a cero")
            return
        if cantidad_cabinas_cobro is None or cantidad_cabinas_cobro <= 0:
            self.mostrar_mensaje("Error", "La cantidad de cabinas de cobro tiene que ser mayor a cero")
            return
        if h is None or h <= 0:
            self.mostrar_mensaje("Error", "El parámetro h tiene que ser mayor a cero")
            return
        if t is None:
            self.mostrar_mensaje("Error", "El parámetro T no puede ser vacío")
            return

        # Limpio elementos de interfaz
        self.limpiar_tabla()
        self.mostrar_porcentaje_simulacion()
        self.mostrar_porcentaje_datos()
        self.mostrar_cantidad_iteraciones_realizadas()

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
                                                                          cantidad_lugares_estacionamiento,
                                                                          cantidad_cabinas_cobro, h, t)

        # Obtengo datos necesarios para generacion de headers
        ids_lugares_estacionamiento = self.iteraciones_simuladas[0].get("informacion_simulacion") \
            .get("ids_lugares_estacionamiento")
        ids_cabinas_cobro = self.iteraciones_simuladas[0].get("informacion_simulacion").get("ids_cabinas_cobro")
        ids_autos = self.iteraciones_simuladas[0].get("informacion_simulacion").get("ids_autos")

        # Preparo headers de tabla de acuerdo a iteraciones simuladas
        self.preparar_tabla(ids_lugares_estacionamiento, ids_cabinas_cobro, ids_autos)

        # Muestro dato de cantidad iteraciones efectivas realizadas
        self.mostrar_cantidad_iteraciones_realizadas(self.iteraciones_simuladas[-1].get("n_iteracion"))

        # Calculo y seteo datos de paginación y iteraciones efectivas realizadas
        self.pagina_actual = 1
        self.cantidad_paginas = math.ceil(len(self.iteraciones_simuladas) / self.tamanio_pagina)
        self.lbl_informacion_paginas.setText(str(self.pagina_actual) + "/" + str(self.cantidad_paginas))

        # Cargo tabla
        self.cargar_tabla_iteraciones_simuladas()

    """ Metodos """

    def obtener_pagina_iteraciones_simuladas(self):

        # Obtengo página a partir de datos de paginación
        if len(self.iteraciones_simuladas) < self.tamanio_pagina:
            pagina = self.iteraciones_simuladas[0:len(self.iteraciones_simuladas)]
        else:
            index_inf = (self.pagina_actual - 1) * self.tamanio_pagina
            index_sup = index_inf + self.tamanio_pagina
            if index_sup > len(self.iteraciones_simuladas):
                index_sup = len(self.iteraciones_simuladas)
            pagina = self.iteraciones_simuladas[index_inf:index_sup]

        return pagina

    def preparar_tabla(self, ids_lugares_estacionamiento=None, ids_cabinas_cobro=None, ids_autos=None):

        # Genero listas vacias en caso de parametros None
        if ids_lugares_estacionamiento is None:
            ids_lugares_estacionamiento = [0]
        if ids_cabinas_cobro is None:
            ids_cabinas_cobro = [0]
        if ids_autos is None:
            ids_autos = [0]

        # Preparo tabla de semanas simuladas
        cantidad_lugares_estacionamiento = len(ids_lugares_estacionamiento)
        cantidad_cabinas_cobro = len(ids_cabinas_cobro)
        cantidad_autos = len(ids_autos)
        self.grid_iteraciones_simuladas.setColumnCount(14 + cantidad_lugares_estacionamiento * 2 +
                                                       cantidad_cabinas_cobro * 3 + cantidad_autos * 3)
        i = 0

        header = QTableWidgetItem("N° de iteración")
        header.setBackground(QColor(204, 204, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        header = QTableWidgetItem("Evento")
        header.setBackground(QColor(204, 204, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        header = QTableWidgetItem("Reloj")
        header.setBackground(QColor(204, 204, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1

        header = QTableWidgetItem("RND")
        header.setBackground(QColor(255, 242, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        header = QTableWidgetItem("T. prox. llegada")
        header.setBackground(QColor(255, 242, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        header = QTableWidgetItem("Prox. llegada")
        header.setBackground(QColor(255, 242, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1

        header = QTableWidgetItem("RND")
        header.setBackground(QColor(217, 234, 211))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        header = QTableWidgetItem("T. estac.")
        header.setBackground(QColor(217, 234, 211))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        for id_lugar_estacionamiento in ids_lugares_estacionamiento:
            header = QTableWidgetItem("F. estac. (" + str(id_lugar_estacionamiento) + ")")
            header.setBackground(QColor(217, 234, 211))
            self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
            i += 1

        header = QTableWidgetItem("T. cobrando")
        header.setBackground(QColor(208, 224, 227))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1

        for id_cabina_cobro in ids_cabinas_cobro:
            header = QTableWidgetItem("F. cobrado (" + str(id_cabina_cobro) + ")")
            header.setBackground(QColor(208, 224, 227))
            self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
            i += 1

        for id_lugar_estacionamiento in ids_lugares_estacionamiento:
            header = QTableWidgetItem("Estado l. estac. (" + str(id_lugar_estacionamiento) + ")")
            header.setBackground(QColor(217, 210, 233))
            self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
            i += 1

        for id_cabina_cobro in ids_cabinas_cobro:
            header = QTableWidgetItem("Estado c. cobro (" + str(id_cabina_cobro) + ")")
            header.setBackground(QColor(234, 209, 220))
            self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
            i += 1
            header = QTableWidgetItem("Cola c. cobro (" + str(id_cabina_cobro) + ")")
            header.setBackground(QColor(234, 209, 220))
            self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
            i += 1

        header = QTableWidgetItem("A. rechazados")
        header.setBackground(QColor(244, 204, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        header = QTableWidgetItem("Monto recaudado")
        header.setBackground(QColor(244, 204, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        header = QTableWidgetItem("Porc. ocup.")
        header.setBackground(QColor(244, 204, 204))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1

        header = QTableWidgetItem("RND")
        header.setBackground(QColor(249, 203, 156))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1
        header = QTableWidgetItem("Tipo auto")
        header.setBackground(QColor(249, 203, 156))
        self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
        i += 1

        for id_auto in ids_autos:
            header = QTableWidgetItem("Estado auto (" + str(id_auto) + ")")
            header.setBackground(QColor(234, 153, 153))
            self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
            i += 1
            header = QTableWidgetItem("H. inicio esp. (" + str(id_auto) + ")")
            header.setBackground(QColor(234, 153, 153))
            self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
            i += 1
            header = QTableWidgetItem("Monto (" + str(id_auto) + ")")
            header.setBackground(QColor(234, 153, 153))
            self.grid_iteraciones_simuladas.setHorizontalHeaderItem(i, header)
            i += 1

    def limpiar_datos(self):

        # Limpio datos
        self.iteraciones_simuladas = None
        self.pagina_actual = None
        self.cantidad_paginas = None

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
        self.txt_h.clear()
        self.txt_t.clear()

        # Limpio labels relacionados con paginación e iteraciones a mostrar
        self.lbl_informacion_paginas.setText("0/0")
        self.lbl_informacion_cantidad_iteraciones_realizadas.setText("0")

        # Cargo valores por defecto en txts
        self.txt_tiempo_autos.setText("13")
        self.txt_probabilidad_chico_autos.setText("45")
        self.txt_probabilidad_grande_autos.setText("25")
        self.txt_probabilidad_utilitario_autos.setText("30")
        self.txt_probabilidad_1_tiempo_estacionamiento.setText("50")
        self.txt_probabilidad_2_tiempo_estacionamiento.setText("30")
        self.txt_probabilidad_3_tiempo_estacionamiento.setText("15")
        self.txt_probabilidad_4_tiempo_estacionamiento.setText("5")
        self.txt_cantidad_lugares_estacionamiento.setText("20")
        self.txt_cantidad_cabinas_cobro.setText("1")
        self.txt_h.setText("0,5")
        self.txt_t.setText("10")

    def limpiar_tabla(self):

        # Limpio grilla de semanas simuladas
        self.grid_iteraciones_simuladas.clearSelection()
        self.grid_iteraciones_simuladas.setCurrentCell(-1, -1)
        self.grid_iteraciones_simuladas.setRowCount(0)

    def mostrar_porcentaje_simulacion(self, porcenjate=0):
        porcenjate_str = str(porcenjate).replace(".", ",")
        self.lbl_informacion_porcentaje_simulacion.setText(porcenjate_str)
        self.app.processEvents()

    def mostrar_porcentaje_datos(self, porcenjate=0):
        porcenjate_str = str(porcenjate).replace(".", ",")
        self.lbl_informacion_porcentaje_datos.setText(porcenjate_str)
        self.app.processEvents()

    def mostrar_cantidad_iteraciones_realizadas(self, cantidad_iteraciones=0):
        cantidad_iteraciones_str = str(cantidad_iteraciones)
        self.lbl_informacion_cantidad_iteraciones_realizadas.setText(cantidad_iteraciones_str)
        self.app.processEvents()

    def mostrar_mensaje(self, titulo, mensaje):

        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def cargar_tabla_iteraciones_simuladas(self):

        # Obtengo datos necesarios para generacion de headers
        ids_lugares_estacionamiento = self.iteraciones_simuladas[0].get("informacion_simulacion") \
            .get("ids_lugares_estacionamiento")
        ids_cabinas_cobro = self.iteraciones_simuladas[0].get("informacion_simulacion").get("ids_cabinas_cobro")
        ids_autos = self.iteraciones_simuladas[0].get("informacion_simulacion").get("ids_autos")

        # Obtengo pagina de iteraciones simuladas a mostrar
        iteraciones_a_mostrar = self.obtener_pagina_iteraciones_simuladas()

        # Calculo cada cuantas finlas mostrar el porcentaje de datos cargados
        if len(iteraciones_a_mostrar) <= 100:
            paso_muestra_datos = 1
        else:
            paso_muestra_datos = round(len(iteraciones_a_mostrar) / 50)
        proxima_muestra_datos = paso_muestra_datos

        # Genero filas de tabla
        self.grid_iteraciones_simuladas.setRowCount(len(iteraciones_a_mostrar))
        index_f = 0
        for iteracion_a_mostrar in iteraciones_a_mostrar:
            index_c = 0

            # Obtengo datos en formato conveniente y agrego a fila
            n_iteracion = iteracion_a_mostrar.get("n_iteracion")
            n_iteracion_str = str(n_iteracion)
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(n_iteracion_str))
            index_c += 1

            evento_str = iteracion_a_mostrar.get("evento")
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(evento_str))
            index_c += 1

            reloj = iteracion_a_mostrar.get("reloj")
            reloj_str = str(reloj).replace(".", ",") if reloj is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(reloj_str))
            index_c += 1

            rnd_tiempo_entre_llegadas = iteracion_a_mostrar.get("eventos").get("llegada_autos")\
                .get("rnd_tiempo_entre_llegadas")
            rnd_tiempo_entre_llegadas_str = str(rnd_tiempo_entre_llegadas).replace(".", ",") \
                if rnd_tiempo_entre_llegadas is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(rnd_tiempo_entre_llegadas_str))
            index_c += 1

            tiempo_proxima_llegada = iteracion_a_mostrar.get("eventos").get("llegada_autos")\
                .get("tiempo_proxima_llegada")
            tiempo_proxima_llegada_str = str(tiempo_proxima_llegada).replace(".", ",") \
                if tiempo_proxima_llegada is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(tiempo_proxima_llegada_str))
            index_c += 1

            proxima_llegada = iteracion_a_mostrar.get("eventos").get("llegada_autos").get("proxima_llegada")
            proxima_llegada_str = str(proxima_llegada).replace(".", ",") if proxima_llegada is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(proxima_llegada_str))
            index_c += 1

            rnd_fin_estacionamiento = iteracion_a_mostrar.get("eventos").get("fin_estacionamiento")\
                .get("rnd_fin_estacionamiento")
            rnd_fin_estacionamiento_str = str(rnd_fin_estacionamiento).replace(".", ",") \
                if rnd_fin_estacionamiento is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(rnd_fin_estacionamiento_str))
            index_c += 1

            tiempo_estacionamiento = iteracion_a_mostrar.get("eventos").get("fin_estacionamiento") \
                .get("tiempo_estacionamiento")
            tiempo_estacionamiento_str = str(tiempo_estacionamiento) if tiempo_estacionamiento is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(tiempo_estacionamiento_str))
            index_c += 1

            for i in range(0, len(ids_lugares_estacionamiento)):
                fin_estacionamiento = iteracion_a_mostrar.get("eventos").get("fin_estacionamiento")\
                    .get("fines_estacionamiento")[i].tiempo_fin_evento
                fin_estacionamiento_str = str(fin_estacionamiento).replace(".", ",") \
                    if fin_estacionamiento is not None else ""
                self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(fin_estacionamiento_str))
                index_c += 1

            tiempo_cobrado = iteracion_a_mostrar.get("eventos").get("fin_cobrado").get("tiempo_cobrado")
            tiempo_cobrado_str = str(tiempo_cobrado).replace(".", ",") if tiempo_cobrado is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(tiempo_cobrado_str))
            index_c += 1

            for i in range(0, len(ids_cabinas_cobro)):
                fin_cobrado = iteracion_a_mostrar.get("eventos").get("fin_cobrado")\
                    .get("fines_cobrado")[i].tiempo_fin_evento
                fin_cobrado_str = str(fin_cobrado).replace(".", ",") if fin_cobrado is not None else ""
                self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(fin_cobrado_str))
                index_c += 1

            for i in range(0, len(ids_lugares_estacionamiento)):
                estado_str = iteracion_a_mostrar.get("servidores").get("lugares_estacionamiento")[i].estado
                self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(estado_str))
                index_c += 1

            for i in range(0, len(ids_cabinas_cobro)):
                estado_str = iteracion_a_mostrar.get("servidores").get("cabinas_cobro")[i].estado
                self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(estado_str))
                index_c += 1
                cola = iteracion_a_mostrar.get("servidores").get("cabinas_cobro")[i].cola
                cola_str = str(cola)
                self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(cola_str))
                index_c += 1

            autos_rechazados = iteracion_a_mostrar.get("contadores").get("autos_rechazados")
            autos_rechazados_str = str(autos_rechazados)
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(autos_rechazados_str))
            index_c += 1

            monto_recaudado = iteracion_a_mostrar.get("contadores").get("monto_recaudado")
            monto_recaudado_str = "$ " + str(monto_recaudado)
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(monto_recaudado_str))
            index_c += 1

            porcentaje_ocupacion = iteracion_a_mostrar.get("contadores").get("porcentaje_ocupacion")
            porcentaje_ocupacion_str = (str(porcentaje_ocupacion).replace(".", ",")
                                        if porcentaje_ocupacion is not None else "") + " %"
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(porcentaje_ocupacion_str))
            index_c += 1

            rnd_tipo_auto = iteracion_a_mostrar.get("clientes").get("auxiliares").get("rnd_tipo_auto")
            rnd_tipo_auto_str = str(rnd_tipo_auto).replace(".", ",") if rnd_tipo_auto is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(rnd_tipo_auto_str))
            index_c += 1

            tipo_auto = iteracion_a_mostrar.get("clientes").get("auxiliares").get("tipo_auto")
            tipo_auto_str = str(tipo_auto) if tipo_auto is not None else ""
            self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(tipo_auto_str))
            index_c += 1

            if ids_autos is not None:
                index_ids_autos_totales = 0
                index_ids_autos_iteracion = 0
                while index_ids_autos_totales < len(ids_autos):
                    auto_encontrado = False
                    try:
                        if ids_autos[index_ids_autos_totales] == iteracion_a_mostrar.get("clientes")\
                                .get("autos")[index_ids_autos_iteracion].id:
                            auto_encontrado = True
                    except IndexError:
                        pass

                    if auto_encontrado:
                        auto = iteracion_a_mostrar.get("clientes").get("autos")[index_ids_autos_iteracion]
                        estado_str = auto.estado
                        if auto.lugar_estacionamiento is not None:
                            estado_str += " (" + str(auto.lugar_estacionamiento.id) + ")"
                        elif auto.cabina_cobro is not None:
                            estado_str += "(" + str(auto.cabina_cobro.id) + ")"
                        self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(estado_str))
                        index_c += 1
                        hora_inicio_espera_para_pagar = auto.hora_inicio_espera_para_pagar
                        hora_inicio_espera_para_pagar_str = str(hora_inicio_espera_para_pagar).replace(".", ",") \
                            if hora_inicio_espera_para_pagar is not None else ""
                        self.grid_iteraciones_simuladas.setItem(index_f, index_c,
                                                                QTableWidgetItem(hora_inicio_espera_para_pagar_str))
                        index_c += 1
                        monto = auto.monto
                        monto_str = "$ " + str(monto) if monto is not None else ""
                        self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(monto_str))
                        index_c += 1

                        index_ids_autos_totales += 1
                        index_ids_autos_iteracion += 1

                    else:
                        estado_str = ""
                        self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(estado_str))
                        index_c += 1
                        hora_inicio_espera_para_pagar_str = ""
                        self.grid_iteraciones_simuladas.setItem(index_f, index_c,
                                                                QTableWidgetItem(hora_inicio_espera_para_pagar_str))
                        index_c += 1
                        monto_str = ""
                        self.grid_iteraciones_simuladas.setItem(index_f, index_c, QTableWidgetItem(monto_str))
                        index_c += 1

                        index_ids_autos_totales += 1

            index_f += 1

            # Muestro porcentaje de datos cargados cuando corresponda
            if index_f >= proxima_muestra_datos:
                porcentaje = round(index_f * 100 / len(iteraciones_a_mostrar))
                self.mostrar_porcentaje_datos(porcentaje)
                while proxima_muestra_datos <= index_f:
                    proxima_muestra_datos += paso_muestra_datos

        # Muestro porcentaje de datos cargados final
        self.mostrar_porcentaje_datos(100)

    """ Eventos """

    # Evento show
    def showEvent(self, QShowEvent):
        self.accion_limpiar()
