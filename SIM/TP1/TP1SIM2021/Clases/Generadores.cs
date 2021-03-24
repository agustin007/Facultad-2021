using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP1SIM2021.Clases
{
  class Generadores
  {
    

    public class MetodoLineal
    {
      int cantidad;
      float semilla;
      float a;
      float c;
      float m;

    }
    public class MetodoCongruencialMultiplicativo
    {
      int cantidad;
      float semilla;
      float a;
      float m;
    }
    public class MetodoLenguaje
    {

      List<double> numerosGenerados = new List<double>();

      public List<double> GeneradorLenguaje(int cantidad, int semilla)
      {

       
        var random = new Random(semilla);

        for (int index = 0; index < cantidad;index ++)
        {
          var numero = Math.Round(random.NextDouble(),4);
          Console.WriteLine($"Iteración {index +1} - semilla {semilla} - valor {numero}");
          numerosGenerados.Add(numero);
        }
        return numerosGenerados;

      }
    }

  }
}
