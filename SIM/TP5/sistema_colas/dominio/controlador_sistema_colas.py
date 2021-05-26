import math
import random
from decimal import Decimal
from statistics import mean

from soporte.helper import *

from sistema_colas.soporte.helper import truncar, TWOPLACES


class ControladorSistemaColas:

    tiempo_simulacion = None
    tiempo_desde = None
    cantidad_iteraciones = None
    tiempo_autos = None
    proxima_llegada = 0
    probabilidad_chico_autos = None
    probabilidad_grande_autos = None
    probabilidad_utilitario_autos = None
    probabilidad_1_tiempo_estacionamiento = None
    probabilidad_2_tiempo_estacionamiento = None
    probabilidad_3_tiempo_estacionamiento = None
    probabilidad_4_tiempo_estacionamiento = None
    cantidad_cabinas_cobro = None
    tiempo_cobro = None

    estado_auto = None

    def simular_iteracion(self, vector_estado):

        #Obtengo el evento
        evento = vector_estado.get("evento")

        #Realizo la trnasicion del primer estado
        if(evento == "inicializacion"):
            evento == "llegada_autos"

        #Obtengo la hora
        tiempo_autos = vector_estado.get("reloj")
        if(evento == "llegada_autos"):
            tiempo_autos += vector_estado.get("tiempo_proxima_llegada")
            estado_auto = "Estacionado"
        elif(evento == "fin_estacionamiento"):
            tiempo_autos += vector_estado.get("tiempo_estacionado")
            # Obtengo las cabinas de cobro para luego saber si el auto tiene que esperar o no
            cabinas_cobro = vector_estado["servidores"]["cabinas_cobro"]

            for i in range(1 , cabinas_cobro.len + 1 ):
                if(i["cola"] != 0):
                    estado_auto = "EsperandoPagar"
                else:
                    # Ya que es fin de estacionamiento obtengo el tiempo de cobro y el fin de cobro
                    tiempo_cobrado = 2
                    fines_cobrado = tiempo_autos + tiempo_cobrado

        elif(evento == "fin_cobrado"):
            tiempo_autos += self.vector_estado.get("tiempo_cobrado")
            estado_auto = "Pagando"

        #Obtengo llegada auto
        rnd_tiempo_entre_llegadas = truncar(random.random(), 2)
        tiempo_proxima_llegada = Decimal(-1 * rnd_tiempo_entre_llegadas * math.log(rnd_tiempo_entre_llegadas)).quantize(TWOPLACES)
        self.proxima_llegada += self.proxima_llegada + tiempo_proxima_llegada

        #Obtengo fin estacionamiento
        rnd_fin_estacionamiento = truncar(random.random(), 2)
        limite_fin_estacinamiento_1 = self.probabilidad_1_tiempo_estacionamiento / 100
        limite_fin_estacinamiento_2 = limite_fin_estacinamiento_1 + (self.probabilidad_2_tiempo_estacionamiento / 100)
        limite_fin_estacinamiento_3 = limite_fin_estacinamiento_2 + (self.probabilidad_3_tiempo_estacionamiento / 100)
        if( 0 < rnd_fin_estacionamiento < limite_fin_estacinamiento_1):
            tiempo_estacionado = 1
        elif( limite_fin_estacinamiento_1 < rnd_fin_estacionamiento < limite_fin_estacinamiento_2):
            tiempo_estacionado = 2
        elif( limite_fin_estacinamiento_2 < rnd_fin_estacionamiento < limite_fin_estacinamiento_3):
            tiempo_estacionado = 3
        else:
            tiempo_estacionado = 4
        fines_tiempo_estacionado = tiempo_autos + tiempo_estacionado

        #Valido que haya lugar en el estacionamiento
        lugares_estacionamiento = vector_estado.get("lugares_estacionamiento");
        autos_rechazados = vector_estado["contadores"]["autos_rechazados"]
        for i in range(1, lugares_estacionamiento.len):
            if(i["estado"] == "Libre"):
                i["estado"] = "Ocupado"
                i["n_lugar_estacionamiento"] = i
                """Agregar auto que esta en ese lugar ? """
            else:
                autos_rechazados += 1

        #Obtengo el tipo de auto si llega un nuevo auto
        if(evento == "llegada_autos"):
            rnd_tipo_auto = truncar(random.random(), 2)
            limite_tipo_auto_chico = self.probabilidad_chico_autos / 100
            limite_tipo_auto_grande = limite_tipo_auto_chico + (self.probabilidad_grande_autos / 100)
            limite_tipo_auto_utilitario = limite_tipo_auto_grande + (self.probabilidad_utilitario_autos / 100)
            if( 0 < rnd_tipo_auto < limite_tipo_auto_chico):
                tipo_auto = 1
            elif( limite_tipo_auto_chico < rnd_tipo_auto < limite_tipo_auto_grande):
                tipo_auto = 2
            else:
                tipo_auto = 3

            auxiliar = {
                "rnd_tipo_auto":rnd_tipo_auto,
                "tipo_auto": tipo_auto
            }
            autos = vector_estado.get["clientes"]["autos"]
            autos.append({
                "n_auto": tipo_auto,
                "estado": estado_auto
            })
        elif(evento == "fin_estacionamiento"):
            #Mantengo los datos
            auxiliar = vector_estado["clientes"]["auxiliares"]
            auto = vector_estado.get["clientes"]["autos"].pop()
            autos = vector_estado.get["clientes"]["autos"]
            autos.append(auto)

            #Realizo el cobro
            monto_recaudado = vector_estado["contadores"]["monto_recaudado"]
            ingreso_a_cabina = False
            for i in range(1 , cabinas_cobro.len + 1 ):
                if(cabinas_cobro[i]["estado"] == "Libre"):
                    cabinas_cobro[i]["estado"] = "Ocupada"
                    ingreso_a_cabina = True
                if(ingreso_a_cabina == False & (cabinas_cobro[i]["estado"] == "Ocupada" & cabinas_cobro[i]["cola"] == 0)):
                    cabinas_cobro[i]["estado"] = "Ocupada"
                    cabinas_cobro[i]["cola"] = 1
                    ingreso_a_cabina = True
                if(ingreso_a_cabina == True):
                    """if(tipo_auto == ""):"""

                    break
        porcentaje_ocupacion = 0
        porcentaje_ocupacion_promedio = 0

        # Armo nuevo vector de estado
        vector_estado = {
            "evento": evento,
            "reloj": tiempo_autos,
            "eventos": {
                "llegada_autos": {
                    "rnd_tiempo_entre_llegadas": rnd_tiempo_entre_llegadas,
                    "tiempo_proxima_llegada": tiempo_proxima_llegada,
                    "proxima_llegada": self.proxima_llegada,
                },

                "fin_estacionamiento": {
                    "rnd_fin_estacionamiento": rnd_fin_estacionamiento,
                    "tiempo_estacionado": tiempo_estacionado,
                    "fines_tiempo_estacionado": fines_tiempo_estacionado,
                },
                "fin_cobrado": {
                    "tiempo_cobrado": tiempo_cobrado,
                    "fines_cobrado": fines_cobrado,
                }
            },
            "servidores": {
                "lugares_estacionamiento": lugares_estacionamiento,
                "cabinas_cobro": cabinas_cobro,
            },
            "contadores": {
                "autos_rechazados": autos_rechazados,
                "monto_recaudado": monto_recaudado,
                "porcentaje_ocupacion": porcentaje_ocupacion,
                "porcentaje_ocupacion_promedio": porcentaje_ocupacion_promedio,
            },
            "clientes": {
                "auxiliares": auxiliar,
                "autos": autos
            }
        }

        return vector_estado


    def simular_iteraciones(self, tiempo_simulacion, tiempo_desde, cantidad_iteraciones, tiempo_autos,
                            probabilidad_chico_autos, probabilidad_grande_autos, probabilidad_utilitario_autos,
                            probabilidad_1_tiempo_estacionamiento, probabilidad_2_tiempo_estacionamiento,
                            probabilidad_3_tiempo_estacionamiento, probabilidad_4_tiempo_estacionamiento,
                            cantidad_cabinas_cobro, tiempo_cobro):

        # Agrego datos como atributos del objeto para poder manejarlos a nivel clase
        self.tiempo_simulacion = tiempo_simulacion
        self.tiempo_desde = tiempo_desde
        self.cantidad_iteraciones = cantidad_iteraciones
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

        for i in range(1, cantidad_iteraciones + 1):
            vector_estado = self.simular_iteracion(vector_estado)
            if(tiempo_desde <= i <= cantidad_iteraciones):
                iteraciones_simuladas.append(vector_estado)
            if( cantidad_iteraciones < tiempo_simulacion):
                iteraciones_simuladas.append(vector_estado)

        # Devuelvo semanas simuladas de interés
        return iteraciones_simuladas

