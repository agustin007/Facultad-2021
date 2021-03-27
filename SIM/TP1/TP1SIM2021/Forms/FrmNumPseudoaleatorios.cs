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
            string semillaStr;
            string aStr;
            string cStr;
            string mStr;
            string cantidadStr;

            int metodoSeleccionado =CmbMetodos.SelectedIndex;
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

                    numerosPseudoaleatorios = GeneradorNumerosPseudoaleatorios.GenerarConMetodoCongruencialLineal(
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

                    numerosPseudoaleatorios = GeneradorNumerosPseudoaleatorios.GenerarConMetodoCongruencialMultiplicativo(
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

                    numerosPseudoaleatorios = GeneradorNumerosPseudoaleatorios.GenerarConMetodoProvistoPorLenguaje(
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
