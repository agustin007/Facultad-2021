import random
from decimal import Decimal

from soporte.helper import *

from montecarlo.soporte.helper import SIXPLACES


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
    stock_inicial = None
    stock_minimo = None

    def simular_semana(self, vector_estado):

        # Obtengo semana recorrida
        semana = vector_estado.get("semana") + 1

        # Obtengo demanda semanal
        rnd_demanda = truncar(random.random(), 2)
        limite_demanda_0 = self.probabilidad_0_demanda / 100
        limite_demanda_1 = limite_demanda_0 + (self.probabilidad_1_demanda / 100)
        limite_demanda_2 = limite_demanda_1 + (self.probabilidad_2_demanda / 100)
        if 0 < rnd_demanda < limite_demanda_0:
            demanda = 0
        elif limite_demanda_0 <= rnd_demanda < limite_demanda_1:
            demanda = 1
        elif limite_demanda_1 <= rnd_demanda < limite_demanda_2:
            demanda = 2
        else:
            demanda = 3

        # Obtengo stock de la semana anterior
        stock = vector_estado.get("stock")

        # Si tiene que llegar un pedido esta semana, verifico si hay una bicicleta dañada para actualizar el stock
        rnd_bicicleta_daniada = None
        bicicleta_daniada = None
        semana_proxima_entrega = vector_estado.get("semana_proxima_entrega")
        if semana == semana_proxima_entrega:
            semana_proxima_entrega = None
            rnd_bicicleta_daniada = truncar(random.random(), 2)
            limite_demanda_bicicleta_daniada = self.probabilidad_bicicleta_daniada / 100
            if 0 < rnd_bicicleta_daniada < limite_demanda_bicicleta_daniada:
                bicicleta_daniada = True
            else:
                bicicleta_daniada = False
            if bicicleta_daniada:
                stock += 5
            else:
                stock += 6

        # Verifico si se cumple la demanda para obtener las ventas perdidas y actualizar el stock
        ventas_perdidas = None
        if demanda <= stock:
            stock -= demanda
        else:
            ventas_perdidas = demanda - stock
            stock = 0

        # Verifico si debe realizarse un pedido
        rnd_tiempo_entrega = None
        tiempo_entrega = None
        if stock <= self.stock_minimo and semana_proxima_entrega is None:
            rnd_tiempo_entrega = truncar(random.random(), 2)
            limite_tiempo_entrega_1 = self.probabilidad_1_tiempo_entrega / 100
            limite_tiempo_entrega_2 = limite_tiempo_entrega_1 + (self.probabilidad_2_tiempo_entrega / 100)
            if 0 < rnd_tiempo_entrega < limite_tiempo_entrega_1:
                tiempo_entrega = 1
            elif limite_tiempo_entrega_1 <= rnd_tiempo_entrega < limite_tiempo_entrega_2:
                tiempo_entrega = 2
            else:
                tiempo_entrega = 3
            semana_proxima_entrega = semana + tiempo_entrega

        # Calculo costos
        costo_tenencia = 0 if stock == 0 else stock * self.costo_tenencia
        costo_pedido = 0 if rnd_tiempo_entrega is None else self.costo_pedido
        costo_agotamiento = 0 if ventas_perdidas is None else ventas_perdidas * self.costo_agotamiento

        costo_total = costo_tenencia + costo_pedido + costo_agotamiento
        costo_total_acumulado = costo_total + vector_estado.get("costo_total_acumulado")
        costo_total_promedio = Decimal((((semana - 1) * vector_estado.get("costo_total_acumulado"))
                                        + costo_total) / semana).quantize(SIXPLACES)

        # Armo nuevo vector de estado
        vector_estado = {
            "semana": semana,
            "rnd_demanda": rnd_demanda,
            "demanda": demanda,
            "rnd_tiempo_entrega": rnd_tiempo_entrega,
            "tiempo_entrega": tiempo_entrega,
            "rnd_bicicleta_daniada": rnd_bicicleta_daniada,
            "bicicleta_daniada": bicicleta_daniada,
            "semana_proxima_entrega": semana_proxima_entrega,
            "stock": stock,
            "ventas_perdidas": ventas_perdidas,
            "costo_tenencia": costo_tenencia,
            "costo_pedido": costo_pedido,
            "costo_agotamiento": costo_agotamiento,
            "costo_total": costo_total,
            "costo_total_acumulado": costo_total_acumulado,
            "costo_total_promedio": costo_total_promedio.quantize(TWOPLACES)
        }

        return vector_estado

    def simular_semanas(self, cantidad_semanas, semana_desde, semana_hasta, probabilidad_0_demanda,
                        probabilidad_1_demanda, probabilidad_2_demanda, probabilidad_3_demanda,
                        probabilidad_1_tiempo_entrega, probabilidad_2_tiempo_entrega, probabilidad_3_tiempo_entrega,
                        probabilidad_bicicleta_daniada, costo_tenencia, costo_pedido, costo_agotamiento, stock_inicial,
                        stock_minimo):

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
        self.stock_inicial = stock_inicial
        self.stock_minimo = stock_minimo

        # Genero vector de estado inicial
        vector_estado = {
            "semana": 0,
            "rnd_demanda": None,
            "demanda": None,
            "rnd_tiempo_entrega"
            "tiempo_entrega": None,
            "rnd_bicicleta_daniada": None,
            "bicicleta_daniada": None,
            "semana_proxima_entrega": None,
            "stock": stock_inicial,
            "ventas_perdidas": None,
            "costo_tenencia": 0,
            "costo_pedido": 0,
            "costo_agotamiento": 0,
            "costo_total": 0,
            "costo_total_acumulado": 0,
            "costo_total_promedio": 0
        }

        # Realizo simulación almacenando los vectores estados de las semanas de interés
        dias_simulados = [vector_estado]
        for i in range(1, cantidad_semanas + 1):
            vector_estado = self.simular_semana(vector_estado)
            if semana_desde <= i <= semana_hasta:
                dias_simulados.append(vector_estado)
        if semana_hasta < cantidad_semanas:
            dias_simulados.append(vector_estado)

        # Devuelvo semanas simuladas de interés
        return dias_simulados

