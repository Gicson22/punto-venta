from PyQt5 import QtWidgets, uic
from Controlador.ArregloClientes import ArregloClientes
from Controlador.Clientes import *

aCli = ArregloClientes()

class VentanaClientes(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaClientes, self).__init__(parent)
        uic.loadUi("UI/VentanaClientes.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnListar.clicked.connect(self.listar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.listar()

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
        self.tblClientes.setRowCount(aCli.tamañoArregloClientes())
        self.tblClientes.setColumnCount(9)
        for i in range(0, aCli.tamañoArregloClientes()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getDni()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getNombres()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getApellidoPaterno()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getApellidoMaterno()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getDireccion()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getTelefono()))
            
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

            if aCli.buscarClientes(Dni) == -1:
                aCli.adicionaClientes(objCli)
                aCli.grabar()
                self.limpiarControles()               
                self.listar()

            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "El Dni ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

 # Método que permite consultar un Cliente

    def consultar(self):
        self.limpiarTabla()
        if aCli.tamañoArregloClientes() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Clientes", "No existen Clientes a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Clientes", "Ingrese el DNI a consultar...!!!")
            pos = aCli.buscarClientes(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El DNI ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.tblClientes.setRowCount(1)
                self.tblClientes.setItem(0, 0, QtWidgets.QTableWidgetItem(aCli.devolverClientes(pos).getDni()))
                self.tblClientes.setItem(0, 1, QtWidgets.QTableWidgetItem(aCli.devolverClientes(pos).getNombres()))
                self.tblClientes.setItem(0, 2, QtWidgets.QTableWidgetItem(aCli.devolverClientes(pos).getApellidoPaterno()))
                self.tblClientes.setItem(0, 3, QtWidgets.QTableWidgetItem(aCli.devolverClientes(pos).getApellidoMaterno()))
                self.tblClientes.setItem(0, 4, QtWidgets.QTableWidgetItem(aCli.devolverClientes(pos).getDireccion()))
                self.tblClientes.setItem(0, 5, QtWidgets.QTableWidgetItem(aCli.devolverClientes(pos).getTelefono()))
                      
 # Método que permite eliminar un Cliente de la lista

    def eliminar(self):
        if aCli.tamañoArregloClientes() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Clientes", "No existen pClientes a eliminar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblClientes.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                Dni = self.tblClientes.item(indiceFila, 0).text()
                pos = aCli.buscarClientes(Dni)
                aCli.eliminarCliente(pos)
                aCli.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Clientes", "Debe seleccionar un fila...!!!", QtWidgets.QMessageBox.Ok) 

    def modificar(self):
        if aCli.tamañoArregloClientes() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "No existen Clientes a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            Dni, _ = QtWidgets.QInputDialog.getText(self, "Modificar Cliente", "Ingrese el Cliente a modificar...!!!")
            pos = aCli.buscarClientes(Dni)
            if pos != -1:
                objCliente = aCli.devolverClientes(pos)
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtDni.setText(objCliente.getDni())
                self.txtDni.setVisible(False)
                self.lblDni.setVisible(False)
                self.txtNombres.setText(objCliente.getNombres())
                self.txtApellidoPaterno.setText(objCliente.getApellidoPaterno())
                self.txtApellidoMaterno.setText(objCliente.getApellidoMaterno())
                self.txtDireccion.setText(objCliente.getDireccion())
                self.txtTelefono.setText(objCliente.getTelefono())
                
    
    def grabar(self):
        try:
            pos = aCli.buscarClientes(self.obtenerDni())
            objClientes = aCli.devolverClientes(pos)
            objClientes.setNombres(self.obtenerNombres())
            objClientes.setApellidoPaterno(self.obtenerApellidoPaterno())
            objClientes.setApellidoMaterno(self.obtenerApellidoMaterno())
            objClientes.setDireccion(self.obtenerDireccion())
            objClientes.setTelefono(self.obtenerTelefono())
            self.btnModificar.setVisible(True)
            self.btnGrabar.setVisible(False)
            self.limpiarTabla()
            self.limpiarControles()
            aCli.grabar()
            self.listar()
            self.txtDni.setVisible(True)
            self.lblDni.setVisible(True) 
        except:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "Error al intentar modificar...!!!", QtWidgets.QMessageBox.Ok)

