from Controlador.Clientes import Clientes

class ArregloClientes:

    def __init__(self):
        self.dataClientes = []
        self.cargar()

    def cargar(self):
        archivo = open("Modelo/Clientes.txt","r")
        for linea in archivo.readlines():
            columna = str (linea).split(",")
            dni = columna [0]
            nombres = columna [1]
            apellidoPaterno = columna [2]
            apellidoMaterno = columna [3]
            direccion = columna [4]
            telefono = columna [5].strip()
            objCli = Clientes( dni, nombres, apellidoPaterno, apellidoMaterno, direccion,
            telefono)
            self.adicionaClientes(objCli)
        archivo.close()

    def grabar(self):

        archivo = open("Modelo/Clientes.txt", "w")
        for i in range(self.tamañoArregloClientes()):
            archivo.write(str(self.devolverClientes(i).getDni()) + ","
            + str(self.devolverClientes(i).getNombres()) + ","
            + str(self.devolverClientes(i).getApellidoPaterno()) + ","
            + str(self.devolverClientes(i).getApellidoMaterno()) + ","
            + str(self.devolverClientes(i).getDireccion()) + ","
            + str(self.devolverClientes(i).getTelefono()) + "\n")

        archivo.close()  

    def adicionaClientes(self, objCli):
        self.dataClientes.append(objCli)
    
    def devolverClientes(self, pos):
        return self.dataClientes[pos]
    
    def tamañoArregloClientes(self):
        return len(self.dataClientes)
    
    def buscarClientes(self, Dni):
        for i in range (0, self.tamañoArregloClientes()):
            if Dni == self.dataClientes[i].getDni():
                return i
        return -1
    
    def eliminarCliente(self, indice):
        del(self.dataClientes[indice])

