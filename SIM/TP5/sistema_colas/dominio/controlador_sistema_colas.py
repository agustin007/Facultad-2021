import random
from soporte.helper import *


class ControladorSistemaColas:

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

    def simular_semana(self, vector_estado):
        pass
        """
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
        """

    def simular_iteraciones(self, tiempo_simulacion, tiempo_desde, cantidad_iteraciones, tiempo_autos,
                            probabilidad_chico_autos, probabilidad_grande_autos, probabilidad_utilitario_autos,
                            probabilidad_1_tiempo_estacionamiento, probabilidad_2_tiempo_estacionamiento,
                            probabilidad_3_tiempo_estacionamiento, probabilidad_4_tiempo_estacionamiento,
                            cantidad_cabinas_cobro, tiempo_cobro):

        # Agrego datos como atributos del objeto para poder manejarlos a nivel clase
        self.tiempo_autos = tiempo_autos
        self.probabilidad_chico_autos = probabilidad_chico_autos
        self.probabilidad_grande_autos = probabilidad_grande_autos
        self.probabilidad_utilitario_autos = probabilidad_utilitario_autos
        self.probabilidad_1_tiempo_estacionamiento = probabilidad_1_tiempo_estacionamiento
        self.probabilidad_2_tiempo_estacionamiento = probabilidad_2_tiempo_estacionamiento
        self.probabilidad_3_tiempo_estacionamiento = probabilidad_3_tiempo_estacionamiento
        self.probabilidad_4_tiempo_estacionamiento = probabilidad_4_tiempo_estacionamiento
        self.cantidad_cabinas_cobro = cantidad_cabinas_cobro
        self.tiempo_cobro = tiempo_cobro

        # Genero vector de estado inicial
        rnd_tiempo_entre_llegadas = truncar(random.random(), 2)
        vector_estado = {
            "evento": "inicializacion",
            "reloj": 0,
            "eventos": {
                "llegada_autos": {
                    "rnd_tiempo_entre_llegadas": rnd_tiempo_entre_llegadas,
                    "tiempo_proxima_llegada": Decimal(-1 * self.tiempo_autos * math.log(rnd_tiempo_entre_llegadas))
                        .quantize(TWOPLACES),
                    "proxima_llegada": None,
                },
                "fin_estacionamiento": {
                    "rnd_fin_estacionamiento": None,
                    "tiempo_estacionado": None,
                    "fines_tiempo_estacionado": []
                },
                "fin_cobrado": {
                    "tiempo_cobrado": None,
                    "fines_cobrado": []
                },
            },
            "servidores": {
                "lugares_estacionamiento": [],
                "cabinas_cobro": []
            },
            "contadores": {
                "autos_rechazados": 0,
                "monto_recaudado": 0,
                "porcentaje_ocupacion": 0,
                "porcentaje_ocupacion_promedio": 0,
            },
            "clientes": {
                "auxiliares": {
                    "rnd_tipo_auto": None,
                    "tipo_auto": None
                },
                "autos": [
                    {
                        "n_auto": 1,
                        "estado": None
                    }
                ]
            }
        }
        fines_tiempo_estacionamiento = []
        lugares_estacionamiento = []
        for i in range(1, 20+1):
            fines_tiempo_estacionamiento.append({
                "n_lugar_estacionamiento": i,
                "fin_tiempo_estacionado": None
            })
            lugares_estacionamiento.append({
                "n_lugar_estacionamiento": i,
                "estado": "Libre"
            })
        vector_estado["eventos"]["fin_estacionamiento"]["fines_tiempo_estacionado"] = fines_tiempo_estacionamiento
        vector_estado["servidores"]["lugares_estacionamiento"] = lugares_estacionamiento
        fines_cobrado = []
        cabinas_cobro = []
        for i in range(1, self.cantidad_cabinas_cobro+1):
            fines_cobrado.append({
                "n_cabina_cobro": i,
                "fin_cobrado": None
            })
            cabinas_cobro.append({
                "n_cabina_cobro": i,
                "estado": "Libre",
                "cola": 0
            })
        vector_estado["eventos"]["fin_cobrado"]["fines_cobrado"] = fines_cobrado
        vector_estado["servidores"]["cabinas_cobro"] = cabinas_cobro

        # Realizo simulación almacenando los vectores estados de las iteraciones de interés
        iteraciones_simuladas = [vector_estado]
        """
        for i in range(1, cantidad_semanas + 1):
            vector_estado = self.simular_semana(vector_estado)
            if semana_desde <= i <= semana_hasta:
                dias_simulados.append(vector_estado)
        if semana_hasta < cantidad_semanas:
            dias_simulados.append(vector_estado)
        """

        # Devuelvo semanas simuladas de interés
        return iteraciones_simuladas

