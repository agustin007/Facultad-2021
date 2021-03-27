using System;
using System.Collections.Generic;
using System.Data;
using System.Windows.Forms;
using TP1SIM2021.Classes;


namespace TP1SIM2021.Forms
{
    public partial class FrmNumPseudoaleatorios : Form
    {

        /* Atributos*/

        List<double> numerosPseudoaleatorios;

        /* Load */

        public FrmNumPseudoaleatorios()
        {
            InitializeComponent();
        }

        private void FrmNumPseudoaleatorios_Load(object sender, EventArgs e)
        {
            tabPage1.Text = "Numeros Pseudoaleatorios";
            tabPage2.Text = "Grafico";
            tabPage3.Text = "Integrantes";

            List<ItemComboBox> metodos = new List<ItemComboBox>();
            metodos.Add(new ItemComboBox("Congruencial lineal", 0));
            metodos.Add(new ItemComboBox("Congruencial multiplicativo", 1));
            metodos.Add(new ItemComboBox("Provisto por el lenguaje", 2));
            CmbMetodos.DataSource = metodos;
            CmbMetodos.DisplayMember = "Nombre";
            CmbMetodos.ValueMember = "Valor";
            CmbMetodos.SelectedIndex = 0;

            LimpiarCampos();
            LimpiarGrilla();

            /*this.CmbIntervalos.DataSource = numeroIntervalos;
            this.CmbIntervalos.ValueMember = numeroIntervalos[CmbIntervalos.SelectedIndex].ToString();
            this.CmbIntervalos.SelectedIndex = -1;*/

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

        private void BtnGenerar_Click(object sender, EventArgs e)
        {
            int metodoSeleccionado =CmbMetodos.SelectedIndex;
            switch (metodoSeleccionado)
            {
                case 0:
                    if (TxtSemilla.Text != string.Empty && TxtA.Text != string.Empty && TxtC.Text != string.Empty &&
                        TxtM.Text != string.Empty && TxtCantidad.Text != string.Empty)
                    {
                        int semilla = Convert.ToInt32(TxtSemilla.Text);
                        int cantidad = Convert.ToInt32(TxtCantidad.Text);
                        int a = Convert.ToInt32(TxtA.Text);
                        int c = Convert.ToInt32(TxtC.Text);
                        int m = Convert.ToInt32(TxtM.Text);

                        numerosPseudoaleatorios = GeneradorNumerosPseudoaleatorios.GenerarConMetodoCongruencialLineal(cantidad, semilla, a, c, m);
                        GenerarTabla(numerosPseudoaleatorios);

                    }
                    else
                    {
                        MessageBox.Show("Por favor, ingrese los parámetros necesarios para poder generar los números pseudoaleatorios",
                            "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                    break;

                case 1:
                    if (TxtSemilla.Text != string.Empty && TxtA.Text != string.Empty && TxtC.Text != string.Empty &&
                        TxtM.Text != string.Empty && TxtCantidad.Text != string.Empty)
                    {

                        int semilla = Convert.ToInt32(TxtSemilla.Text);
                        int cantidad = Convert.ToInt32(TxtCantidad.Text);
                        int a = Convert.ToInt32(TxtA.Text);
                        int c = Convert.ToInt32(TxtC.Text);
                        int m = Convert.ToInt32(TxtM.Text);

                        numerosPseudoaleatorios = GeneradorNumerosPseudoaleatorios.GenerarConMetodoCongruencialMultiplicativo(cantidad, semilla, a, m);
                        GenerarTabla(numerosPseudoaleatorios);

                    }
                    else
                    {
                        MessageBox.Show("Por favor, ingrese los parámetros necesarios para poder generar los números pseudoaleatorios",
                            "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                    break;

                case 2:
                    if (TxtCantidad.Text != string.Empty)
                    {
                        int cantidad = Convert.ToInt32(TxtCantidad.Text);

                        numerosPseudoaleatorios = GeneradorNumerosPseudoaleatorios.GenerarConMetodoProvistoPorLenguaje(cantidad);
                        GenerarTabla(numerosPseudoaleatorios);
                    }
                    else
                    {
                        MessageBox.Show("Por favor, ingrese los parámetros necesarios para poder generar los números pseudoaleatorios",
                            "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                    break;
            }
        }

        private void BtnLimpiar_Click(object sender, EventArgs e)
        {
            CmbMetodos.SelectedIndex = 0;
            this.LimpiarCampos();
            this.LimpiarGrilla();
        }

        /* Validaciones que no permiten ingresar letras o espacios en los campos */

        private void TxtSemilla_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && (e.KeyChar != '.'))
            {
                e.Handled = true;
            }
        }

        private void TxtA_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && (e.KeyChar != '.'))
            {
                e.Handled = true;
            }
        }

        private void TxtC_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && (e.KeyChar != '.'))
            {
                e.Handled = true;
            }
        }

        private void TxtM_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && (e.KeyChar != '.'))
            {
                e.Handled = true;
            }
        }

        private void TxtCantidad_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) && (e.KeyChar != '.'))
            {
                e.Handled = true;
            }
        }
    } 
}
