using System;
using System.Data;
using System.Collections.Generic;
using TP1SIM2021.Classes;

namespace TP1SIM2021.Controllers
{
    class ControllerNumPseudoaleatorios
    {
        public List<double> GenerarNumerosPseudoaleatoriosConMetodoCongruencialLineal (int cantidad, int semilla, int a, int c, int m)
        {
            return GeneradorNumerosPseudoaleatorios.GenerarConMetodoCongruencialLineal(cantidad, semilla, a, c, m);
        }

        public List<double> GenerarNumerosPseudoaleatoriosConMetodoCongruencialMultiplicativo(int cantidad, int semilla, int a, int m)
        {
            return GeneradorNumerosPseudoaleatorios.GenerarConMetodoCongruencialMultiplicativo(cantidad, semilla, a, m);
        }

        public List<double> GenerarNumerosPseudoaleatoriosConMetodoProvistoPorLenguaje(int cantidad)
        {
            return GeneradorNumerosPseudoaleatorios.GenerarConMetodoProvistoPorLenguaje(cantidad);
        }

        public DataTable ConstruirTablaNumerosPseudoaleatorios (List<double> numerosPseudoaleatorios)
        {
            DataTable tabla = new DataTable();

            tabla.Columns.Add("N°");
            tabla.Columns.Add("Número pseudoaleatorio");
            for (int i = 0; i < numerosPseudoaleatorios.Count; i++)
            {
                tabla.Rows.Add(i + 1, numerosPseudoaleatorios[i]);
            }

            return tabla;
        }

        public List<(double, double)> ObtenerIntervalos(double minimo, double maximo, int cantidadIntervalos)
        {
            List<(double, double)> intervalos = new List<(double, double)>();

            double rangoTotal = maximo - minimo;
            double rangoIntervalos = rangoTotal / cantidadIntervalos;
            double limiteInferior = 0;
            double limiteSuperior = 0;
            for (int i = 0; i < cantidadIntervalos; i++)
            {
                if (i == 0)
                {
                    limiteInferior = minimo;
                }
                limiteSuperior = limiteInferior + rangoIntervalos;
                intervalos.Add((Math.Round(limiteInferior, 2), Math.Round(limiteSuperior, 2)));
                limiteInferior = limiteSuperior;
            }

            return intervalos;
        }

        public int[] ObtenerFrecuenciaPorIntervalo(List<double> numerosPseudoaleatorios, List<(double, double)> intervalos)
        {
            int[] frecuenciaPorIntervalo = new int[intervalos.Count];

            for (int i = 0; i < intervalos.Count; i++)
            {
                frecuenciaPorIntervalo[i] = 0;
            }
            foreach (double numeroPseudoaleatorio in numerosPseudoaleatorios)
            {
                for (int i = 0; i < intervalos.Count; i++)
                {
                    (double, double) intervalo = intervalos[i];
                    if (intervalo.Item1 <= numeroPseudoaleatorio && numeroPseudoaleatorio < intervalo.Item2)
                    {
                        frecuenciaPorIntervalo[i] = frecuenciaPorIntervalo[i] + 1;
                        break;
                    }
                }
            }

            return frecuenciaPorIntervalo;
        }

        public DataTable ConstruirTablaTestChiCuadrado(List<(double, double)> intervalos, int[] frecuenciaPorIntervalo,  
            int cantidadNumerosPseudoaleatorios)
        {
            DataTable tabla = new DataTable();

            int fo = 0;
            double c = 0;
            double cAcum = 0;
            double fe = (double)cantidadNumerosPseudoaleatorios / intervalos.Count;
            for (int i = 0; i < intervalos.Count; i++)
            {
                if (i == 0)
                {
                    tabla.Columns.Add("Intervalo");
                    tabla.Columns.Add("fo");
                    tabla.Columns.Add("fe");
                    tabla.Columns.Add("C");
                    tabla.Columns.Add("C (AC)");
                }

                fo = frecuenciaPorIntervalo[i];
                c = Math.Pow(fo - fe, 2) / fe;
                cAcum = cAcum + c;

                string intervaloStr = Convert.ToString(intervalos[i].Item1) + " - " + Convert.ToString(intervalos[i].Item2);
                string foStr = fo.ToString();
                string feStr = Math.Round(fe, 4).ToString();
                string cStr = Math.Round(c, 4).ToString();
                string cAcumStr = Math.Round(cAcum, 4).ToString();

                tabla.Rows.Add(intervaloStr, foStr, feStr, cStr, cAcumStr);
            }

            return tabla;
        }

    }
}
