class Cliente:

    id = None
    estado = None

    def __init__(self, id_cliente=None, estado=None):
        self.id = id_cliente
        self.estado = estado


ESTADO_AUTO_ESTACIONADO = "Estacionado"
ESTADO_AUTO_ESPERANDO_PAGAR = "Esperando pagar"
ESTADO_AUTO_PAGANDO = "Pagando"

TIPO_AUTO_CHICO = "Chico"
TIPO_AUTO_GRANDE = "Grande"
TIPO_AUTO_UTILITARIO = "Utilitario"

ORDEN_AUTOS_POR_ID = "orden_autos_por_id"


class Auto(Cliente):

    lugar_estacionamiento = None
    cabina_cobro = None
    hora_inicio_espera_para_pagar = None
    monto = None
    ordenar_por = None

    def __init__(self, id_cliente=None, estado=None, lugar_estacionamiento=None, cabina_cobro=None,
                 hora_inicio_espera_para_pagar=None, monto=None):
        super().__init__(id_cliente, estado)
        self.lugar_estacionamiento = lugar_estacionamiento
        self.cabina_cobro = cabina_cobro
        self.hora_inicio_espera_para_pagar = hora_inicio_espera_para_pagar
        self.monto = monto

    def __eq__(self, other):
        if isinstance(other, Auto):
            if Auto.ordenar_por is None:
                Auto.ordenar_por = ORDEN_AUTOS_POR_ID
            if Auto.ordenar_por == ORDEN_AUTOS_POR_ID:
                return True if self.id == other.id else False
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Auto):
            if Auto.ordenar_por is None:
                Auto.ordenar_por = ORDEN_AUTOS_POR_ID
            if Auto.ordenar_por == ORDEN_AUTOS_POR_ID:
                return True if self.id != other.id else False
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Auto):
            if Auto.ordenar_por is None:
                Auto.ordenar_por = ORDEN_AUTOS_POR_ID
            if Auto.ordenar_por == ORDEN_AUTOS_POR_ID:
                return True if self.id > other.id else False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            if Auto.ordenar_por is None:
                Auto.ordenar_por = ORDEN_AUTOS_POR_ID
            if Auto.ordenar_por == ORDEN_AUTOS_POR_ID:
                return True if self.id < other.id else False
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Auto):
            if Auto.ordenar_por is None:
                Auto.ordenar_por = ORDEN_AUTOS_POR_ID
            if Auto.ordenar_por == ORDEN_AUTOS_POR_ID:
                return True if self.id >= other.id else False
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Auto):
            if Auto.ordenar_por is None:
                Auto.ordenar_por = ORDEN_AUTOS_POR_ID
            if Auto.ordenar_por == ORDEN_AUTOS_POR_ID:
                return True if self.id <= other.id else False
        else:
            return False

    def __str__(self):
        return "Auto(id={id}, estado={estado}, lugar_estacionamiento={lugar_estacionamiento}, " \
               "cabina_cobro={cabina_cobro}, hora_inicio_espera_para_pagar={hora_inicio_espera_para_pagar}, " \
               "monto={monto})".format(
                    id=str(self.id),
                    estado=self.estado,
                    lugar_estacionamiento=self.lugar_estacionamiento or "None",
                    cabina_cobro=self.cabina_cobro or "None",
                    hora_inicio_espera_para_pagar=str(self.hora_inicio_espera_para_pagar),
                    monto=str(self.monto),
                )

    def __repr__(self):
        return "Auto(id={id}, estado={estado}, lugar_estacionamiento={lugar_estacionamiento}, " \
               "cabina_cobro={cabina_cobro}, hora_inicio_espera_para_pagar={hora_inicio_espera_para_pagar}, " \
               "monto={monto})".format(
                    id=str(self.id),
                    estado=self.estado,
                    lugar_estacionamiento=self.lugar_estacionamiento or "None",
                    cabina_cobro=self.cabina_cobro or "None",
                    hora_inicio_espera_para_pagar=str(self.hora_inicio_espera_para_pagar),
                    monto=str(self.monto),
                )
