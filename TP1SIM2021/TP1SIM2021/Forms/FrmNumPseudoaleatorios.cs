using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
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
     //Generarmos una lista de objetos metodos para cargar el comboBox
    List<Metodo> metodos = new List<Metodo>()
    {
      new Metodo {Id=1, Descripcion="Lineal"},
      new Metodo {Id=2, Descripcion = "Congruencial Multiplicativo" },
      new Metodo {Id=3, Descripcion = "Congruencial Mixto"}
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
      if (CmbMetodos.SelectedIndex ==1) { }
      if (CmbMetodos.SelectedIndex == 2){ }
      if (CmbMetodos.SelectedIndex == 3) { }
    }
  }
}
