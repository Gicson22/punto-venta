from Controlador.DetalleVenta import DetalleVenta

class ArregloDetalleVenta:

    def __init__(self):
        self.dataDetalleVenta = []
    
    def adicionaDetalleVenta(self, objVenta):
        self.dataDetalleVenta.append(objVenta)
    
    def devolverDetalleVenta(self, pos):
        return self.dataDetalleVenta[pos]
    
    def tamaĆ±oArregloDetalleVenta(self):
        return len(self.dataDetalleVenta)
    
    def buscarDetalleVenta(self, numero):
        for i in range(self.tamaĆ±oArregloDetalleVenta()):
            if numero == self.dataDetalleVenta[i].getnumero():
                return i
        return -1
    
    def eliminarDetalleVenta(self, indice):
        del(self.dataDetalleVenta[indice])
    
