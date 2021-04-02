import random
import sorting
import matplotlib.pyplot as plt
import numpy as np
from soporte.helper import *


class ControladorGeneradorNumerosPseudoaleatorios:

    def generar_numeros_pseudoaleatorios_congruencial_lineal(self, cantidad, semilla, a, c, m):

        # Genero lista de numeros aleatorios
        numeros_generados = []
        xi = semilla
        for _ in range(0, cantidad):
            xi = truncar((a * xi + c) % m, 4)
            numero_pseualeatorio = truncar(xi / m, 4)
            numeros_generados.append(numero_pseualeatorio)

        return numeros_generados

    def generar_numeros_pseudoaleatorios_congruencial_multiplicativo(self, cantidad, semilla, a, m):

        # Genero lista de numeros aleatorios
        numeros_generados = []
        xi = semilla
        for _ in range(0, cantidad):
            xi = round((a * xi) % m, 4)
            numero_pseualeatorio = truncar(xi / m, 4)
            numeros_generados.append(numero_pseualeatorio)

        return numeros_generados

    def generar_numeros_pseudoaleatorios_provisto_por_lenguaje(self, cantidad):

        # Genero lista de numeros aleatorios
        numeros_generados = []
        for _ in range(0, cantidad):
            numero_pseualeatorio = truncar(random.random(), 4)
            numeros_generados.append(numero_pseualeatorio)

        return numeros_generados

    def realizar_test_chi_cuadrado(self, numeros_pseudoaleatorios, cantidad_intervalos):

        # Genero lista de intervalos
        intervalos = []
        max_intervalo = 0
        paso = Decimal(1 / cantidad_intervalos).quantize(SIXPLACES)
        for i in range(0, cantidad_intervalos):
            min_intervalo = Decimal(max_intervalo).quantize(SIXPLACES)
            max_intervalo = Decimal(min_intervalo + paso).quantize(SIXPLACES)
            intervalos.append((min_intervalo, max_intervalo))

        # Ordeno lista de numeros pseudoaleatorios para facilitar el calculo de frecuencias por intervalo, optimizando
        # el procesamiento con un algoritmo de ordenamiento de O(n * log n)
        numeros_pseudoaleatorios = sorting.merge(numeros_pseudoaleatorios)

        # Calculo frecuencias por intervalos
        frecuencias_x_intervalo = [0] * cantidad_intervalos
        index = 0
        for numero_pseudoaleatorio in numeros_pseudoaleatorios:
            if not (intervalos[index][0] <= numero_pseudoaleatorio < intervalos[index][1]):
                index += 1
            frecuencias_x_intervalo[index] += 1

        # Genero una lista de diccionarios con el calculo de la prueba de chi cuadrado por intervalo y guardo el final
        # en una variable
        chi_cuadrado_x_intervalo = []
        fe = len(numeros_pseudoaleatorios) / cantidad_intervalos
        c_acum = 0
        for i in range(0, cantidad_intervalos):
            intervalo = (intervalos[i][0].quantize(TWOPLACES), intervalos[i][1].quantize(TWOPLACES))
            fo = frecuencias_x_intervalo[i]
            c = ((fo - fe) ** 2) / fe
            c_acum += c
            chi_cuadrado_x_intervalo.append({
                "intervalo": intervalo,
                "fo": fo,
                "fe": round(fe, 4),
                "c": round(c, 4),
                "c_acum": round(c_acum, 4)
            })
        chi_cuadrado = round(c_acum, 4)

        return chi_cuadrado_x_intervalo, chi_cuadrado

    """
    def generar_grafico_frecuencias(self, medias, frecuencias_observadas, frecuencias_esperadas):

        # Creo grafico
        x = np.arange(len(medias))
        width = 0.35
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, frecuencias_observadas, width, label="Observadas")
        rects2 = ax.bar(x + width / 2, frecuencias_esperadas, width, label="Esperadas")

        ax.set_ylabel("Cantidad")
        ax.set_title("Frecuencias esperadas y observadas")
        ax.set_xticks(x)
        ax.set_xticklabels(medias)
        ax.legend()

        for rect in rects1:
            height = rect.get_height()
            ax.annotate("{}".format(height), xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3),
                        textcoords="offset points", ha="center", va="bottom")
        for rect in rects2:
            height = rect.get_height()
            ax.annotate("{}".format(height), xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3),
                        textcoords="offset points", ha="center", va="bottom")
        fig.tight_layout()
        plt.show()
    """
