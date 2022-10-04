from PyQt5 import QtWidgets, uic
from Controlador.ArregloClientes import *
from Controlador.ArregloProductos import *
from Vista.VentanaClientes import *
from Vista.VentanaProductos import *

lista = []

class VentanaVentas(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaVentas, self).__init__(parent)
        uic.loadUi("UI/VentanaVentas.ui", self)

        self.btnBuscarCliente.clicked.connect(self.buscarCliente)
        self.btnBuscarProducto.clicked.connect(self.buscarProducto)
        self.btnAgregar.clicked.connect(self.agregar)
        self.item = 0
        self.stock_actual_temporal = {}

    def obtenerStockActualTemporal(self, codigoProducto):
        stockEncontrado = -1
        if len(self.stock_actual_temporal) != 0:
            for llave in self.stock_actual_temporal:
                if llave == codigoProducto:
                    stockEncontrado = self.stock_actual_temporal[llave]
                    return stockEncontrado
        return stockEncontrado

    def actualizarStockActualTemporal(self,codigoProducto, cantidad):  
        for llave in self.stock_actual_temporal:
            if llave == codigoProducto:
                self.stock_actual_temporal[llave] = self.stock_actual_temporal[llave] - cantidad

    def actualizarStock(self):
        for i in range(self.tblDetalle.rowCount()):
            codigoProducto = self.tblDetalle.item(i,1).text()
            cantidad = int(self.tblDetalle.item(i,4).text())
            pos = aPro.buscarProducto(codigoProducto)
            objProducto = aPro.devolverProducto(pos)
            stock_actual = int(objProducto.getStockActual()) - cantidad
            aPro.actualizarStock(stock_actual, codigoProducto)


    def buscarCliente(self):
        codigoCliente = self.txtCodigoCliente.text()
        if codigoCliente == "":
            QtWidgets.QMessageBox.information(self, "Dni Cliente", "Debe ingresar el Dni del cliente...!!!", QtWidgets.QMessageBox.Ok)
        else:
            pos = aCli.buscarClientes(codigoCliente)
            objCliente = aCli.devolverClientes(pos)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Dni Cliente", "Cliente no registrado...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.txtNombres.setText(objCliente.getNombres() + " " + objCliente.getApellidoPaterno() + " " + objCliente.getApellidoMaterno())

    def buscarProducto(self):
        codigo = self.txtCodigoProducto.text()
        if codigo == "":
            QtWidgets.QMessageBox.information(self, "Código Producto", "Debe ingresar el código del producto...!!!", QtWidgets.QMessageBox.Ok)
        else:
            pos = aPro.buscarProducto(codigo)
            objProducto = aPro.devolverProducto(pos)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Código Producto", "Producto no registrado...!!!", QtWidgets.QMessageBox.Ok)
            else:
                stock_temporal = self.obtenerStockActualTemporal(codigo)
                if stock_temporal == -1:
                    self.stock_actual_temporal[self.txtCodigoProducto.
                    text()] = int(objProducto.getStockActual())
                    stock_temporal = self.obtenerStockActualTemporal(codigo)
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.txtStock.setText(str(stock_temporal))
                #self.txtStock.setText(objProducto.getStockActual())
                self.txtPrecio.setText(objProducto.getPrecioVenta())



    def obtenerCodigo(self):
        return self.txtCodigoProducto.text()

    def obtenerDescripcion(self):
        return self.txtDescripcion.text()

    def obtenerPrecio(self):
        return float(self.txtPrecio.text())

    def obtenerCantidad(self):
        return int(self.txtCantidad.text())

    def obtenerItem(self):
        self.item = self.item + 1
        return self.item


    def agregar(self):
        try:
            if self.obtenerCantidad() > int(self.txtStock.text()):
                QtWidgets.QMessageBox.information(self, "Venta", "No se puede vender esa cantidad...!!!", QtWidgets.QMessageBox.Ok)
            elif self.obtenerCantidad() <= 0:
                QtWidgets.QMessageBox.information(self, "Venta", "La cantidad ingresada es incorrecta...!!!", QtWidgets.QMessageBox.Ok)
            else:
                lista.append((self.obtenerItem(), self.obtenerCodigo(),self.
                obtenerDescripcion(), self.obtenerPrecio(), self.obtenerCantidad(),
                self.obtenerPrecio()*self.obtenerCantidad()))
                self.actualizarStockActualTemporal(self.obtenerCodigo(),self.
                obtenerCantidad())
                self.mostrarDetalle()
                self.calcularPago()
        except:
            QtWidgets.QMessageBox.information(self, "Venta", "Existe un error al agregar los productos...!!!", QtWidgets.QMessageBox.Ok)
            self.item = self.item - 1

    def mostrarDetalle(self):
        self.tblDetalle.setRowCount(len(lista))
        self.tblDetalle.setColumnCount(6)
        for i in range(len(lista)):
            self.tblDetalle.setItem(i, 0, QtWidgets.QTableWidgetItem(str(lista[i][0])))
            self.tblDetalle.setItem(i, 1, QtWidgets.QTableWidgetItem(str(lista[i][1])))
            self.tblDetalle.setItem(i, 2, QtWidgets.QTableWidgetItem(str(lista[i][2])))
            self.tblDetalle.setItem(i, 3, QtWidgets.QTableWidgetItem(str(lista[i][3])))
            self.tblDetalle.setItem(i, 4, QtWidgets.QTableWidgetItem(str(lista[i][4])))
            self.tblDetalle.setItem(i, 5, QtWidgets.QTableWidgetItem(str(lista[i][5])))
        self.limpiarControles()

    def limpiarControles(self):
        self.txtCodigoProducto.clear()
        self.txtDescripcion.clear()
        self.txtStock.clear()
        self.txtPrecio.clear()
        self.txtCantidad.clear()

    def calcularPago(self):
        self.subTotal_Pagar = 0
        for i in range(len(lista)):
            self.subTotal = lista [i][5]
            self.subTotal_Pagar = self.subTotal_Pagar + float(self.subTotal)
            self.igv = 0.18 * self.subTotal_Pagar
            self.total_pagar = self.subTotal_Pagar + self.igv
        self.txtSubTotal.setText("s/. " + str(round(self.subTotal_Pagar,2)))    
        self.txtIgv.setText("s/. " + str(round(self.igv,2)))
        self.txtTotalPagar.setText("s/. " + str(round(self.total_pagar,2)))