import math


def truncar(numero, cantidad_decimales):
    cantidad_decimales = 10 ** cantidad_decimales
    return math.floor(numero * cantidad_decimales) / cantidad_decimales
