namespace TP1SIM2021.Classes
{
    class ItemComboBox
    {
        public ItemComboBox (string nombre, int valor)
        {
            this.Nombre = nombre;
            this.Valor = valor;
        }

        public string Nombre { get; set; }
        public int Valor { get; set; }
    }
}
