import random
import sorting
import matplotlib.pyplot as plt
from soporte.helper import *


class ControladorGeneradorVariablesAleatorias:

    def generar_variables_aleatorias_uniforme(self, cantidad, a, b):

        # Genero lista de variables aleatorias
        variables_generadas = []
        for _ in range(0, cantidad):
            variable_aleatoria = truncar(a + random.random() * (b - a), 4)
            variables_generadas.append(variable_aleatoria)

        return variables_generadas

    def generar_variables_aleatorias_normal(self, cantidad, mu, sigma):

        # Genero lista de variables aleatorias
        variables_generadas = []
        for _ in range(0, cantidad):
            z = math.sqrt(-2 * math.log(1 - random.random())) * math.cos(2 * math.pi * random.random())
            variable_aleatoria = truncar(mu + z * sigma, 4)
            variables_generadas.append(variable_aleatoria)

        return variables_generadas

    def generar_variables_aleatorias_exponencial(self, cantidad, lambd):

        # Genero lista de variables aleatorias
        variables_generadas = []
        for _ in range(0, cantidad):
            variable_aleatoria = truncar(-1 / lambd * math.log(1 - random.random()), 4)
            variables_generadas.append(variable_aleatoria)

        return variables_generadas

    """
    def obtener_intervalos(self, cantidad_intervalos):

        # Genero lista de intervalos
        intervalos = []
        max_intervalo = 0
        paso = Decimal(1 / cantidad_intervalos).quantize(SIXPLACES)
        for i in range(0, cantidad_intervalos):
            min_intervalo = Decimal(max_intervalo).quantize(SIXPLACES)
            max_intervalo = Decimal(min_intervalo + paso).quantize(SIXPLACES)
            intervalos.append((min_intervalo, max_intervalo))

        return intervalos
    """

    """
    def generar_histograma(self, numeros_pseudoaleatorios, intervalos):

        # Creo grafico
        fig, ax = plt.subplots()

        cantidad_intervalos = len(intervalos)
        n_bins = cantidad_intervalos
        x = numeros_pseudoaleatorios

        ax.hist(x, n_bins, range=(0, 1), rwidth=0.8, color="navy", label="Frecuencias observadas")
        ax.legend(prop={"size": 8})
        ax.set_title("Histograma")

        xticks = []
        xticks_labels = []
        for intervalo in intervalos:
            media = (intervalo[0] + intervalo[1]) / 2
            xticks.append(media)
            if cantidad_intervalos <= 10:
                xticks_labels.append(str(round(media, 2)))
            else:
                xticks_labels.append(str(round(media, 3)))
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticks_labels, rotation=45)

        plt.xlabel("Valores")
        plt.ylabel("Cantidad")
        plt.show()
    """

    """
    def realizar_test_chi_cuadrado(self, numeros_pseudoaleatorios, intervalos):

        # Ordeno lista de numeros pseudoaleatorios para facilitar el calculo de frecuencias por intervalo, optimizando
        # el procesamiento con un algoritmo de ordenamiento de O(n * log n)
        numeros_pseudoaleatorios = sorting.merge(numeros_pseudoaleatorios)

        # Calculo frecuencias por intervalos
        cantidad_intervalos = len(intervalos)
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
        fo_acum = 0
        fe_acum = 0
        c_acum = 0
        for i in range(0, cantidad_intervalos):
            intervalo = (intervalos[i][0].quantize(TWOPLACES), intervalos[i][1].quantize(TWOPLACES))
            fo = frecuencias_x_intervalo[i]
            fo_acum += fo
            fe_acum += fe
            c = ((fo - fe) ** 2) / fe
            c_acum += c
            chi_cuadrado_x_intervalo.append({
                "intervalo": intervalo,
                "fo": fo,
                "fo_acum": round(fo_acum, 4),
                "fe": round(fe, 4),
                "fe_acum": round(fe_acum, 4),
                "c": round(c, 4),
                "c_acum": round(c_acum, 4)
            })
        chi_cuadrado = round(c_acum, 4)

        return chi_cuadrado_x_intervalo, chi_cuadrado
    """

