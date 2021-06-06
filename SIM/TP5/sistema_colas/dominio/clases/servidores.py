ESTADO_SERVIDOR_LIBRE = "Libre"
ESTADO_SERVIDOR_OCUPADO = "Ocupado"

ORDEN_SERVIDORES_POR_ID = "orden_servidores_por_id"
ORDEN_SERVIDORES_POR_ESTADO = "orden_servidores_por_estado"
ORDEN_SERVIDORES_POR_COLA = "orden_servidores_por_cola"


class Servidor:

    id = None
    estado = None
    cola = None
    ordenar_por = None

    def __init__(self, id_servidor=None, estado=None, cola=0):
        self.id = id_servidor
        self.estado = estado
        self.cola = cola

    def __eq__(self, other):
        if isinstance(other, Servidor):
            if Servidor.ordenar_por is None:
                Servidor.ordenar_por = ORDEN_SERVIDORES_POR_ID
            if Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ID:
                return True if self.id == other.id else False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ESTADO:
                return True if self.estado == other.estado else False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_COLA:
                return True if self.cola == other.cola else False
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Servidor):
            if Servidor.ordenar_por is None:
                Servidor.ordenar_por = ORDEN_SERVIDORES_POR_ID
            if Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ID:
                return True if self.id != other.id else False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ESTADO:
                return True if self.estado != other.estado else False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_COLA:
                return True if self.cola != other.cola else False
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Servidor):
            if Servidor.ordenar_por is None:
                Servidor.ordenar_por = ORDEN_SERVIDORES_POR_ID
            if Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ID:
                return True if self.id > other.id else False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ESTADO:
                if self.estado == ESTADO_SERVIDOR_OCUPADO and other.estado == ESTADO_SERVIDOR_LIBRE:
                    return True
                return False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_COLA:
                return True if self.cola > other.cola else False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Servidor):
            if Servidor.ordenar_por is None:
                Servidor.ordenar_por = ORDEN_SERVIDORES_POR_ID
            if Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ID:
                return True if self.id < other.id else False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ESTADO:
                if self.estado == ESTADO_SERVIDOR_LIBRE and other.estado == ESTADO_SERVIDOR_OCUPADO:
                    return True
                return False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_COLA:
                return True if self.cola < other.cola else False
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Servidor):
            if Servidor.ordenar_por is None:
                Servidor.ordenar_por = ORDEN_SERVIDORES_POR_ID
            if Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ID:
                return True if self.id >= other.id else False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ESTADO:
                if self.estado == ESTADO_SERVIDOR_LIBRE and other.estado == ESTADO_SERVIDOR_LIBRE or \
                        self.estado == ESTADO_SERVIDOR_OCUPADO and other.estado == ESTADO_SERVIDOR_OCUPADO or \
                        self.estado == ESTADO_SERVIDOR_OCUPADO and other.estado == ESTADO_SERVIDOR_LIBRE:
                    return True
                return False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_COLA:
                return True if self.cola >= other.cola else False
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Servidor):
            if Servidor.ordenar_por is None:
                Servidor.ordenar_por = ORDEN_SERVIDORES_POR_ID
            if Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ID:
                return True if self.id <= other.id else False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_ESTADO:
                if self.estado == ESTADO_SERVIDOR_LIBRE and other.estado == ESTADO_SERVIDOR_LIBRE or \
                        self.estado == ESTADO_SERVIDOR_OCUPADO and other.estado == ESTADO_SERVIDOR_OCUPADO or \
                        self.estado == ESTADO_SERVIDOR_LIBRE and other.estado == ESTADO_SERVIDOR_OCUPADO:
                    return True
                return False
            elif Servidor.ordenar_por == ORDEN_SERVIDORES_POR_COLA:
                return True if self.cola <= other.cola else False
        else:
            return False


class LugarEstacionamiento(Servidor):

    def __repr__(self):
        return "LugarEstacionamiento(id=" + str(self.id) + ", estado=" + self.estado + ")"


class CabinaCobro(Servidor):

    def __repr__(self):
        return "CabinaCobro(id=" + str(self.id) + ", estado=" + self.estado + ", cola=" + str(self.cola) + ")"
