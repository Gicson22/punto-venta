from PyQt5 import QtWidgets, uic
from Vista.VentanaClientes import VentanaClientes
from Vista.VentanaProductos import VentanaProductos
from Vista.VentanaVentas import VentanaVentas


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/VentanaPrincipal.ui", self)

        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        self.btnClientes.clicked.connect(self.abrirVentanaClientes)
        self.btnVender.clicked.connect(self.abrirVentanaVentas)

    def abrirVentanaProductos(self):
        vProductos = VentanaProductos(self)
        vProductos.show()

    def abrirVentanaClientes(self):
        vClientes = VentanaClientes(self)
        vClientes.show()

    def abrirVentanaVentas(self):
        vVentas = VentanaVentas(self)
        vVentas.show()


        


