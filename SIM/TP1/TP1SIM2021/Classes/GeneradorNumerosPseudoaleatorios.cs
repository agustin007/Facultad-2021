using System;
using System.Collections.Generic;

namespace TP1SIM2021.Classes
{

    class GeneradorNumerosPseudoaleatorios
    {

        public static List<double> GenerarConMetodoCongruencialLineal(int cantidad, int semilla, int a, int c, int m)
        {
            List<double> numerosPseudoaleatorios = new List<double>();
            double numeroPseudoaleatorio;
            int xi = semilla;
            for (int index = 0; index < cantidad; index++)
            {
                xi = (a * xi + c) % m;
                numeroPseudoaleatorio = (double)xi / m;
                numerosPseudoaleatorios.Add(Math.Truncate(numeroPseudoaleatorio * 10000) / 10000);
            }

            return numerosPseudoaleatorios;
        }

        public static List<double> GenerarConMetodoCongruencialMultiplicativo(int cantidad, int semilla, int a, int m)
        {
            List<double> numerosPseudoaleatorios = new List<double>();
            double numeroPseudoaleatorio;
            int xi = semilla;

            for (int index = 0; index < cantidad; index++)
            {
                xi = (a * xi) % m;
                numeroPseudoaleatorio = (double)xi / m;
                numerosPseudoaleatorios.Add(Math.Truncate(numeroPseudoaleatorio * 10000) / 10000);
            }

            return numerosPseudoaleatorios;
        }

        public static List<double> GenerarConMetodoProvistoPorLenguaje(int cantidad)
        {
            List<double> numerosPseudoaleatorios = new List<double>();
            double numeroPseudoaleatorio;
            Random random = new Random();

            for (int index = 0; index < cantidad; index++)
            {
                numeroPseudoaleatorio = random.NextDouble();
                numerosPseudoaleatorios.Add(Math.Truncate(numeroPseudoaleatorio * 10000) / 10000);
            }
            return numerosPseudoaleatorios;
        }
   
    }
}
