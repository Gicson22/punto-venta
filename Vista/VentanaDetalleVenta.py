from PyQt5 import QtWidgets, uic
from Controlador.ArregloClientes import ArregloClientes
from Controlador.Clientes import *

aPro = ArregloClientes()

class VentanaVentas(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaVentas, self).__init__(parent)
        uic.loadUi("UI/VentanaVentas.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnListar.clicked.connect(self.listar)

    # Métodos para obtener los valores de las cajas de texto
    # y de los combobox

    def obtenerDni(self):
        return self.txtDni.text()
    
    def obtenerNombres(self):
        return self.txtNombres.text()
    
    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()
    
    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()
    
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    
    def obtenerTelefono(self):
        return self.txtTelefono.text()


    # Método que permite limpiar la tabla

    def limpiarTabla(self):
        self.tblClientes.clearContents()
        self.tblClientes.setRowCount(0)
    
    # Método permite validar que los campos estén llenos

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del Cliente...!!!"
        if self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombres del Cliente...!!!"
        if self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del Cliente...!!!"
        if self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del Cliente...!!!"
        if self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Direccion del Cliente...!!!"
        if self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Direccion del Cliente...!!!"
        else:
            return ""
    
    # Método que permite mostrar los datos en la tabla Clientes

    def listar(self):
        self.tblClientes.setRowCount(aPro.tamañoArregloClientes())
        self.tblClientes.setColumnCount(9)
        for i in range(0, aPro.tamañoArregloClientes()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aPro.devolverClientes(i).getDni()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aPro.devolverClientes(i).getNombres()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aPro.devolverClientes(i).getApellidoPaterno()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aPro.devolverClientes(i).getApellidoMaterno()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aPro.devolverClientes(i).getDireccion()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aPro.devolverClientes(i).getTelefono()))
            
    # Método que permite limpiar las cajas de texo y los combobox

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()
    
    # Método que permite registrar los datos en la tabla

    def registrar(self):
        if self.valida() == "":
            objCli = Clientes(self.obtenerDni(), self.obtenerNombres(), self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenerTelefono())
            Dni = self.obtenerDni()

            if aPro.buscarClientes(Dni) == -1:
                aPro.adicionaClientes(objCli)
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "El Dni ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

 # Método que permite consultar un Cliente

    def consultar(self):
        self.limpiarTabla()
        if aPro.tamañoArregloClientes() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Clientes", "No existen Clientes a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Clientes", "Ingrese el DNI a consultar...!!!")
            pos = aPro.buscarClientes(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El DNI ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.tblClientes.setRowCount(1)
                self.tblClientes.setItem(0, 0, QtWidgets.QTableWidgetItem(aPro.devolverClientes(pos).getDni()))
                self.tblClientes.setItem(0, 1, QtWidgets.QTableWidgetItem(aPro.devolverClientes(pos).getNombres()))
                self.tblClientes.setItem(0, 2, QtWidgets.QTableWidgetItem(aPro.devolverClientes(pos).getApellidoPaterno()))
                self.tblClientes.setItem(0, 3, QtWidgets.QTableWidgetItem(aPro.devolverClientes(pos).getApellidoMaterno()))
                self.tblClientes.setItem(0, 4, QtWidgets.QTableWidgetItem(aPro.devolverClientes(pos).getDireccion()))
                self.tblClientes.setItem(0, 5, QtWidgets.QTableWidgetItem(aPro.devolverClientes(pos).getTelefono()))
                      
 # Método que permite eliminar un Cliente de la lista



    def eliminar(self):

        if aPro.tamañoArregloClientes() == 0:

            QtWidgets.QMessageBox.information(self, "Eliminar Clientes", "No existen pClientes a eliminar...!!!", QtWidgets.QMessageBox.Ok)

        else:

            fila = self.tblClientes.selectedItems()

            if fila:

                indiceFila = fila[0].row()

                Dni = self.tblClientes.item(indiceFila, 0).text()

                pos = aPro.buscarClientes(Dni)

                aPro.eliminarCliente(pos)

                self.limpiarTabla()

                self.listar()

            else:

                QtWidgets.QMessageBox.information(self, "Eliminar Clientes", "Debe seleccionar un fila...!!!", QtWidgets.QMessageBox.Ok)    

