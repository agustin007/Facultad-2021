ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO = "orden_eventos_por_fin_evento"
ORDEN_EVENTOS_POR_SERVIDOR = "orden_eventos_por_fin_evento"


class Evento:

    tiempo_fin_evento = None
    servidor = None
    ordenar_por = None

    def __init__(self, tiempo_fin_evento=None, servidor=None):

        self.tiempo_fin_evento = tiempo_fin_evento
        self.servidor = servidor

    def __eq__(self, other):
        if isinstance(other, Evento):
            if Evento.ordenar_por is None:
                Evento.ordenar_por = ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO
            if Evento.ordenar_por == ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO:
                return True if self.tiempo_fin_evento == other.tiempo_fin_evento else False
            elif Evento.ordenar_por == ORDEN_EVENTOS_POR_SERVIDOR:
                return self.servidor.__eq__(other)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Evento):
            if Evento.ordenar_por is None:
                Evento.ordenar_por = ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO
            if Evento.ordenar_por == ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO:
                return True if self.tiempo_fin_evento != other.tiempo_fin_evento else False
            elif Evento.ordenar_por == ORDEN_EVENTOS_POR_SERVIDOR:
                return self.servidor.__ne__(other)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Evento):
            if Evento.ordenar_por is None:
                Evento.ordenar_por = ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO
            if Evento.ordenar_por == ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO:
                if self.tiempo_fin_evento is None and other.tiempo_fin_evento is None:
                    return False
                elif self.tiempo_fin_evento is not None and other.tiempo_fin_evento is None:
                    return False
                elif self.tiempo_fin_evento is None and other.tiempo_fin_evento is not None:
                    return True
                return True if self.tiempo_fin_evento > other.tiempo_fin_evento else False
            elif Evento.ordenar_por == ORDEN_EVENTOS_POR_SERVIDOR:
                return self.servidor.__gt__(other)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Evento):
            if Evento.ordenar_por is None:
                Evento.ordenar_por = ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO
            if Evento.ordenar_por == ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO:
                if self.tiempo_fin_evento is None and other.tiempo_fin_evento is None:
                    return False
                elif self.tiempo_fin_evento is not None and other.tiempo_fin_evento is None:
                    return True
                elif self.tiempo_fin_evento is None and other.tiempo_fin_evento is not None:
                    return False
                return True if self.tiempo_fin_evento < other.tiempo_fin_evento else False
            elif Evento.ordenar_por == ORDEN_EVENTOS_POR_SERVIDOR:
                return self.servidor.__lt__(other)
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Evento):
            if Evento.ordenar_por is None:
                Evento.ordenar_por = ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO
            if Evento.ordenar_por == ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO:
                if self.tiempo_fin_evento is None and other.tiempo_fin_evento is None:
                    return True
                elif self.tiempo_fin_evento is not None and other.tiempo_fin_evento is None:
                    return False
                elif self.tiempo_fin_evento is None and other.tiempo_fin_evento is not None:
                    return True
                return True if self.tiempo_fin_evento >= other.tiempo_fin_evento else False
            elif Evento.ordenar_por == ORDEN_EVENTOS_POR_SERVIDOR:
                return self.servidor.__ge__(other)
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Evento):
            if Evento.ordenar_por is None:
                Evento.ordenar_por = ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO
            if Evento.ordenar_por == ORDEN_EVENTOS_POR_TIEMPO_FIN_EVENTO:
                if self.tiempo_fin_evento is None and other.tiempo_fin_evento is None:
                    return True
                elif self.tiempo_fin_evento is not None and other.tiempo_fin_evento is None:
                    return True
                elif self.tiempo_fin_evento is None and other.tiempo_fin_evento is not None:
                    return False
                return True if self.tiempo_fin_evento <= other.tiempo_fin_evento else False
            elif Evento.ordenar_por == ORDEN_EVENTOS_POR_SERVIDOR:
                return self.servidor.__le__(other)
        else:
            return False


class FinEstacionamiento(Evento):

    def __str__(self):
        return "FinEstacionamiento(tiempo_fin_evento={tiempo_fin_evento}, servidor={servidor})".format(
            tiempo_fin_evento=str(self.tiempo_fin_evento),
            servidor=self.servidor or "None"
        )

    def __repr__(self):
        return "FinEstacionamiento(tiempo_fin_evento={tiempo_fin_evento}, servidor={servidor})".format(
            tiempo_fin_evento=str(self.tiempo_fin_evento),
            servidor=self.servidor or "None"
        )


class FinCobrado(Evento):

    def __str__(self):
        return "FinCobrado(tiempo_fin_evento={tiempo_fin_evento}, servidor={servidor})".format(
            tiempo_fin_evento=str(self.tiempo_fin_evento),
            servidor=self.servidor or "None"
        )

    def __repr__(self):
        return "FinCobrado(tiempo_fin_evento={tiempo_fin_evento}, servidor={servidor})".format(
            tiempo_fin_evento=str(self.tiempo_fin_evento),
            servidor=self.servidor or "None"
        )
