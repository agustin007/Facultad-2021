import random
import sorting
from scipy import stats
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

    def ordenar_variables_aleatorias(self, variables_aleatorias):

        # Ordeno lista de variables aleatorias para facilitar la obtencion de mínimo y máximo y obtención de frecuencias
        # por intervalo, optimizando el procesamiento con un algoritmo de ordenamiento de O(n * log n)
        return sorting.merge(variables_aleatorias)

    def obtener_intervalos(self, cantidad_intervalos, minimo, maximo):

        # Genero lista de intervalos
        intervalos = []
        max_intervalo = minimo
        paso = Decimal((maximo - minimo) / cantidad_intervalos).quantize(SIXPLACES)
        for i in range(0, cantidad_intervalos):
            min_intervalo = Decimal(max_intervalo).quantize(SIXPLACES)
            max_intervalo = Decimal(min_intervalo + paso).quantize(SIXPLACES)
            intervalos.append((min_intervalo, max_intervalo))

        return intervalos

    def generar_histograma(self, variables_aleatorias, intervalos, minimo, maximo):

        # Creo grafico
        fig, ax = plt.subplots()

        cantidad_intervalos = len(intervalos)
        n_bins = cantidad_intervalos
        x = variables_aleatorias

        ax.hist(x, n_bins, range=(minimo, maximo), rwidth=0.8, color="navy", label="Frecuencias observadas")
        ax.legend(prop={"size": 8})
        ax.set_title("Histograma")

        xticks = []
        xticks_labels = []
        for intervalo in intervalos:
            media = (intervalo[0] + intervalo[1]) / 2
            xticks.append(media)
            xticks_labels.append(str(round(media, 2)))
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticks_labels, rotation=45)

        plt.xlabel("Valores")
        plt.ylabel("Cantidad")
        plt.show()

    def obtener_frecuencias_por_intervalos(self, variables_aleatorias, parametros_variables_aleatorias, intervalos):
    
        # Calculo frecuencias observadas por intervalo
        cantidad_intervalos = len(intervalos)
        frecuencias_observadas_x_intervalo = [0] * cantidad_intervalos
        index = 0
        for variable_aleatoria in variables_aleatorias:
            if not (intervalos[index][0] <= variable_aleatoria < intervalos[index][1]):
                index += 1
            frecuencias_observadas_x_intervalo[index] += 1

        # Calculo frecuencias esperadas por intervalo
        distribucion = parametros_variables_aleatorias.get("distribucion")
        if distribucion == 0:
            fe = Decimal(len(variables_aleatorias) / cantidad_intervalos)
            frecuencias_esperadas_x_intervalo = [fe] * cantidad_intervalos
        else:
            frecuencias_esperadas_x_intervalo = [None] * cantidad_intervalos
            for i in range(0, cantidad_intervalos):
                intervalo = intervalos[i]
                if distribucion == 1:
                    mu = parametros_variables_aleatorias.get("mu")
                    sigma = parametros_variables_aleatorias.get("sigma")
                    fe = Decimal((stats.norm(mu, sigma).cdf(float(intervalo[1])) -
                                  stats.norm(mu, sigma).cdf(float(intervalo[0]))) * len(variables_aleatorias))
                else:
                    lambd = parametros_variables_aleatorias.get("lambda")
                    fe = Decimal((stats.expon(0, 1 / lambd).cdf(float(intervalo[1])) -
                                  stats.expon(0, 1 / lambd).cdf(float(intervalo[0]))) * len(variables_aleatorias))
                frecuencias_esperadas_x_intervalo[i] = fe

        # Genero una lista de diccionarios con las frecuencias observadas y esperadas por intervalo
        frecuencias_x_intervalo = []
        fo_acum = 0
        fe_acum = 0
        for i in range(0, cantidad_intervalos):
            intervalo = (intervalos[i][0].quantize(TWOPLACES), intervalos[i][1].quantize(TWOPLACES))
            fo = frecuencias_observadas_x_intervalo[i]
            fo_acum += fo
            fe = frecuencias_esperadas_x_intervalo[i]
            fe_acum += fe
            frecuencias_x_intervalo.append({
                "intervalo": intervalo,
                "fo": fo,
                "fo_acum": round(fo_acum, 4),
                "fe": fe.quantize(FOURPLACES),
                "fe_acum": round(fe_acum, 4),
            })

        return frecuencias_x_intervalo

