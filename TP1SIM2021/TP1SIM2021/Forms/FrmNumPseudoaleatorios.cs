using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TP1SIM2021.Forms
{
  public partial class FrmNumPseudoaleatorios : Form
  {
    public FrmNumPseudoaleatorios()
    {
      InitializeComponent();
    }

    private void FrmNumPseudoaleatorios_Load(object sender, EventArgs e)
    {
      this.tabPage1.Text = "Numeros Pseudoaleatorios";
      this.tabPage2.Text = "Grafico";
      this.tabPage3.Text = "Integrantes";
    }
  }
}
