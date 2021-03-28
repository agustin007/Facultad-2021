namespace TP1SIM2021.Forms
{
    partial class FrmNumPseudoaleatorios
    {
    /// <summary>
    /// Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    /// Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    /// Required method for Designer support - do not modify
    /// the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea2 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend2 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            this.TabPaginas = new System.Windows.Forms.TabControl();
            this.TabPagina1 = new System.Windows.Forms.TabPage();
            this.BtnLimpiar = new System.Windows.Forms.Button();
            this.LblCantidad = new System.Windows.Forms.Label();
            this.TxtCantidad = new System.Windows.Forms.TextBox();
            this.GrdNumerosPseudoaleatorios = new System.Windows.Forms.DataGridView();
            this.TxtM = new System.Windows.Forms.TextBox();
            this.TxtC = new System.Windows.Forms.TextBox();
            this.TxtA = new System.Windows.Forms.TextBox();
            this.LblM = new System.Windows.Forms.Label();
            this.LblC = new System.Windows.Forms.Label();
            this.LblA = new System.Windows.Forms.Label();
            this.LblSemilla = new System.Windows.Forms.Label();
            this.BtnGenerarNumeros = new System.Windows.Forms.Button();
            this.TxtSemilla = new System.Windows.Forms.TextBox();
            this.CmbMetodos = new System.Windows.Forms.ComboBox();
            this.LblMetodo = new System.Windows.Forms.Label();
            this.TabPagina2 = new System.Windows.Forms.TabPage();
            this.chartGraficoFrecuencias = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.CmbIntervalosGrafico = new System.Windows.Forms.ComboBox();
            this.LblIntervalosGrafico = new System.Windows.Forms.Label();
            this.BtnGenerarGrafico = new System.Windows.Forms.Button();
            this.TabPagina3 = new System.Windows.Forms.TabPage();
            this.CmbIntervalosTest = new System.Windows.Forms.ComboBox();
            this.GrdTest = new System.Windows.Forms.DataGridView();
            this.LblAlfaTest = new System.Windows.Forms.Label();
            this.CmbAlfaTest = new System.Windows.Forms.ComboBox();
            this.BtnTest = new System.Windows.Forms.Button();
            this.TabPagina4 = new System.Windows.Forms.TabPage();
            this.TxtIntregantes = new System.Windows.Forms.RichTextBox();
            this.LblIntervalosTest = new System.Windows.Forms.Label();
            this.TabPaginas.SuspendLayout();
            this.TabPagina1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.GrdNumerosPseudoaleatorios)).BeginInit();
            this.TabPagina2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.chartGraficoFrecuencias)).BeginInit();
            this.TabPagina3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.GrdTest)).BeginInit();
            this.TabPagina4.SuspendLayout();
            this.SuspendLayout();
            // 
            // TabPaginas
            // 
            this.TabPaginas.Controls.Add(this.TabPagina1);
            this.TabPaginas.Controls.Add(this.TabPagina2);
            this.TabPaginas.Controls.Add(this.TabPagina3);
            this.TabPaginas.Controls.Add(this.TabPagina4);
            this.TabPaginas.Dock = System.Windows.Forms.DockStyle.Fill;
            this.TabPaginas.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.TabPaginas.Location = new System.Drawing.Point(0, 0);
            this.TabPaginas.Name = "TabPaginas";
            this.TabPaginas.SelectedIndex = 0;
            this.TabPaginas.Size = new System.Drawing.Size(825, 464);
            this.TabPaginas.SizeMode = System.Windows.Forms.TabSizeMode.FillToRight;
            this.TabPaginas.TabIndex = 0;
            // 
            // TabPagina1
            // 
            this.TabPagina1.Controls.Add(this.BtnLimpiar);
            this.TabPagina1.Controls.Add(this.LblCantidad);
            this.TabPagina1.Controls.Add(this.TxtCantidad);
            this.TabPagina1.Controls.Add(this.GrdNumerosPseudoaleatorios);
            this.TabPagina1.Controls.Add(this.TxtM);
            this.TabPagina1.Controls.Add(this.TxtC);
            this.TabPagina1.Controls.Add(this.TxtA);
            this.TabPagina1.Controls.Add(this.LblM);
            this.TabPagina1.Controls.Add(this.LblC);
            this.TabPagina1.Controls.Add(this.LblA);
            this.TabPagina1.Controls.Add(this.LblSemilla);
            this.TabPagina1.Controls.Add(this.BtnGenerarNumeros);
            this.TabPagina1.Controls.Add(this.TxtSemilla);
            this.TabPagina1.Controls.Add(this.CmbMetodos);
            this.TabPagina1.Controls.Add(this.LblMetodo);
            this.TabPagina1.Location = new System.Drawing.Point(4, 25);
            this.TabPagina1.Name = "TabPagina1";
            this.TabPagina1.Padding = new System.Windows.Forms.Padding(3);
            this.TabPagina1.Size = new System.Drawing.Size(817, 435);
            this.TabPagina1.TabIndex = 0;
            this.TabPagina1.UseVisualStyleBackColor = true;
            // 
            // BtnLimpiar
            // 
            this.BtnLimpiar.Location = new System.Drawing.Point(95, 259);
            this.BtnLimpiar.Name = "BtnLimpiar";
            this.BtnLimpiar.Size = new System.Drawing.Size(175, 26);
            this.BtnLimpiar.TabIndex = 11;
            this.BtnLimpiar.Text = "Limpiar";
            this.BtnLimpiar.UseVisualStyleBackColor = true;
            this.BtnLimpiar.Click += new System.EventHandler(this.BtnLimpiar_Click);
            // 
            // LblCantidad
            // 
            this.LblCantidad.AutoSize = true;
            this.LblCantidad.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblCantidad.Location = new System.Drawing.Point(19, 201);
            this.LblCantidad.Name = "LblCantidad";
            this.LblCantidad.Size = new System.Drawing.Size(64, 17);
            this.LblCantidad.TabIndex = 10;
            this.LblCantidad.Text = "Cantidad";
            // 
            // TxtCantidad
            // 
            this.TxtCantidad.Location = new System.Drawing.Point(95, 198);
            this.TxtCantidad.Name = "TxtCantidad";
            this.TxtCantidad.Size = new System.Drawing.Size(175, 23);
            this.TxtCantidad.TabIndex = 6;
            this.TxtCantidad.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtCantidad_KeyPress);
            // 
            // GrdNumerosPseudoaleatorios
            // 
            this.GrdNumerosPseudoaleatorios.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.GrdNumerosPseudoaleatorios.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.GrdNumerosPseudoaleatorios.Dock = System.Windows.Forms.DockStyle.Right;
            this.GrdNumerosPseudoaleatorios.Location = new System.Drawing.Point(288, 3);
            this.GrdNumerosPseudoaleatorios.Name = "GrdNumerosPseudoaleatorios";
            this.GrdNumerosPseudoaleatorios.Size = new System.Drawing.Size(526, 429);
            this.GrdNumerosPseudoaleatorios.TabIndex = 8;
            // 
            // TxtM
            // 
            this.TxtM.Location = new System.Drawing.Point(95, 165);
            this.TxtM.Name = "TxtM";
            this.TxtM.Size = new System.Drawing.Size(175, 23);
            this.TxtM.TabIndex = 5;
            this.TxtM.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtM_KeyPress);
            // 
            // TxtC
            // 
            this.TxtC.Location = new System.Drawing.Point(95, 132);
            this.TxtC.Name = "TxtC";
            this.TxtC.Size = new System.Drawing.Size(175, 23);
            this.TxtC.TabIndex = 4;
            this.TxtC.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtC_KeyPress);
            // 
            // TxtA
            // 
            this.TxtA.Location = new System.Drawing.Point(95, 99);
            this.TxtA.Name = "TxtA";
            this.TxtA.Size = new System.Drawing.Size(175, 23);
            this.TxtA.TabIndex = 3;
            this.TxtA.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtA_KeyPress);
            // 
            // LblM
            // 
            this.LblM.AutoSize = true;
            this.LblM.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblM.Location = new System.Drawing.Point(19, 168);
            this.LblM.Name = "LblM";
            this.LblM.Size = new System.Drawing.Size(19, 17);
            this.LblM.TabIndex = 7;
            this.LblM.Text = "m";
            // 
            // LblC
            // 
            this.LblC.AutoSize = true;
            this.LblC.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblC.Location = new System.Drawing.Point(19, 135);
            this.LblC.Name = "LblC";
            this.LblC.Size = new System.Drawing.Size(15, 17);
            this.LblC.TabIndex = 6;
            this.LblC.Text = "c";
            // 
            // LblA
            // 
            this.LblA.AutoSize = true;
            this.LblA.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblA.Location = new System.Drawing.Point(19, 102);
            this.LblA.Name = "LblA";
            this.LblA.Size = new System.Drawing.Size(16, 17);
            this.LblA.TabIndex = 5;
            this.LblA.Text = "a";
            // 
            // LblSemilla
            // 
            this.LblSemilla.AutoSize = true;
            this.LblSemilla.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblSemilla.Location = new System.Drawing.Point(19, 69);
            this.LblSemilla.Name = "LblSemilla";
            this.LblSemilla.Size = new System.Drawing.Size(53, 17);
            this.LblSemilla.TabIndex = 4;
            this.LblSemilla.Text = "Semilla";
            // 
            // BtnGenerarNumeros
            // 
            this.BtnGenerarNumeros.Location = new System.Drawing.Point(95, 227);
            this.BtnGenerarNumeros.Name = "BtnGenerarNumeros";
            this.BtnGenerarNumeros.Size = new System.Drawing.Size(175, 26);
            this.BtnGenerarNumeros.TabIndex = 7;
            this.BtnGenerarNumeros.Text = "Generar números";
            this.BtnGenerarNumeros.UseVisualStyleBackColor = true;
            this.BtnGenerarNumeros.Click += new System.EventHandler(this.BtnGenerarNumeros_Click);
            // 
            // TxtSemilla
            // 
            this.TxtSemilla.Location = new System.Drawing.Point(95, 66);
            this.TxtSemilla.Name = "TxtSemilla";
            this.TxtSemilla.Size = new System.Drawing.Size(175, 23);
            this.TxtSemilla.TabIndex = 2;
            this.TxtSemilla.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtSemilla_KeyPress);
            // 
            // CmbMetodos
            // 
            this.CmbMetodos.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmbMetodos.FormattingEnabled = true;
            this.CmbMetodos.Location = new System.Drawing.Point(95, 32);
            this.CmbMetodos.Name = "CmbMetodos";
            this.CmbMetodos.Size = new System.Drawing.Size(175, 24);
            this.CmbMetodos.TabIndex = 1;
            this.CmbMetodos.SelectedIndexChanged += new System.EventHandler(this.CmbMetodos_SelectedIndexChanged);
            // 
            // LblMetodo
            // 
            this.LblMetodo.AutoSize = true;
            this.LblMetodo.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblMetodo.Location = new System.Drawing.Point(19, 35);
            this.LblMetodo.Name = "LblMetodo";
            this.LblMetodo.Size = new System.Drawing.Size(55, 17);
            this.LblMetodo.TabIndex = 0;
            this.LblMetodo.Text = "Metodo";
            // 
            // TabPagina2
            // 
            this.TabPagina2.Controls.Add(this.chartGraficoFrecuencias);
            this.TabPagina2.Controls.Add(this.CmbIntervalosGrafico);
            this.TabPagina2.Controls.Add(this.LblIntervalosGrafico);
            this.TabPagina2.Controls.Add(this.BtnGenerarGrafico);
            this.TabPagina2.Location = new System.Drawing.Point(4, 25);
            this.TabPagina2.Name = "TabPagina2";
            this.TabPagina2.Padding = new System.Windows.Forms.Padding(3);
            this.TabPagina2.Size = new System.Drawing.Size(817, 435);
            this.TabPagina2.TabIndex = 1;
            this.TabPagina2.UseVisualStyleBackColor = true;
            // 
            // chartGraficoFrecuencias
            // 
            this.chartGraficoFrecuencias.BorderlineColor = System.Drawing.Color.Black;
            this.chartGraficoFrecuencias.BorderlineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Solid;
            chartArea2.Name = "ChartArea1";
            this.chartGraficoFrecuencias.ChartAreas.Add(chartArea2);
            this.chartGraficoFrecuencias.Dock = System.Windows.Forms.DockStyle.Bottom;
            legend2.Name = "Legend1";
            this.chartGraficoFrecuencias.Legends.Add(legend2);
            this.chartGraficoFrecuencias.Location = new System.Drawing.Point(3, 98);
            this.chartGraficoFrecuencias.Name = "chartGraficoFrecuencias";
            this.chartGraficoFrecuencias.Size = new System.Drawing.Size(811, 334);
            this.chartGraficoFrecuencias.TabIndex = 3;
            this.chartGraficoFrecuencias.Text = "chartGrafico";
            // 
            // CmbIntervalosGrafico
            // 
            this.CmbIntervalosGrafico.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmbIntervalosGrafico.FormattingEnabled = true;
            this.CmbIntervalosGrafico.Location = new System.Drawing.Point(95, 32);
            this.CmbIntervalosGrafico.Name = "CmbIntervalosGrafico";
            this.CmbIntervalosGrafico.Size = new System.Drawing.Size(175, 24);
            this.CmbIntervalosGrafico.TabIndex = 2;
            // 
            // LblIntervalosGrafico
            // 
            this.LblIntervalosGrafico.AutoSize = true;
            this.LblIntervalosGrafico.Location = new System.Drawing.Point(20, 35);
            this.LblIntervalosGrafico.Name = "LblIntervalosGrafico";
            this.LblIntervalosGrafico.Size = new System.Drawing.Size(69, 17);
            this.LblIntervalosGrafico.TabIndex = 1;
            this.LblIntervalosGrafico.Text = "Intervalos";
            // 
            // BtnGenerarGrafico
            // 
            this.BtnGenerarGrafico.Location = new System.Drawing.Point(95, 62);
            this.BtnGenerarGrafico.Name = "BtnGenerarGrafico";
            this.BtnGenerarGrafico.Size = new System.Drawing.Size(177, 30);
            this.BtnGenerarGrafico.TabIndex = 0;
            this.BtnGenerarGrafico.Text = "Generar Gráfico";
            this.BtnGenerarGrafico.UseVisualStyleBackColor = true;
            this.BtnGenerarGrafico.Click += new System.EventHandler(this.BtnGenerarGrafico_Click);
            // 
            // TabPagina3
            // 
            this.TabPagina3.Controls.Add(this.LblIntervalosTest);
            this.TabPagina3.Controls.Add(this.CmbIntervalosTest);
            this.TabPagina3.Controls.Add(this.GrdTest);
            this.TabPagina3.Controls.Add(this.LblAlfaTest);
            this.TabPagina3.Controls.Add(this.CmbAlfaTest);
            this.TabPagina3.Controls.Add(this.BtnTest);
            this.TabPagina3.Location = new System.Drawing.Point(4, 25);
            this.TabPagina3.Name = "TabPagina3";
            this.TabPagina3.Padding = new System.Windows.Forms.Padding(3);
            this.TabPagina3.Size = new System.Drawing.Size(817, 435);
            this.TabPagina3.TabIndex = 3;
            this.TabPagina3.UseVisualStyleBackColor = true;
            // 
            // CmbIntervalosTest
            // 
            this.CmbIntervalosTest.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmbIntervalosTest.FormattingEnabled = true;
            this.CmbIntervalosTest.Location = new System.Drawing.Point(95, 32);
            this.CmbIntervalosTest.Name = "CmbIntervalosTest";
            this.CmbIntervalosTest.Size = new System.Drawing.Size(175, 24);
            this.CmbIntervalosTest.TabIndex = 10;
            // 
            // GrdTest
            // 
            this.GrdTest.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.GrdTest.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.GrdTest.Dock = System.Windows.Forms.DockStyle.Right;
            this.GrdTest.Location = new System.Drawing.Point(288, 3);
            this.GrdTest.Name = "GrdTest";
            this.GrdTest.Size = new System.Drawing.Size(526, 429);
            this.GrdTest.TabIndex = 9;
            // 
            // LblAlfaTest
            // 
            this.LblAlfaTest.AutoSize = true;
            this.LblAlfaTest.Location = new System.Drawing.Point(20, 69);
            this.LblAlfaTest.Name = "LblAlfaTest";
            this.LblAlfaTest.Size = new System.Drawing.Size(32, 17);
            this.LblAlfaTest.TabIndex = 6;
            this.LblAlfaTest.Text = "Alfa";
            // 
            // CmbAlfaTest
            // 
            this.CmbAlfaTest.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmbAlfaTest.FormattingEnabled = true;
            this.CmbAlfaTest.Location = new System.Drawing.Point(95, 66);
            this.CmbAlfaTest.Name = "CmbAlfaTest";
            this.CmbAlfaTest.Size = new System.Drawing.Size(175, 24);
            this.CmbAlfaTest.TabIndex = 5;
            // 
            // BtnTest
            // 
            this.BtnTest.Location = new System.Drawing.Point(95, 99);
            this.BtnTest.Name = "BtnTest";
            this.BtnTest.Size = new System.Drawing.Size(177, 30);
            this.BtnTest.TabIndex = 4;
            this.BtnTest.Text = "Test de Chi Cuadrado";
            this.BtnTest.UseVisualStyleBackColor = true;
            this.BtnTest.Click += new System.EventHandler(this.BtnTest_Click);
            // 
            // TabPagina4
            // 
            this.TabPagina4.Controls.Add(this.TxtIntregantes);
            this.TabPagina4.Location = new System.Drawing.Point(4, 25);
            this.TabPagina4.Name = "TabPagina4";
            this.TabPagina4.Padding = new System.Windows.Forms.Padding(3);
            this.TabPagina4.Size = new System.Drawing.Size(817, 435);
            this.TabPagina4.TabIndex = 2;
            this.TabPagina4.UseVisualStyleBackColor = true;
            // 
            // TxtIntregantes
            // 
            this.TxtIntregantes.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.TxtIntregantes.Location = new System.Drawing.Point(6, 6);
            this.TxtIntregantes.Name = "TxtIntregantes";
            this.TxtIntregantes.ReadOnly = true;
            this.TxtIntregantes.Size = new System.Drawing.Size(163, 134);
            this.TxtIntregantes.TabIndex = 1;
            this.TxtIntregantes.Text = "Agustín Carranza 67298, Marcos Mariatti 70707, Erik Martinez 66697, Chiara Masset" +
    "ti 74184, Gonzalo Medrano 72412, Facundo Mondati 74284";
            // 
            // LblIntervalosTest
            // 
            this.LblIntervalosTest.AutoSize = true;
            this.LblIntervalosTest.Location = new System.Drawing.Point(20, 35);
            this.LblIntervalosTest.Name = "LblIntervalosTest";
            this.LblIntervalosTest.Size = new System.Drawing.Size(69, 17);
            this.LblIntervalosTest.TabIndex = 11;
            this.LblIntervalosTest.Text = "Intervalos";
            // 
            // FrmNumPseudoaleatorios
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(825, 464);
            this.Controls.Add(this.TabPaginas);
            this.Name = "FrmNumPseudoaleatorios";
            this.Text = "TP1";
            this.Load += new System.EventHandler(this.FrmNumPseudoaleatorios_Load);
            this.TabPaginas.ResumeLayout(false);
            this.TabPagina1.ResumeLayout(false);
            this.TabPagina1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.GrdNumerosPseudoaleatorios)).EndInit();
            this.TabPagina2.ResumeLayout(false);
            this.TabPagina2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.chartGraficoFrecuencias)).EndInit();
            this.TabPagina3.ResumeLayout(false);
            this.TabPagina3.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.GrdTest)).EndInit();
            this.TabPagina4.ResumeLayout(false);
            this.ResumeLayout(false);

    }

    #endregion

        private System.Windows.Forms.TabControl TabPaginas;
        private System.Windows.Forms.TabPage TabPagina1;
        private System.Windows.Forms.TabPage TabPagina2;
        private System.Windows.Forms.TabPage TabPagina4;
        private System.Windows.Forms.RichTextBox TxtIntregantes;
        private System.Windows.Forms.TextBox TxtM;
        private System.Windows.Forms.TextBox TxtC;
        private System.Windows.Forms.TextBox TxtA;
        private System.Windows.Forms.Label LblM;
        private System.Windows.Forms.Label LblC;
        private System.Windows.Forms.Label LblA;
        private System.Windows.Forms.Label LblSemilla;
        private System.Windows.Forms.Button BtnGenerarNumeros;
        private System.Windows.Forms.TextBox TxtSemilla;
        private System.Windows.Forms.ComboBox CmbMetodos;
        private System.Windows.Forms.Label LblMetodo;
        private System.Windows.Forms.Label LblCantidad;
        private System.Windows.Forms.TextBox TxtCantidad;
        private System.Windows.Forms.Button BtnLimpiar;
        private System.Windows.Forms.ComboBox CmbIntervalosGrafico;
        private System.Windows.Forms.Label LblIntervalosGrafico;
        private System.Windows.Forms.Button BtnGenerarGrafico;
        private System.Windows.Forms.TabPage TabPagina3;
        private System.Windows.Forms.Button BtnTest;
        private System.Windows.Forms.Label LblAlfaTest;
        private System.Windows.Forms.ComboBox CmbAlfaTest;
        private System.Windows.Forms.DataGridView GrdNumerosPseudoaleatorios;
        private System.Windows.Forms.DataGridView GrdTest;
        private System.Windows.Forms.DataVisualization.Charting.Chart chartGraficoFrecuencias;
        private System.Windows.Forms.ComboBox CmbIntervalosTest;
        private System.Windows.Forms.Label LblIntervalosTest;
    }
}