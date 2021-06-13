import random
import bisect
import copy
from dominio.clases.clientes import *
from dominio.clases.servidores import *
from dominio.clases.eventos import *
from soporte.helper import *


class ControladorSistemaColas:

    # Atributos
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
    tiempo_cobro = None

    ultimo_id_auto = 0

    # Constantes
    EVENTO_LLEGADA_AUTO = "llegada_auto"
    EVENTO_FIN_ESTACIONAMIENTO = "fin_estacionamiento"
    EVENTO_FIN_COBRADO = "fin_cobrado"

    def simular_iteracion(self, vector_estado):

        # Copio vector estado anterior para realizar las acciones necesarias de esta iteración sin modificar el anterior
        vector_estado = copy.deepcopy(vector_estado)

        # Quito datos auxiliares de demás eventos innecesarios para nuevo vector estado
        vector_estado["eventos"]["llegada_autos"]["rnd_tiempo_entre_llegadas"] = None
        vector_estado["eventos"]["llegada_autos"]["tiempo_proxima_llegada"] = None
        vector_estado["eventos"]["fin_estacionamiento"]["rnd_fin_estacionamiento"] = None
        vector_estado["eventos"]["fin_estacionamiento"]["tiempo_estacionamiento"] = None
        vector_estado["eventos"]["fin_cobrado"]["tiempo_cobrado"] = None
        vector_estado["clientes"]["auxiliares"]["rnd_tipo_auto"] = None
        vector_estado["clientes"]["auxiliares"]["tipo_auto"] = None

        # Establezco criterios de ordenamiento para agilizar el algoritmo
        Servidor.ordenar_por = ORDEN_SERVIDORES_POR_ESTADO
        Evento.ordenar_por = ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO

        # Obtengo siguiente evento a procesar
        evento = None
        reloj_evento = None
        servidor_a_liberar = None

        proxima_llegada = vector_estado.get("eventos").get("llegada_autos").get("proxima_llegada")
        if proxima_llegada is not None:
            evento = self.EVENTO_LLEGADA_AUTO
            reloj_evento = proxima_llegada

        menor_fin_estacionamiento = vector_estado.get("eventos").get("fin_estacionamiento") \
            .get("fines_estacionamiento")[0]
        if menor_fin_estacionamiento.tiempo_fin_evento is not None and \
                menor_fin_estacionamiento.tiempo_fin_evento < reloj_evento:
            evento = self.EVENTO_FIN_ESTACIONAMIENTO
            reloj_evento = menor_fin_estacionamiento.tiempo_fin_evento
            servidor_a_liberar = menor_fin_estacionamiento.servidor

        menor_fin_cobrado = vector_estado.get("eventos").get("fin_cobrado").get("fines_cobrado")[0]
        if menor_fin_cobrado.tiempo_fin_evento is not None and \
                menor_fin_cobrado.tiempo_fin_evento < reloj_evento:
            evento = self.EVENTO_FIN_COBRADO
            reloj_evento = menor_fin_cobrado.tiempo_fin_evento
            servidor_a_liberar = menor_fin_cobrado.servidor

        # Seteo nuevo evento en vector
        vector_estado["reloj"] = reloj_evento
        vector_estado["evento"] = evento
        if servidor_a_liberar is not None:
            vector_estado["evento"] += " (" + str(servidor_a_liberar.id) + ")"

        # Realizo acciones dependiendo del evento

        # Evento llegada_autos
        if evento == self.EVENTO_LLEGADA_AUTO:

            # Aumento contador de ids de auto
            self.ultimo_id_auto += 1

            # Completo datos de evento sabiendo a que auto se refiere
            vector_estado["evento"] += " (" + str(self.ultimo_id_auto) + ")"

            # Genero próxima llegada
            rnd_tiempo_entre_llegadas = truncar(random.random(), 2)
            tiempo_proxima_llegada = round(-1 * self.tiempo_autos * math.log(1 - rnd_tiempo_entre_llegadas), 2)
            proxima_llegada = round(reloj_evento + tiempo_proxima_llegada, 2)

            # Seteo datos de próxima llegada en vector estado
            vector_estado["eventos"]["llegada_autos"]["rnd_tiempo_entre_llegadas"] = rnd_tiempo_entre_llegadas
            vector_estado["eventos"]["llegada_autos"]["tiempo_proxima_llegada"] = tiempo_proxima_llegada
            vector_estado["eventos"]["llegada_autos"]["proxima_llegada"] = proxima_llegada

            # Verifico si existe al menos algún lugar del estacionamiento libre, para pasarlo a ocupado
            lugar_estacionamiento_encontrado = None
            primer_lugar_estacionamiento_vacio = vector_estado.get("servidores").get("lugares_estacionamiento")[0]
            if primer_lugar_estacionamiento_vacio.estado == ESTADO_SERVIDOR_LIBRE:
                lugar_estacionamiento_encontrado = vector_estado.get("servidores").get("lugares_estacionamiento").pop(0)
                lugar_estacionamiento_encontrado.estado = ESTADO_SERVIDOR_OCUPADO
                bisect.insort(vector_estado.get("servidores").get("lugares_estacionamiento"),
                              lugar_estacionamiento_encontrado)

            # Si se encontró lugar de estacionamiento
            if lugar_estacionamiento_encontrado is not None:

                # Genero fin estacionamiento para el auto recién llegado
                rnd_fin_estacionamiento = truncar(random.random(), 2)
                limite_tiempo_estacionamiento_1 = self.probabilidad_1_tiempo_estacionamiento / 100
                limite_tiempo_estacionamiento_2 = limite_tiempo_estacionamiento_1 \
                                                  + self.probabilidad_2_tiempo_estacionamiento / 100
                limite_tiempo_estacionamiento_3 = limite_tiempo_estacionamiento_2 \
                                                  + self.probabilidad_3_tiempo_estacionamiento / 100
                if 0 <= rnd_fin_estacionamiento < limite_tiempo_estacionamiento_1:
                    tiempo_estacionamiento = 60
                elif limite_tiempo_estacionamiento_1 <= rnd_fin_estacionamiento < limite_tiempo_estacionamiento_2:
                    tiempo_estacionamiento = 120
                elif limite_tiempo_estacionamiento_2 <= rnd_fin_estacionamiento < limite_tiempo_estacionamiento_3:
                    tiempo_estacionamiento = 180
                else:
                    tiempo_estacionamiento = 240
                fin_tiempo_estacionado = round(reloj_evento + tiempo_estacionamiento, 2)

                # Seteo datos de fin tiempo estacionado
                vector_estado["eventos"]["fin_estacionamiento"]["rnd_fin_estacionamiento"] = rnd_fin_estacionamiento
                vector_estado["eventos"]["fin_estacionamiento"]["tiempo_estacionamiento"] = tiempo_estacionamiento
                index = None
                for i in range(0, len(vector_estado.get("eventos").get("fin_estacionamiento").get(
                        "fines_estacionamiento"))):
                    if vector_estado.get("eventos").get("fin_estacionamiento").get("fines_estacionamiento")\
                            [i].servidor.id == lugar_estacionamiento_encontrado.id:
                        index = i
                        break
                fin_estacionamiento = vector_estado.get("eventos").get("fin_estacionamiento").get(
                    "fines_estacionamiento").pop(index)
                fin_estacionamiento.tiempo_fin_evento = fin_tiempo_estacionado
                bisect.insort(vector_estado.get("eventos").get("fin_estacionamiento").get("fines_estacionamiento"),
                              fin_estacionamiento)

                # Genero auxiliares para generación de auto
                rnd_tipo_auto = truncar(random.random(), 2)
                limite_autos_chico = self.probabilidad_chico_autos / 100
                limite_autos_grande = limite_autos_chico + self.probabilidad_grande_autos / 100
                if 0 <= rnd_tipo_auto < limite_autos_chico:
                    tipo_auto = TIPO_AUTO_CHICO
                elif limite_autos_chico <= rnd_tipo_auto < limite_autos_grande:
                    tipo_auto = TIPO_AUTO_GRANDE
                else:
                    tipo_auto = TIPO_AUTO_UTILITARIO

                # Seteo datos auxiliares para geneación de auto
                vector_estado["clientes"]["auxiliares"]["rnd_tipo_auto"] = rnd_tipo_auto
                vector_estado["clientes"]["auxiliares"]["tipo_auto"] = tipo_auto

                # Genero auto con sus atributos correspondientes
                id_auto = self.ultimo_id_auto
                estado_auto = ESTADO_AUTO_ESTACIONADO
                lugar_estacionamiento_auto = lugar_estacionamiento_encontrado
                cabina_cobro_auto = None
                hora_inicio_espera_para_pagar_auto = None
                if tipo_auto == TIPO_AUTO_CHICO:
                    monto_auto = int(50 * tiempo_estacionamiento / 60)
                elif tipo_auto == TIPO_AUTO_GRANDE:
                    monto_auto = int(80 * tiempo_estacionamiento / 60)
                else:
                    monto_auto = int(100 * tiempo_estacionamiento / 60)

                vector_estado.get("clientes").get("autos").append(
                    Auto(id_auto, estado_auto, lugar_estacionamiento_auto, cabina_cobro_auto,
                         hora_inicio_espera_para_pagar_auto, monto_auto)
                )
                # Seteo datos de contadores
                vector_estado["contadores"]["lugares_estacionamiento_ocupados"] += 1
                porcentaje_ocupacion = round(vector_estado.get("contadores").get("lugares_estacionamiento_ocupados")
                                             * 100 / self.cantidad_lugares_estacionamiento, 2)
                vector_estado["contadores"]["porcentaje_ocupacion"] = porcentaje_ocupacion

            # Si no se encontró lugar de estacionamiento
            else:

                # Seteo datos de contadores
                vector_estado["contadores"]["autos_rechazados"] += 1

        # Evento fin_estacionamiento
        elif evento == self.EVENTO_FIN_ESTACIONAMIENTO:

            # Borro dato de fin de estacionamiento
            fin_estacionamiento = vector_estado.get("eventos").get("fin_estacionamiento") \
                .get("fines_estacionamiento").pop(0)
            fin_estacionamiento.tiempo_fin_evento = None
            bisect.insort(vector_estado.get("eventos").get("fin_estacionamiento").get("fines_estacionamiento"),
                          fin_estacionamiento)

            # Verifico si existe al menos algúna cabina de cobro libre, para pasarla a ocupada o agregar uno a la cola
            # que menos tenga
            cabina_cobro_encontrada = None
            cabina_cobro_con_menos_cola_encontrada = None
            primer_cabina_cobro_vacia = vector_estado.get("servidores").get("cabinas_cobro")[0]
            if primer_cabina_cobro_vacia.estado == ESTADO_SERVIDOR_LIBRE:
                cabina_cobro_encontrada = vector_estado.get("servidores").get("cabinas_cobro").pop(0)
                cabina_cobro_encontrada.estado = ESTADO_SERVIDOR_OCUPADO
                bisect.insort(vector_estado.get("servidores").get("cabinas_cobro"),
                              cabina_cobro_encontrada)
            else:
                aux_menor_cola = None
                for cabina_cobro in vector_estado.get("servidores").get("cabinas_cobro"):
                    if cabina_cobro_con_menos_cola_encontrada is None or cabina_cobro.cola < aux_menor_cola:
                        cabina_cobro_con_menos_cola_encontrada = cabina_cobro
                        aux_menor_cola = cabina_cobro_con_menos_cola_encontrada.cola
            if not cabina_cobro_encontrada:
                cabina_cobro_con_menos_cola_encontrada.cola += 1

            # Si se encontró cabina de cobro
            if cabina_cobro_encontrada is not None:

                # Seteo datos de lugar de estacionamiento, ya que se desocupa el lugar
                index = None
                for i in range(0, len(vector_estado.get("servidores").get("lugares_estacionamiento"))):
                    if vector_estado.get("servidores").get("lugares_estacionamiento")[i].id == servidor_a_liberar.id:
                        index = i
                        break
                lugar_estacionamiento = vector_estado.get("servidores").get("lugares_estacionamiento").pop(index)
                lugar_estacionamiento.estado = ESTADO_SERVIDOR_LIBRE
                bisect.insort(vector_estado.get("servidores").get("lugares_estacionamiento"),
                              lugar_estacionamiento)

                # Genero fin cobrado para el auto que recién termina su estacionamiento
                tiempo_cobrado = self.tiempo_cobro
                fin_tiempo_cobrado = round(reloj_evento + tiempo_cobrado, 2)

                # Seteo datos de fin cobrado
                vector_estado["eventos"]["fin_cobrado"]["tiempo_cobrado"] = tiempo_cobrado
                index = None
                for i in range(0, len(vector_estado.get("eventos").get("fin_cobrado").get(
                        "fines_cobrado"))):
                    if vector_estado.get("eventos").get("fin_cobrado").get("fines_cobrado")\
                            [i].servidor.id == cabina_cobro_encontrada.id:
                        index = i
                        break
                fin_cobrado = vector_estado.get("eventos").get("fin_cobrado").get(
                    "fines_cobrado").pop(index)
                fin_cobrado.tiempo_fin_evento = fin_tiempo_cobrado
                bisect.insort(vector_estado.get("eventos").get("fin_cobrado").get("fines_cobrado"),
                              fin_cobrado)

                # Seteo datos del auto, ya que cambia el estado
                index = None
                for i in range(0, len(vector_estado.get("clientes").get("autos"))):
                    if vector_estado.get("clientes").get("autos")[i].lugar_estacionamiento is not None:
                        if vector_estado.get("clientes").get("autos")[i].lugar_estacionamiento.id == \
                                servidor_a_liberar.id:
                            index = i
                            break
                vector_estado.get("clientes").get("autos")[index].lugar_estacionamiento = None
                vector_estado.get("clientes").get("autos")[index].cabina_cobro = cabina_cobro_encontrada
                vector_estado.get("clientes").get("autos")[index].estado = ESTADO_AUTO_PAGANDO

                # Seteo datos de contadores
                vector_estado["contadores"]["lugares_estacionamiento_ocupados"] -= 1
                porcentaje_ocupacion = round(vector_estado.get("contadores").get("lugares_estacionamiento_ocupados")
                                             * 100 / self.cantidad_lugares_estacionamiento, 2)
                vector_estado["contadores"]["porcentaje_ocupacion"] = porcentaje_ocupacion

            # Si no se encontró cabina de cobro
            else:

                # Seteo datos del auto, ya que cambia el estado
                index = None
                for i in range(0, len(vector_estado.get("clientes").get("autos"))):
                    if vector_estado.get("clientes").get("autos")[i].lugar_estacionamiento is not None:
                        if vector_estado.get("clientes").get("autos")[i].lugar_estacionamiento.id == \
                                servidor_a_liberar.id:
                            index = i
                            break
                vector_estado.get("clientes").get("autos")[index].estado = ESTADO_AUTO_ESPERANDO_PAGAR
                vector_estado.get("clientes").get("autos")[index].hora_inicio_espera_para_pagar = reloj_evento

        elif evento == self.EVENTO_FIN_COBRADO:

            # Borro dato de fin de cobrado
            fin_cobrado = vector_estado.get("eventos").get("fin_cobrado") \
                .get("fines_cobrado").pop(0)
            fin_cobrado.tiempo_fin_evento = None
            bisect.insort(vector_estado.get("eventos").get("fin_cobrado").get("fines_cobrado"),
                          fin_cobrado)

            # Seteo datos de cabina de cobro, ya que se desocupa la cabina o disminuye la cola
            index = None
            for i in range(0, len(vector_estado.get("servidores").get("cabinas_cobro"))):
                if vector_estado.get("servidores").get("cabinas_cobro")[i].id == servidor_a_liberar.id:
                    index = i
                    break
            cabina_cobro_con_cola_encontrada = None
            if vector_estado.get("servidores").get("cabinas_cobro")[index].cola == 0:
                cabina_cobro = vector_estado.get("servidores").get("cabinas_cobro").pop(index)
                cabina_cobro.estado = ESTADO_SERVIDOR_LIBRE
                bisect.insort(vector_estado.get("servidores").get("cabinas_cobro"),
                              cabina_cobro)
            else:
                vector_estado.get("servidores").get("cabinas_cobro")[index].cola -= 1
                cabina_cobro_con_cola_encontrada = vector_estado.get("servidores").get("cabinas_cobro")[index]

            # Seteo datos del auto, ya que debe destruirse
            index = None
            for i in range(0, len(vector_estado.get("clientes").get("autos"))):
                if vector_estado.get("clientes").get("autos")[i].cabina_cobro is not None:
                    if vector_estado.get("clientes").get("autos")[i].cabina_cobro.id == servidor_a_liberar.id:
                        index = i
                        break
            monto_auto = vector_estado.get("clientes").get("autos")[index].monto
            del vector_estado.get("clientes").get("autos")[index]

            # Seteo datos de contadores
            vector_estado["contadores"]["monto_recaudado"] += monto_auto

            # Si se encontró cola en la cabina de cobro
            if cabina_cobro_con_cola_encontrada is not None:

                # Busco el lugar de estacionamiento del auto que sigue para pagar
                lugar_estacionamiento_auto = None
                aux_menor_hora_inicio_espera_para_pagar = None
                for auto in vector_estado.get("clientes").get("autos"):
                    if auto.estado == ESTADO_AUTO_ESPERANDO_PAGAR:
                        if aux_menor_hora_inicio_espera_para_pagar is None or \
                                auto.hora_inicio_espera_para_pagar < aux_menor_hora_inicio_espera_para_pagar:
                            lugar_estacionamiento_auto = auto.lugar_estacionamiento
                            aux_menor_hora_inicio_espera_para_pagar = auto.hora_inicio_espera_para_pagar

                # Seteo datos de lugar de estacionamiento, ya que se desocupa el lugar
                index = None
                for i in range(0, len(vector_estado.get("servidores").get("lugares_estacionamiento"))):
                    if vector_estado.get("servidores").get("lugares_estacionamiento")\
                            [i].id == lugar_estacionamiento_auto.id:
                        index = i
                        break
                lugar_estacionamiento = vector_estado.get("servidores").get("lugares_estacionamiento").pop(
                    index)
                lugar_estacionamiento.estado = ESTADO_SERVIDOR_LIBRE
                bisect.insort(vector_estado.get("servidores").get("lugares_estacionamiento"),
                              lugar_estacionamiento)

                # Genero fin cobrado para el auto que recién termina su estacionamiento
                tiempo_cobrado = self.tiempo_cobro
                fin_tiempo_cobrado = round(reloj_evento + tiempo_cobrado, 2)

                # Seteo datos de fin cobrado
                vector_estado["eventos"]["fin_cobrado"]["tiempo_cobrado"] = tiempo_cobrado
                index = None
                for i in range(0, len(vector_estado.get("eventos").get("fin_cobrado").get(
                        "fines_cobrado"))):
                    if vector_estado.get("eventos").get("fin_cobrado").get("fines_cobrado")\
                            [i].servidor.id == cabina_cobro_con_cola_encontrada.id:
                        index = i
                        break
                fin_cobrado = vector_estado.get("eventos").get("fin_cobrado").get(
                    "fines_cobrado").pop(index)
                fin_cobrado.tiempo_fin_evento = fin_tiempo_cobrado
                bisect.insort(vector_estado.get("eventos").get("fin_cobrado").get("fines_cobrado"),
                              fin_cobrado)

                # Seteo datos del auto, ya que cambia el estado
                index = None
                for i in range(0, len(vector_estado.get("clientes").get("autos"))):
                    if vector_estado.get("clientes").get("autos")[i].lugar_estacionamiento is not None:
                        if vector_estado.get("clientes").get("autos")[i].lugar_estacionamiento.id == \
                                lugar_estacionamiento_auto.id:
                            index = i
                            break
                vector_estado.get("clientes").get("autos")[index].lugar_estacionamiento = None
                vector_estado.get("clientes").get("autos")[index].cabina_cobro = cabina_cobro_con_cola_encontrada
                vector_estado.get("clientes").get("autos")[index].estado = ESTADO_AUTO_PAGANDO

                # Seteo datos de contadores
                vector_estado["contadores"]["lugares_estacionamiento_ocupados"] -= 1
                porcentaje_ocupacion = round(
                    vector_estado.get("contadores").get("lugares_estacionamiento_ocupados")
                    * 100 / self.cantidad_lugares_estacionamiento, 2)
                vector_estado["contadores"]["porcentaje_ocupacion"] = porcentaje_ocupacion

        return vector_estado

    def completar_objetos_temporales(self, iteraciones_simuladas):

        # Establezco criterios de ordenamiento para agilizar el algoritmo
        Servidor.ordenar_por = ORDEN_SERVIDORES_POR_ID
        Evento.ordenar_por = ORDEN_EVENTOS_POR_SERVIDOR

        # Obtengo todos los ids de autos generados durante las iteraciones simuladas ordenados
        ids_autos = []
        for iteracion_simulada in iteraciones_simuladas:
            for auto in iteracion_simulada.get("clientes").get("autos"):
                ids_autos.append(auto.id)

        # Elimino ids de autos duplicados
        ids_autos = sorted(list(set(ids_autos)))

        # Ordeno eventos y servidores y agrego objetos temporales faltantes en cada iteración
        for iteracion_simulada in iteraciones_simuladas:

            # Ordeno eventos
            iteracion_simulada["eventos"]["fin_estacionamiento"]["fines_estacionamiento"] = \
                sorted(iteracion_simulada.get("eventos").get("fin_estacionamiento")
                       .get("fines_estacionamiento"))
            iteracion_simulada["eventos"]["fin_cobrado"]["fines_cobrado"] = \
                sorted(iteracion_simulada.get("eventos").get("fin_cobrado")
                       .get("fines_cobrado"))

            # Ordeno servidores
            iteracion_simulada["servidores"]["lugares_estacionamiento"] = \
                sorted(iteracion_simulada.get("servidores").get("lugares_estacionamiento"))
            iteracion_simulada["servidores"]["cabinas_cobro"] = \
                sorted(iteracion_simulada.get("servidores").get("cabinas_cobro"))

            autos_ordenados = []
            autos_incompletos = iteracion_simulada.get("clientes").get("autos")
            index_ids_autos = 0
            index_ids_autos_incompletos = 0
            while index_ids_autos < len(ids_autos) and index_ids_autos_incompletos < len(autos_incompletos):
                if ids_autos[index_ids_autos] < autos_incompletos[index_ids_autos_incompletos]:
                    autos_ordenados.append(
                        Auto(ids_autos[index_ids_autos], None, None, None, None, None)
                    )
                    index_ids_autos += 1
                else:
                    autos_ordenados.append(
                        autos_incompletos[index_ids_autos_incompletos]
                    )
                    index_ids_autos_incompletos += 1

    def simular_iteraciones(self, tiempo_simulacion, tiempo_desde, cantidad_iteraciones, tiempo_autos,
                            probabilidad_chico_autos, probabilidad_grande_autos, probabilidad_utilitario_autos,
                            probabilidad_1_tiempo_estacionamiento, probabilidad_2_tiempo_estacionamiento,
                            probabilidad_3_tiempo_estacionamiento, probabilidad_4_tiempo_estacionamiento,
                            cantidad_lugares_estacionamiento, cantidad_cabinas_cobro, tiempo_cobro):

        # Reestablezo control de ids de autos
        self.ultimo_id_auto = 0

        # Agrego datos como atributos del objeto para poder manejarlos a nivel clase
        self.tiempo_autos = tiempo_autos
        self.probabilidad_chico_autos = probabilidad_chico_autos
        self.probabilidad_grande_autos = probabilidad_grande_autos
        self.probabilidad_utilitario_autos = probabilidad_utilitario_autos
        self.probabilidad_1_tiempo_estacionamiento = probabilidad_1_tiempo_estacionamiento
        self.probabilidad_2_tiempo_estacionamiento = probabilidad_2_tiempo_estacionamiento
        self.probabilidad_3_tiempo_estacionamiento = probabilidad_3_tiempo_estacionamiento
        self.probabilidad_4_tiempo_estacionamiento = probabilidad_4_tiempo_estacionamiento
        self.cantidad_lugares_estacionamiento = cantidad_lugares_estacionamiento
        self.cantidad_cabinas_cobro = cantidad_cabinas_cobro
        self.tiempo_cobro = tiempo_cobro

        # Genero vector de estado inicial
        rnd_tiempo_entre_llegadas = truncar(random.random(), 2)
        tiempo_proxima_llegada = round(-1 * self.tiempo_autos * math.log(1 - rnd_tiempo_entre_llegadas), 2)
        proxima_llegada = tiempo_proxima_llegada
        vector_estado = {
            "evento": "inicializacion",
            "reloj": 0,
            "eventos": {
                "llegada_autos": {
                    "rnd_tiempo_entre_llegadas": rnd_tiempo_entre_llegadas,
                    "tiempo_proxima_llegada": tiempo_proxima_llegada,
                    "proxima_llegada": proxima_llegada,
                },
                "fin_estacionamiento": {
                    "rnd_fin_estacionamiento": None,
                    "tiempo_estacionamiento": None,
                    "fines_estacionamiento": []
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
                "lugares_estacionamiento_ocupados": 0,
                "porcentaje_ocupacion": 0,
                "monto_recaudado": 0,
            },
            "clientes": {
                "auxiliares": {
                    "rnd_tipo_auto": None,
                    "tipo_auto": None
                },
                "autos": []
            }
        }

        for i in range(1, cantidad_lugares_estacionamiento + 1):
            lugar_estacionamiento = LugarEstacionamiento(i, ESTADO_SERVIDOR_LIBRE)
            fin_estacionamiento = FinEstacionamiento(None, lugar_estacionamiento)
            vector_estado.get("servidores").get("lugares_estacionamiento").append(lugar_estacionamiento)
            vector_estado.get("eventos").get("fin_estacionamiento").get("fines_estacionamiento") \
                .append(fin_estacionamiento)

        for i in range(1, cantidad_cabinas_cobro + 1):
            cabina_cobro = CabinaCobro(i, ESTADO_SERVIDOR_LIBRE)
            fin_cobrado = FinCobrado(None, cabina_cobro)
            vector_estado.get("servidores").get("cabinas_cobro").append(cabina_cobro)
            vector_estado.get("eventos").get("fin_cobrado").get("fines_cobrado").append(fin_cobrado)

        # Realizo simulación almacenando los vectores estados de las iteraciones de interés
        iteraciones_simuladas = [vector_estado]
        ultimo_vector_estado_agregado = True
        cantidad_iteraciones_agregadas = 0

        # Agrego iteraciones dentro de lo parametrizado
        while 1:
            vector_estado_proximo = self.simular_iteracion(vector_estado)
            if vector_estado_proximo.get("reloj") > tiempo_simulacion:
                break
            vector_estado = vector_estado_proximo
            ultimo_vector_estado_agregado = False

            if vector_estado.get("reloj") >= tiempo_desde and cantidad_iteraciones_agregadas < cantidad_iteraciones:
                ultimo_vector_estado_agregado = True
                cantidad_iteraciones_agregadas += 1
                iteraciones_simuladas.append(vector_estado)

        # Compleo objetos temporales para mostrar correctamente la simulación
        self.completar_objetos_temporales(iteraciones_simuladas)

        # Agrego ultimo vector de estado si aún no se agregó
        if not ultimo_vector_estado_agregado:
            for auto in vector_estado.get("clientes").get("autos"):
                auto.estado = None
                auto.lugar_estacionamiento = None
                auto.cabina_cobro = None
                auto.hora_inicio_espera_para_pagar = None
                auto.monto = None
            iteraciones_simuladas.append(vector_estado)

        # Muestro iteraciones simuladas por consola
        print("########## RESULTADOS DE LA SIMULACIÓN ##########\n")
        for i in range(0, len(iteraciones_simuladas)):
            print("########## ITERACION " + str(i + 1) + " ##########")
            mostrar_diccionario_formateado(iteraciones_simuladas[i])
            print("\n")

        # Devuelvo iteraciones simuladas de interés
        # return iteraciones_simuladas
