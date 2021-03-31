using System;
using System.Data;
using System.Collections.Generic;
using System.Windows.Forms;
using TP1SIM2021.Controllers;
using TP1SIM2021.Classes;
using System.Windows.Forms.DataVisualization.Charting;


namespace TP1SIM2021.Forms
{
    public partial class FrmNumPseudoaleatorios : Form
    {

        /* Atributos*/

        List<double> numerosPseudoaleatorios;
        List<(double, double)> intervalos;
        List<int> frecuenciaPorIntervalo;
        ControllerNumPseudoaleatorios controlador;

        /* Load */

        public FrmNumPseudoaleatorios()
        {
            InitializeComponent();
        }

        private void FrmNumPseudoaleatorios_Load(object sender, EventArgs e)
        {
            controlador = new ControllerNumPseudoaleatorios();

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

            CmbIntervalosHistograma.DataSource = intervalos;
            CmbIntervalosHistograma.DisplayMember = "Nombre";
            CmbIntervalosHistograma.ValueMember = "Valor";
            CmbIntervalosHistograma.SelectedIndex = 0;

            CmbIntervalosTest.DataSource = intervalos;
            CmbIntervalosTest.DisplayMember = "Nombre";
            CmbIntervalosTest.ValueMember = "Valor";
            CmbIntervalosTest.SelectedIndex = 0;

            LimpiarCampos();
            LimpiarGrillaNumerosPseudoaleatorios();
            LimpiarChartHistograma();
            LimpiarGrillaTestChiCuadrado();
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

        private void LimpiarGrillaNumerosPseudoaleatorios()
        {
            GrdNumerosPseudoaleatorios.DataSource = null;
            GrdNumerosPseudoaleatorios.Rows.Clear();
        }

        private void LimpiarChartHistograma()
        {
            chartHistograma.Titles.Clear();
            chartHistograma.Series.Clear();
        }

        private void LimpiarGrillaTestChiCuadrado()
        {
            GrdTest.DataSource = null;
            GrdTest.Rows.Clear();
        }

        private void GenerarTablaNumerosPseudoaleatorios()
        {
            LimpiarGrillaNumerosPseudoaleatorios();

            GrdNumerosPseudoaleatorios.DataSource = controlador.ConstruirTablaNumerosPseudoaleatorios(numerosPseudoaleatorios);
        }

        private void GenerarGrafico()
        {
            LimpiarChartHistograma();

            chartHistograma.Titles.Add("Histograma");

            chartHistograma.ChartAreas["chartHistogramaArea"].AxisX.Minimum = 0.0;
            chartHistograma.ChartAreas["chartHistogramaArea"].AxisX.Maximum = 1.0;
            chartHistograma.ChartAreas["chartHistogramaArea"].AxisX.Interval = Math.Round(1.0 / intervalos.Count, 4);

            chartHistograma.Series.Add("Frecuencias observadas");
            chartHistograma.Series["Frecuencias observadas"].Palette = ChartColorPalette.BrightPastel;
            for (int i = 0; i < intervalos.Count; i++)
            {
                chartHistograma.Series["Frecuencias observadas"].Points.AddXY((intervalos[i].Item1 + intervalos[i].Item2) / 2, 
                    frecuenciaPorIntervalo[i]);
            }
        }

        private void GenerarTablaTest()
        {
            LimpiarGrillaTestChiCuadrado();

            GrdTest.DataSource = controlador.ConstruirTablaTestChiCuadrado(intervalos, frecuenciaPorIntervalo, 
                numerosPseudoaleatorios.Count);
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

                    break;
            }

            if (intervalos != null)
            {
                intervalos.Clear();
            }
            if (frecuenciaPorIntervalo != null)
            {
                frecuenciaPorIntervalo.Clear();
            }

            LimpiarChartHistograma();
            LimpiarGrillaTestChiCuadrado();

            GenerarTablaNumerosPseudoaleatorios();
        }

        private void BtnGenerarHistograma_Click(object sender, EventArgs e)
        {
            if (numerosPseudoaleatorios == null || numerosPseudoaleatorios.Count == 0)
            {
                MessageBox.Show("Debe generar números pseudoaleatorios para poder generar el Histograma", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            int cantidadIntervalos = Convert.ToInt32(CmbIntervalosHistograma.SelectedValue);
            intervalos = controlador.ObtenerIntervalos(0.0, 1.0, cantidadIntervalos);
            frecuenciaPorIntervalo = controlador.ObtenerFrecuenciaObservadaPorIntervalo(numerosPseudoaleatorios, intervalos);
            GenerarGrafico();
        }

        private void BtnRealizarTest_Click(object sender, EventArgs e)
        {
            if (numerosPseudoaleatorios == null || numerosPseudoaleatorios.Count == 0)
            {
                MessageBox.Show("Debe generar números pseudoaleatorios para poder realizar el Test de Chi Cuadrado", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            int cantidadIntervalos = Convert.ToInt32(CmbIntervalosTest.SelectedValue);
            intervalos = controlador.ObtenerIntervalos(0.0, 1.0, cantidadIntervalos);
            frecuenciaPorIntervalo = controlador.ObtenerFrecuenciaObservadaPorIntervalo(numerosPseudoaleatorios, intervalos);
            GenerarTablaTest();
        }

        private void BtnLimpiar_Click(object sender, EventArgs e)
        {
            CmbMetodos.SelectedIndex = 0;

            if (numerosPseudoaleatorios != null)
            {
                numerosPseudoaleatorios.Clear();
            }
            if (intervalos != null)
            {
                intervalos.Clear();
            }
            if (frecuenciaPorIntervalo != null)
            {
                frecuenciaPorIntervalo.Clear();
            }

            LimpiarCampos();
            LimpiarGrillaNumerosPseudoaleatorios();
            LimpiarChartHistograma();
            LimpiarGrillaTestChiCuadrado();
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