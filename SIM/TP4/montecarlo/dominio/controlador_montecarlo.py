from decimal import Decimal


class ControladorMontecarlo:

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

    def simular_semana(self, vector_estado):
        pass

    def simular_semanas(self, cantidad_semanas, semana_desde, semana_hasta, probabilidad_0_demanda,
                        probabilidad_1_demanda, probabilidad_2_demanda, probabilidad_3_demanda,
                        probabilidad_1_tiempo_entrega, probabilidad_2_tiempo_entrega, probabilidad_3_tiempo_entrega,
                        probabilidad_bicicleta_daniada, costo_tenencia, costo_pedido, costo_agotamiento, stock_minimo):

        # Agrego datos como atributos del objeto para poder manejarlos a nivel clase
        self.probabilidad_0_demanda = probabilidad_0_demanda
        self.probabilidad_1_demanda = probabilidad_1_demanda
        self.probabilidad_2_demanda = probabilidad_2_demanda
        self.probabilidad_3_demanda = probabilidad_3_demanda
        self.probabilidad_1_tiempo_entrega = probabilidad_1_tiempo_entrega
        self.probabilidad_2_tiempo_entrega = probabilidad_2_tiempo_entrega
        self.probabilidad_3_tiempo_entrega = probabilidad_3_tiempo_entrega
        self.probabilidad_bicicleta_daniada = probabilidad_bicicleta_daniada
        self.costo_tenencia = costo_tenencia
        self.costo_pedido = costo_pedido
        self.costo_agotamiento = costo_agotamiento
        self.stock_minimo = stock_minimo

        # Genero vector de estado inicial
