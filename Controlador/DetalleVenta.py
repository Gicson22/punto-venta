class DetalleVenta:

    def __init__(self, numero, codigoCliente, NombreApellidos, fecha,
    codigoProducto, descripcion, stock, precio, cantidad):

        self.__numero = numero
        self.__codigoCliente = codigoCliente
        self.__NombreApellidos = NombreApellidos
        self.__fecha = fecha
        self.__codigoProducto = codigoProducto
        self.__descripcion = descripcion
        self.__stock = stock
        self.__precio = precio
        self.__cantidad = cantidad

    def getnumero(self):
        return self.__numero
    
    def getcodigoCliente(self):
        return self.__codigoCliente

    def getNombreApellidos(self):
        return self.__NombreApellidos

    def getfecha(self):
        return self.__fecha

    def getcodigoProducto(self):
        return self.__codigoProducto

    def getdescripcion(self):
        return self.__descripcion

    def getstock(self):
        return self.__stock

    def getprecio(self):
        return self.__precio

    def getcantidad(self):
        return self.__cantidad
    
    def setnumero(self, numero):
        self.__numero = numero
    
    def setcodigoCliente(self, codigoCliente):
        self.codigoCliente = codigoCliente
    
    def setNombreApellidos(self, NombreApellidos):
        self.NombreApellidos = NombreApellidos
    
    def setfecha(self, fecha):
        self.fecha = fecha
    
    def setcodigoProducto(self, codigoProducto):
        self.__codigoProducto = codigoProducto
    
    def setdescripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def setstock(self, stock):
        self.__stock = stock
    
    def setprecio(self, precio):
        self.__precio = precio

    def setcantidad(self, cantidad):
        self.__cantidad = cantidad
    


