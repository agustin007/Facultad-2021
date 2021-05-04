from decimal import Decimal
import random

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

        #variables que reflejan el stock
        
        stock = 7
        stock_reabastecimiento = 6
        stock_minimo = 2

        #variables asociadas a la demanda y al tiempo de espera por pedido

        demanda = 0
        tiempo_entrega = 0

        #variables asociadas a los costos de inventario

        costo_agotamiento = 3
        costo_tenencia = 5
        costo_pedido = 20
        costo_total = 0


        for i in  range(0,cantidad_semanas):

            demanda_random = random.random()
            entrega_random = random.random()
            daniado_random = random.random()

            if demanda_random < 0.5:

                demanda = 0
                stock = stock - demanda

            elif demanda_random >= 0.5 and demanda_random < 0.65:

                demanda = 1
                stock = stock - demanda

            elif demanda_random >= 0.65 and demanda_random < 0.8:

                demanda = 2
                stock = stock - demanda


            elif demanda_random < 0.8:

                demanda = 3
                stock = stock - demanda


            if stock == stock_minimo or stock < stock_minimo :

                if entrega_random < 0.3 :

                    tiempo_entrega = 1

                elif entrega_random >= 0.3 and entrega_random < 0.7:

                    tiempo_entrega = 2

                elif entrega_random > 0.7:

                    tiempo_entrega = 3

            if stock < demanda :

                costo_total = costo_agotamiento * (demanda - stock)

            elif stock > demanda:

                costo_total = (costo_tenencia * demanda) + (costo_tenencia * (stock - demanda))
                
                stock = stock - demanda










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
