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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
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
            this.LblIntervalosTest = new System.Windows.Forms.Label();
            this.CmbIntervalosTest = new System.Windows.Forms.ComboBox();
            this.GrdTest = new System.Windows.Forms.DataGridView();
            this.BtnTest = new System.Windows.Forms.Button();
            this.TabPagina4 = new System.Windows.Forms.TabPage();
            this.TxtIntregantes = new System.Windows.Forms.RichTextBox();
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
            this.TabPaginas.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPaginas.Name = "TabPaginas";
            this.TabPaginas.SelectedIndex = 0;
            this.TabPaginas.Size = new System.Drawing.Size(1100, 571);
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
            this.TabPagina1.Location = new System.Drawing.Point(4, 29);
            this.TabPagina1.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPagina1.Name = "TabPagina1";
            this.TabPagina1.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPagina1.Size = new System.Drawing.Size(1092, 538);
            this.TabPagina1.TabIndex = 0;
            this.TabPagina1.Text = "Numeros Pseudoaleatorios";
            this.TabPagina1.UseVisualStyleBackColor = true;
            // 
            // BtnLimpiar
            // 
            this.BtnLimpiar.Location = new System.Drawing.Point(127, 319);
            this.BtnLimpiar.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.BtnLimpiar.Name = "BtnLimpiar";
            this.BtnLimpiar.Size = new System.Drawing.Size(233, 32);
            this.BtnLimpiar.TabIndex = 11;
            this.BtnLimpiar.Text = "Limpiar";
            this.BtnLimpiar.UseVisualStyleBackColor = true;
            this.BtnLimpiar.Click += new System.EventHandler(this.BtnLimpiar_Click);
            // 
            // LblCantidad
            // 
            this.LblCantidad.AutoSize = true;
            this.LblCantidad.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblCantidad.Location = new System.Drawing.Point(25, 247);
            this.LblCantidad.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblCantidad.Name = "LblCantidad";
            this.LblCantidad.Size = new System.Drawing.Size(75, 20);
            this.LblCantidad.TabIndex = 10;
            this.LblCantidad.Text = "Cantidad";
            // 
            // TxtCantidad
            // 
            this.TxtCantidad.Location = new System.Drawing.Point(127, 244);
            this.TxtCantidad.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TxtCantidad.Name = "TxtCantidad";
            this.TxtCantidad.Size = new System.Drawing.Size(232, 26);
            this.TxtCantidad.TabIndex = 6;
            this.TxtCantidad.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtCantidad_KeyPress);
            // 
            // GrdNumerosPseudoaleatorios
            // 
            this.GrdNumerosPseudoaleatorios.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.GrdNumerosPseudoaleatorios.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.GrdNumerosPseudoaleatorios.Dock = System.Windows.Forms.DockStyle.Right;
            this.GrdNumerosPseudoaleatorios.Location = new System.Drawing.Point(387, 4);
            this.GrdNumerosPseudoaleatorios.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.GrdNumerosPseudoaleatorios.Name = "GrdNumerosPseudoaleatorios";
            this.GrdNumerosPseudoaleatorios.RowHeadersWidth = 51;
            this.GrdNumerosPseudoaleatorios.Size = new System.Drawing.Size(701, 530);
            this.GrdNumerosPseudoaleatorios.TabIndex = 8;
            // 
            // TxtM
            // 
            this.TxtM.Location = new System.Drawing.Point(127, 203);
            this.TxtM.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TxtM.Name = "TxtM";
            this.TxtM.Size = new System.Drawing.Size(232, 26);
            this.TxtM.TabIndex = 5;
            this.TxtM.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtM_KeyPress);
            // 
            // TxtC
            // 
            this.TxtC.Location = new System.Drawing.Point(127, 162);
            this.TxtC.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TxtC.Name = "TxtC";
            this.TxtC.Size = new System.Drawing.Size(232, 26);
            this.TxtC.TabIndex = 4;
            this.TxtC.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtC_KeyPress);
            // 
            // TxtA
            // 
            this.TxtA.Location = new System.Drawing.Point(127, 122);
            this.TxtA.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TxtA.Name = "TxtA";
            this.TxtA.Size = new System.Drawing.Size(232, 26);
            this.TxtA.TabIndex = 3;
            this.TxtA.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtA_KeyPress);
            // 
            // LblM
            // 
            this.LblM.AutoSize = true;
            this.LblM.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblM.Location = new System.Drawing.Point(25, 207);
            this.LblM.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblM.Name = "LblM";
            this.LblM.Size = new System.Drawing.Size(23, 20);
            this.LblM.TabIndex = 7;
            this.LblM.Text = "m";
            // 
            // LblC
            // 
            this.LblC.AutoSize = true;
            this.LblC.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblC.Location = new System.Drawing.Point(25, 166);
            this.LblC.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblC.Name = "LblC";
            this.LblC.Size = new System.Drawing.Size(18, 20);
            this.LblC.TabIndex = 6;
            this.LblC.Text = "c";
            // 
            // LblA
            // 
            this.LblA.AutoSize = true;
            this.LblA.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblA.Location = new System.Drawing.Point(25, 126);
            this.LblA.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblA.Name = "LblA";
            this.LblA.Size = new System.Drawing.Size(18, 20);
            this.LblA.TabIndex = 5;
            this.LblA.Text = "a";
            // 
            // LblSemilla
            // 
            this.LblSemilla.AutoSize = true;
            this.LblSemilla.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblSemilla.Location = new System.Drawing.Point(25, 85);
            this.LblSemilla.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblSemilla.Name = "LblSemilla";
            this.LblSemilla.Size = new System.Drawing.Size(64, 20);
            this.LblSemilla.TabIndex = 4;
            this.LblSemilla.Text = "Semilla";
            // 
            // BtnGenerarNumeros
            // 
            this.BtnGenerarNumeros.Location = new System.Drawing.Point(127, 279);
            this.BtnGenerarNumeros.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.BtnGenerarNumeros.Name = "BtnGenerarNumeros";
            this.BtnGenerarNumeros.Size = new System.Drawing.Size(233, 32);
            this.BtnGenerarNumeros.TabIndex = 7;
            this.BtnGenerarNumeros.Text = "Generar números";
            this.BtnGenerarNumeros.UseVisualStyleBackColor = true;
            this.BtnGenerarNumeros.Click += new System.EventHandler(this.BtnGenerarNumeros_Click);
            // 
            // TxtSemilla
            // 
            this.TxtSemilla.Location = new System.Drawing.Point(127, 81);
            this.TxtSemilla.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TxtSemilla.Name = "TxtSemilla";
            this.TxtSemilla.Size = new System.Drawing.Size(232, 26);
            this.TxtSemilla.TabIndex = 2;
            this.TxtSemilla.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TxtSemilla_KeyPress);
            // 
            // CmbMetodos
            // 
            this.CmbMetodos.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmbMetodos.FormattingEnabled = true;
            this.CmbMetodos.Location = new System.Drawing.Point(127, 39);
            this.CmbMetodos.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.CmbMetodos.Name = "CmbMetodos";
            this.CmbMetodos.Size = new System.Drawing.Size(232, 28);
            this.CmbMetodos.TabIndex = 1;
            this.CmbMetodos.SelectedIndexChanged += new System.EventHandler(this.CmbMetodos_SelectedIndexChanged);
            // 
            // LblMetodo
            // 
            this.LblMetodo.AutoSize = true;
            this.LblMetodo.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.LblMetodo.Location = new System.Drawing.Point(25, 43);
            this.LblMetodo.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblMetodo.Name = "LblMetodo";
            this.LblMetodo.Size = new System.Drawing.Size(64, 20);
            this.LblMetodo.TabIndex = 0;
            this.LblMetodo.Text = "Metodo";
            // 
            // TabPagina2
            // 
            this.TabPagina2.Controls.Add(this.chartGraficoFrecuencias);
            this.TabPagina2.Controls.Add(this.CmbIntervalosGrafico);
            this.TabPagina2.Controls.Add(this.LblIntervalosGrafico);
            this.TabPagina2.Controls.Add(this.BtnGenerarGrafico);
            this.TabPagina2.Location = new System.Drawing.Point(4, 29);
            this.TabPagina2.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPagina2.Name = "TabPagina2";
            this.TabPagina2.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPagina2.Size = new System.Drawing.Size(1092, 538);
            this.TabPagina2.TabIndex = 1;
            this.TabPagina2.Text = "Grafico";
            this.TabPagina2.UseVisualStyleBackColor = true;
            // 
            // chartGraficoFrecuencias
            // 
            this.chartGraficoFrecuencias.BorderlineColor = System.Drawing.Color.Black;
            this.chartGraficoFrecuencias.BorderlineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Solid;
            chartArea1.AxisX.IntervalOffsetType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea1.AxisX.IntervalType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea1.AxisX2.IntervalOffsetType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea1.AxisX2.IntervalType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea1.AxisY.IntervalOffsetType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea1.AxisY.IntervalType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea1.Name = "AreaHisto";
            this.chartGraficoFrecuencias.ChartAreas.Add(chartArea1);
            this.chartGraficoFrecuencias.Dock = System.Windows.Forms.DockStyle.Bottom;
            legend1.Name = "Legend1";
            this.chartGraficoFrecuencias.Legends.Add(legend1);
            this.chartGraficoFrecuencias.Location = new System.Drawing.Point(4, 143);
            this.chartGraficoFrecuencias.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.chartGraficoFrecuencias.Name = "chartGraficoFrecuencias";
            this.chartGraficoFrecuencias.Size = new System.Drawing.Size(1084, 391);
            this.chartGraficoFrecuencias.TabIndex = 3;
            this.chartGraficoFrecuencias.Text = "chartGrafico";
            // 
            // CmbIntervalosGrafico
            // 
            this.CmbIntervalosGrafico.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmbIntervalosGrafico.FormattingEnabled = true;
            this.CmbIntervalosGrafico.Location = new System.Drawing.Point(127, 39);
            this.CmbIntervalosGrafico.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.CmbIntervalosGrafico.Name = "CmbIntervalosGrafico";
            this.CmbIntervalosGrafico.Size = new System.Drawing.Size(232, 28);
            this.CmbIntervalosGrafico.TabIndex = 2;
            // 
            // LblIntervalosGrafico
            // 
            this.LblIntervalosGrafico.AutoSize = true;
            this.LblIntervalosGrafico.Location = new System.Drawing.Point(27, 43);
            this.LblIntervalosGrafico.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblIntervalosGrafico.Name = "LblIntervalosGrafico";
            this.LblIntervalosGrafico.Size = new System.Drawing.Size(81, 20);
            this.LblIntervalosGrafico.TabIndex = 1;
            this.LblIntervalosGrafico.Text = "Intervalos";
            // 
            // BtnGenerarGrafico
            // 
            this.BtnGenerarGrafico.Location = new System.Drawing.Point(127, 81);
            this.BtnGenerarGrafico.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.BtnGenerarGrafico.Name = "BtnGenerarGrafico";
            this.BtnGenerarGrafico.Size = new System.Drawing.Size(236, 37);
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
            this.TabPagina3.Controls.Add(this.BtnTest);
            this.TabPagina3.Location = new System.Drawing.Point(4, 29);
            this.TabPagina3.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPagina3.Name = "TabPagina3";
            this.TabPagina3.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPagina3.Size = new System.Drawing.Size(1092, 538);
            this.TabPagina3.TabIndex = 3;
            this.TabPagina3.Text = "Test de Chi Cuadrado";
            this.TabPagina3.UseVisualStyleBackColor = true;
            // 
            // LblIntervalosTest
            // 
            this.LblIntervalosTest.AutoSize = true;
            this.LblIntervalosTest.Location = new System.Drawing.Point(27, 43);
            this.LblIntervalosTest.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblIntervalosTest.Name = "LblIntervalosTest";
            this.LblIntervalosTest.Size = new System.Drawing.Size(81, 20);
            this.LblIntervalosTest.TabIndex = 11;
            this.LblIntervalosTest.Text = "Intervalos";
            // 
            // CmbIntervalosTest
            // 
            this.CmbIntervalosTest.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmbIntervalosTest.FormattingEnabled = true;
            this.CmbIntervalosTest.Location = new System.Drawing.Point(127, 39);
            this.CmbIntervalosTest.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.CmbIntervalosTest.Name = "CmbIntervalosTest";
            this.CmbIntervalosTest.Size = new System.Drawing.Size(232, 28);
            this.CmbIntervalosTest.TabIndex = 10;
            // 
            // GrdTest
            // 
            this.GrdTest.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.GrdTest.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.GrdTest.Dock = System.Windows.Forms.DockStyle.Right;
            this.GrdTest.Location = new System.Drawing.Point(387, 4);
            this.GrdTest.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.GrdTest.Name = "GrdTest";
            this.GrdTest.RowHeadersWidth = 51;
            this.GrdTest.Size = new System.Drawing.Size(701, 530);
            this.GrdTest.TabIndex = 9;
            // 
            // BtnTest
            // 
            this.BtnTest.Location = new System.Drawing.Point(127, 81);
            this.BtnTest.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.BtnTest.Name = "BtnTest";
            this.BtnTest.Size = new System.Drawing.Size(236, 37);
            this.BtnTest.TabIndex = 4;
            this.BtnTest.Text = "Test de Chi Cuadrado";
            this.BtnTest.UseVisualStyleBackColor = true;
            this.BtnTest.Click += new System.EventHandler(this.BtnTest_Click);
            // 
            // TabPagina4
            // 
            this.TabPagina4.Controls.Add(this.TxtIntregantes);
            this.TabPagina4.Location = new System.Drawing.Point(4, 29);
            this.TabPagina4.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPagina4.Name = "TabPagina4";
            this.TabPagina4.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TabPagina4.Size = new System.Drawing.Size(1092, 538);
            this.TabPagina4.TabIndex = 2;
            this.TabPagina4.Text = "Integrantes";
            this.TabPagina4.UseVisualStyleBackColor = true;
            // 
            // TxtIntregantes
            // 
            this.TxtIntregantes.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.TxtIntregantes.Location = new System.Drawing.Point(8, 7);
            this.TxtIntregantes.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.TxtIntregantes.Name = "TxtIntregantes";
            this.TxtIntregantes.ReadOnly = true;
            this.TxtIntregantes.Size = new System.Drawing.Size(216, 164);
            this.TxtIntregantes.TabIndex = 1;
            this.TxtIntregantes.Text = "Agustín Carranza 67298, Marcos Mariatti 70707, Erik Martinez 66697, Chiara Masset" +
    "ti 74184, Gonzalo Medrano 72412, Facundo Mondati 74284";
            // 
            // FrmNumPseudoaleatorios
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1100, 571);
            this.Controls.Add(this.TabPaginas);
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
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
        private System.Windows.Forms.DataGridView GrdNumerosPseudoaleatorios;
        private System.Windows.Forms.DataGridView GrdTest;
        private System.Windows.Forms.DataVisualization.Charting.Chart chartGraficoFrecuencias;
        private System.Windows.Forms.ComboBox CmbIntervalosTest;
        private System.Windows.Forms.Label LblIntervalosTest;
    }
}