using System;
using System.Collections.Generic;
using System.Data;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using TP1SIM2021.Controllers;
using TP1SIM2021.Classes;


namespace TP1SIM2021.Forms
{
    public partial class FrmNumPseudoaleatorios : Form
    {

        /* Atributos*/

        List<double> numerosPseudoaleatorios;
        ControllerNumPseudoaleatorios controlador;

        /* Load */

        public FrmNumPseudoaleatorios()
        {
            InitializeComponent();
        }

        private void FrmNumPseudoaleatorios_Load(object sender, EventArgs e)
        {
            controlador = new ControllerNumPseudoaleatorios();

            TabPagina1.Text = "Numeros Pseudoaleatorios";
            TabPagina2.Text = "Grafico";
            TabPagina3.Text = "Test de Chi Cuadrado";
            TabPagina4.Text = "Integrantes";

            List<ItemComboBox> metodos = new List<ItemComboBox>();
            metodos.Add(new ItemComboBox("Congruencial lineal", 0));
            metodos.Add(new ItemComboBox("Congruencial multiplicativo", 1));
            metodos.Add(new ItemComboBox("Provisto por el lenguaje", 2));
            CmbMetodos.DataSource = metodos;
            CmbMetodos.DisplayMember = "Nombre";
            CmbMetodos.ValueMember = "Valor";
            CmbMetodos.SelectedIndex = 0;

            List<ItemComboBox> intervalos = new List<ItemComboBox>();
            intervalos.Add(new ItemComboBox("10", 10));
            intervalos.Add(new ItemComboBox("15", 15));
            intervalos.Add(new ItemComboBox("20", 20));
            CmbIntervalosGrafico.DataSource = intervalos;
            CmbIntervalosGrafico.DisplayMember = "Nombre";
            CmbIntervalosGrafico.ValueMember = "Valor";

            LimpiarCampos();
            LimpiarGrilla();
            
        }

        /* Métodos */

        private void LimpiarCampos()
        {
            TxtSemilla.Clear();
            TxtA.Clear();
            TxtC.Clear();
            TxtM.Clear();
            TxtCantidad.Clear();
        }

        private void LimpiarGrilla()
        {
            numerosPseudoaleatorios = new List<double>();
            GrdNumerosPseudoaleatorios.DataSource = null;
            GrdNumerosPseudoaleatorios.Rows.Clear();
        }

        private void GenerarTabla(List<double> lista)
        {
            LimpiarGrilla();

            DataTable tabla = new DataTable();
            tabla.Columns.Add("N°");
            tabla.Columns.Add("Número pseudoaleatorio");
            for (int i = 0; i < lista.Count; i++)
            {
                tabla.Rows.Add(i + 1, lista[i]);
            }

            GrdNumerosPseudoaleatorios.DataSource = tabla;
        }

        private void GenerarGrafico(List<double>numerosPseudoaleatorios)
        {
<<<<<<< HEAD
            Tuple<double, double>[] TuplaIntervalos10  = {
                Tuple.Create(0.0, 0.1),
                Tuple.Create(0.1, 0.2),
                Tuple.Create(0.2, 0.3),
                Tuple.Create(0.3, 0.4),
                Tuple.Create(0.4, 0.5),
                Tuple.Create(0.5, 0.6),
                Tuple.Create(0.6, 0.7),
                Tuple.Create(0.7, 0.8),
                Tuple.Create(0.8, 0.9),
                Tuple.Create(0.9, 1.0)
            };

            int[] cantidadxIntervalo = new int[10];
            chartGraficoFrecuencias.Titles.Add("Histograma");
            chartGraficoFrecuencias.Palette = ChartColorPalette.Fire;
            for (int index = 0; index < TuplaIntervalos10.Length; index++)
=======
            chartGraficoFrecuencias.Titles.Clear();
            chartGraficoFrecuencias.Series.Clear();

            Tuple<double, double>[] TuplaIntervalos10  = {
            Tuple.Create(0.0,0.1),
            Tuple.Create(0.1,0.2),
            Tuple.Create(0.2,0.3),
            Tuple.Create(0.3,0.4),
            Tuple.Create(0.4,0.5),
            Tuple.Create(0.5,0.6),
            Tuple.Create(0.6,0.7),
            Tuple.Create(0.7,0.8),
            Tuple.Create(0.8,0.9),
            Tuple.Create(0.9,1.0)
          };
          int[] cantidadxIntervalo = new int[10];
          chartGraficoFrecuencias.Titles.Add("Histograma");
          chartGraficoFrecuencias.Palette = ChartColorPalette.Fire;
          for(int index = 0; index < TuplaIntervalos10.Length; index++)
          {
            for(int indexJ=0;indexJ < numerosPseudoaleatorios.Count; indexJ++)
>>>>>>> c5cd84be7468af50cc618e3fd0de62534a7d05a2
            {
                for (int indexJ=0;indexJ < numerosPseudoaleatorios.Count; indexJ++)
                {
                    if (numerosPseudoaleatorios[indexJ] >= TuplaIntervalos10[index].Item1 && 
                        numerosPseudoaleatorios[indexJ] < TuplaIntervalos10[index].Item2)
                    {
                        cantidadxIntervalo[index] += 1;
                    }
                }
            }
            for (int index = 0; index < TuplaIntervalos10.Length; index++)
            {
                Series serie = chartGraficoFrecuencias.Series.Add(TuplaIntervalos10[index].ToString());
                serie.Label = cantidadxIntervalo[index].ToString();
                serie.Points.Add(cantidadxIntervalo[index]);
            }
        }

        /* Eventos */

        private void CmbMetodos_SelectedIndexChanged(object sender, EventArgs e)
        {
            LimpiarCampos();

            int metodoSeleccionado = CmbMetodos.SelectedIndex;
            if (metodoSeleccionado == 0)
            {
                TxtSemilla.Enabled = true;
                TxtA.Enabled = true;
                TxtC.Enabled = true;
                TxtM.Enabled = true;
            }
            else if (metodoSeleccionado == 1)
            {
                TxtSemilla.Enabled = true;
                TxtA.Enabled = true;
                TxtC.Enabled = false;
                TxtM.Enabled = true;
            }
            else if (metodoSeleccionado == 2)
            {
                TxtSemilla.Enabled = false;
                TxtA.Enabled = false;
                TxtC.Enabled = false;
                TxtM.Enabled = false;
            }
        }

        private void BtnGenerarNumeros_Click(object sender, EventArgs e)
        {
            string semillaStr;
            string aStr;
            string cStr;
            string mStr;
            string cantidadStr;

            int metodoSeleccionado = CmbMetodos.SelectedIndex;
            switch (metodoSeleccionado)
            {
                case 0:
                    semillaStr = TxtSemilla.Text;
                    aStr = TxtA.Text;
                    cStr = TxtC.Text;
                    mStr = TxtM.Text;
                    cantidadStr = TxtCantidad.Text;

                    if (semillaStr == string.Empty || Convert.ToInt32(semillaStr) < 0)
                    {
                        MessageBox.Show("La semilla tiene que ser mayor o igual a cero", "Error", 
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (aStr == string.Empty || Convert.ToInt32(aStr) <= 0)
                    {
                        MessageBox.Show("La constante A tiene que ser mayor a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (cStr == string.Empty || Convert.ToInt32(cStr) <= 0)
                    {
                        MessageBox.Show("La constante C tiene que ser mayor a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (mStr == string.Empty || Convert.ToInt32(mStr) <= 0)
                    {
                        MessageBox.Show("La constante M tiene que ser mayor a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (Convert.ToInt32(semillaStr) >= Convert.ToInt32(mStr))
                    {
                        MessageBox.Show("La semilla tiene que ser menor que la constante M", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (Convert.ToInt32(aStr) >= Convert.ToInt32(mStr))
                    {
                        MessageBox.Show("La constante A tiene que ser menor que la constante M", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (Convert.ToInt32(cStr) >= Convert.ToInt32(mStr))
                    {
                        MessageBox.Show("La constante C tiene que ser menor que la constante M", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (cantidadStr == string.Empty || Convert.ToInt32(cantidadStr) <= 0)
                    {
                        MessageBox.Show("La cantidad de números a generar tiene que ser mayor a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }

                    numerosPseudoaleatorios = controlador.GenerarNumerosPseudoaleatoriosConMetodoCongruencialLineal(
                        Convert.ToInt32(cantidadStr), Convert.ToInt32(semillaStr), Convert.ToInt32(aStr), Convert.ToInt32(cStr),
                        Convert.ToInt32(mStr));
                    GenerarTabla(numerosPseudoaleatorios);

                    break;

                case 1:
                    semillaStr = TxtSemilla.Text;
                    aStr = TxtA.Text;
                    mStr = TxtM.Text;
                    cantidadStr = TxtCantidad.Text;

                    if (semillaStr == string.Empty || Convert.ToInt32(semillaStr) < 0)
                    {
                        MessageBox.Show("La semilla tiene que ser mayor o igual a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (aStr == string.Empty || Convert.ToInt32(aStr) <= 0)
                    {
                        MessageBox.Show("La constante A tiene que ser mayor a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (mStr == string.Empty || Convert.ToInt32(mStr) <= 0)
                    {
                        MessageBox.Show("La constante M tiene que ser mayor a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (Convert.ToInt32(semillaStr) >= Convert.ToInt32(mStr))
                    {
                        MessageBox.Show("La semilla tiene que ser menor que la constante M", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (Convert.ToInt32(aStr) >= Convert.ToInt32(mStr))
                    {
                        MessageBox.Show("La constante A tiene que ser menor que la constante M", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    if (cantidadStr == string.Empty || Convert.ToInt32(cantidadStr) <= 0)
                    {
                        MessageBox.Show("La cantidad de números a generar tiene que ser mayor a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }

                    numerosPseudoaleatorios = controlador.GenerarNumerosPseudoaleatoriosConMetodoCongruencialMultiplicativo(
                       Convert.ToInt32(cantidadStr), Convert.ToInt32(semillaStr), Convert.ToInt32(aStr), Convert.ToInt32(mStr));
                    GenerarTabla(numerosPseudoaleatorios);

                    break;

                case 2:
                    cantidadStr = TxtCantidad.Text;
                    if (cantidadStr == string.Empty || Convert.ToInt32(cantidadStr) <= 0)
                    {
                        MessageBox.Show("La cantidad de números a generar tiene que ser mayor a cero", "Error",
                            MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }

                    numerosPseudoaleatorios = controlador.GenerarNumerosPseudoaleatoriosConMetodoProvistoPorLenguaje(
                        Convert.ToInt32(cantidadStr));
                    GenerarTabla(numerosPseudoaleatorios);
                    
                    break;
            }
        }

        private void BtnLimpiar_Click(object sender, EventArgs e)
        {
            CmbMetodos.SelectedIndex = 0;
            this.LimpiarCampos();
            this.LimpiarGrilla();
        }

        private void BtnGenerarGrafico_Click(object sender, EventArgs e)
        {
            GenerarGrafico(numerosPseudoaleatorios);
        }

        private void BtnTestChiCuadrado_Click(object sender, EventArgs e)
        {

        }

        /* Validaciones que no permiten ingresar letras o espacios en los campos */

        private void TxtSemilla_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }

        private void TxtA_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }

        private void TxtC_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }

        private void TxtM_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }

        private void TxtCantidad_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }

    } 
}