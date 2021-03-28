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

    }
}
