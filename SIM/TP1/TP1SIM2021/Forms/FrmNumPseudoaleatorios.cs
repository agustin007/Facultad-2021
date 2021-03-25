using System;
using System.Collections.Generic;
using System.Data;
using System.Windows.Forms;
using TP1SIM2021.Clases;


namespace TP1SIM2021.Forms
{
    public partial class FrmNumPseudoaleatorios : Form
    {
        public FrmNumPseudoaleatorios()
        {
            InitializeComponent();
        }

        // Creamos la clase metodo 
        public class Metodo
        {
            public int Id { get; set; }
            public string Descripcion { get; set; }
        }

        //Generarmos una lista de objetos de tipo Metodo para cargar el comboBox
        List<Metodo> metodos = new List<Metodo>()
        {
            new Metodo {Id=1, Descripcion="Congruencial Lineal"},
            new Metodo {Id=2, Descripcion = "Congruencial Multiplicativo" },
            new Metodo {Id=3, Descripcion = "Provisto por el lenguaje"}
        };

        int[] numeroIntervalos = new int[4] { 5,10,15,20};

        private void FrmNumPseudoaleatorios_Load(object sender, EventArgs e)
        {
            this.tabPage1.Text = "Numeros Pseudoaleatorios";
            this.tabPage2.Text = "Grafico";
            this.tabPage3.Text = "Integrantes";
            this.CmbMetodos.DataSource = metodos;
            this.CmbMetodos.DisplayMember = "Descripcion";
            this.CmbMetodos.ValueMember = "Id";
            this.CmbMetodos.SelectedIndex = -1;
            this.CmbIntervalos.DataSource = numeroIntervalos;
            //this.CmbIntervalos.ValueMember = numeroIntervalos[CmbIntervalos.SelectedIndex].ToString();
            this.CmbIntervalos.SelectedIndex = -1;

        }

        private void BtnGenerar_Click(object sender, EventArgs e)
        {
            int metodo = CmbMetodos.SelectedIndex;
            switch (metodo)
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
                        generarTabla(GeneradorNumerosPseudoaleatorios.GenerarConMetodoCongruencialLineal(cantidad, semilla, a, c, m));

                    }
                    else
                    {
                        MessageBox.Show("Por favor, ingrese valores en los campos de numeros a generar", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
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
                        generarTabla(GeneradorNumerosPseudoaleatorios.GenerarConMetodoCongruencialLineal(cantidad, semilla, a, c, m));

                    }
                    else
                    {
                        MessageBox.Show("Por favor, ingrese valores en los campos de numeros a generar", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                    break;

                case 2:
                    if (TxtCantidad.Text != string.Empty)
                    {
                        int cantidad = Convert.ToInt32(TxtCantidad.Text);
                        generarTabla(GeneradorNumerosPseudoaleatorios.GenerarConMetodoProvistoPorLenguaje(cantidad));
                    }
                    else
                    {
                        MessageBox.Show("Por favor, ingrese valores en los campos de numeros a generar", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                    break;
            }
        }
    
    
        private void CmbMetodos_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (CmbMetodos.SelectedIndex == 0)
            {
                TxtA.Enabled = true;
                TxtC.Enabled = true;
                TxtM.Enabled = true;
            }
            else
            {
                if (CmbMetodos.SelectedIndex == 1)
                {
                    TxtC.Enabled = false;
                }
                else
                {
                    if (CmbMetodos.SelectedIndex ==2)
                    {
                        TxtSemilla.Enabled = false;
                        TxtA.Enabled = false;
                        TxtC.Enabled = false;
                        TxtM.Enabled = false;
                    }
                }
            }
        }
        private void generarTabla(List<double> list)
        {
            DataTable tabla = new DataTable();

            tabla.Columns.Add("N°");
            tabla.Columns.Add("Valor");

            for (int i = 0; i < list.Count; i++)
            {
                tabla.Rows.Add(i+1, list[i]);
            }

            GrdNumeros.DataSource = tabla;
        }

    private void BtnLimpiar_Click(object sender, EventArgs e)
    {
      TxtA.Clear();
      TxtC.Clear();
      TxtCantidad.Clear();
      TxtM.Clear();
      TxtSemilla.Clear();
      TxtSemilla.Focus();
    }
    // Validaciones que no permiten ingresar letras o espacios en los campos
    private void TxtSemilla_KeyPress(object sender, KeyPressEventArgs e)
    {
      if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) &&
                (e.KeyChar != '.'))
      {
        e.Handled = true;
      }
    }

    private void TxtA_KeyPress(object sender, KeyPressEventArgs e)
    {
      if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) &&
                (e.KeyChar != '.'))
      {
        e.Handled = true;
      }
    }

    private void TxtC_KeyPress(object sender, KeyPressEventArgs e)
    {
      if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) &&
                (e.KeyChar != '.'))
      {
        e.Handled = true;
      }
    }

    private void TxtM_KeyPress(object sender, KeyPressEventArgs e)
    {
      if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) &&
                (e.KeyChar != '.'))
      {
        e.Handled = true;
      }
    }

    private void TxtCantidad_KeyPress(object sender, KeyPressEventArgs e)
    {
      if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar) &&
                (e.KeyChar != '.'))
      {
        e.Handled = true;
      }
    }
    
  }
}

