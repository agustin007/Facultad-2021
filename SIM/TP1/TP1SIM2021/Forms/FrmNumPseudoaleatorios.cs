using System;
using System.Collections.Generic;
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

        private void FrmNumPseudoaleatorios_Load(object sender, EventArgs e)
        {
            this.tabPage1.Text = "Numeros Pseudoaleatorios";
            this.tabPage2.Text = "Grafico";
            this.tabPage3.Text = "Integrantes";
            this.CmbMetodos.DataSource = metodos;
            this.CmbMetodos.DisplayMember = "Descripcion";
            this.CmbMetodos.ValueMember = "Id";
            this.CmbMetodos.SelectedIndex = -1;
        }

        private void BtnGenerar_Click(object sender, EventArgs e)
        {
            if (CmbMetodos.SelectedIndex == 0 && TxtSemilla.Text != string.Empty && TxtA.Text != string.Empty && TxtC.Text != string.Empty &&
                TxtM.Text != string.Empty && TxtCantidad.Text != string.Empty) { }

            if (CmbMetodos.SelectedIndex == 1 && TxtSemilla.Text != string.Empty && TxtA.Text != string.Empty &&
                TxtM.Text != string.Empty && TxtCantidad.Text != string.Empty) { }

            if (CmbMetodos.SelectedIndex == 2 && TxtSemilla.Text != string.Empty && TxtCantidad.Text!=string.Empty)
            {
                int semilla = Convert.ToInt32(TxtSemilla.Text);
                int cantidad = Convert.ToInt32(TxtCantidad.Text);
                GrdNumeros.AutoGenerateColumns = true;
                GrdNumeros.DataSource= GeneradorNumerosPseudoaleatorios.GenerarConMetodoProvistoPorLenguaje(cantidad);
            }
            else
            {
                MessageBox.Show("Por favor, ingrese la cantidad de numeros a generar", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
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
                        //TxtSemilla.Enabled = false;
                        TxtA.Enabled = false;
                        TxtC.Enabled = false;
                        TxtM.Enabled = false;
                    }
                }
            }
        }
    }
}

