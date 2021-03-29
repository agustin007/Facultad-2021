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

        public List<(double, double)> ObtenerIntervalos(int cantidadIntervalos, double minimo, double maximo)
        {
            List<(double, double)> intervalos = new List<(double, double)>();
            double rangoTotal = maximo - minimo;
            double rangoIntervalos = rangoTotal / cantidadIntervalos;

            double limiteInferior = 0;
            double limiteSuperior = 0;
            for (int i=0; i < cantidadIntervalos; i++)
            {   if (i == 0)
                {
                    limiteInferior = minimo;
                }
                limiteSuperior = limiteInferior + rangoIntervalos;

                intervalos.Add((Math.Round(limiteInferior, 2), Math.Round(limiteSuperior, 2)));

                limiteInferior = limiteSuperior;
            }

            return intervalos;
        }

        public DataTable GenerarTablaTestChiCuadrado(List<(double, double)> intervalos)
        {
            DataTable tabla = new DataTable();

            return tabla;
        }

    }
}
