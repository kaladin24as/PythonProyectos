from PyQt6 import uic, QtWidgets  # Corregida la importación de QMessageBox
from PyQt6.QtWidgets import QMessageBox
from data.deposito import DepositoData
from data.paises import PaisesData
from data.transferencia import TransferenciaData
from datetime import datetime
from gui.registro import RegistroWindow
from model.movimientos import Deposito, Transferencia


class MainWindow():
    def __init__(self):
        self.main = uic.loadUi("gui/main.ui")
        self.initGUI()
        self.main.showMaximized()
    
    def initGUI(self):
# Suponiendo que `btnRegistrarTransferencias` es un QAction
        self.main.btnRegistrarTransferencias.triggered.connect(self.abrirRegistro)
        self.main.btnReportarTransferencias.triggered.connect(self.abrirDeposito)
        self.registro = uic.loadUi("gui/registro.ui")
        self.deposito = uic.loadUi("gui/deposito.ui")
        
    def abrirRegistro(self):
        self.registro.btnRegistrarTransferenciaRegistro.clicked.connect(self.registrarTransaccion)
        self.registro.show()


    def registrarTransaccion(self):
        if self.registro.tipodedocumento.currentText() == "Tipo de documento":
            mBox = QMessageBox()
            mBox.setText("Por favor seleccione el tipo de documento")
            mBox.exec()
            self.registro.tipodedocumento.setFocus()
        elif len(self.registro.txtNumeroDeDocumento.text()) < 4:
            mBox = QMessageBox()
            mBox.setText("Por favor ingrese un numero de documento")
            mBox.exec()
            self.registro.txtNumeroDeDocumento.setFocus()   
        elif self.registro.motivodelgiro.currentText() == "Motivo del giro":
            mBox = QMessageBox()
            mBox.setText("Por favor seleccione el motivo del giro")
            mBox.exec()
            self.registro.motivodelgiro.setFocus()
        elif not self.registro.txtMonto.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText("Por favor ingrese un monto valido")
            mBox.exec()
            self.registro.txtMonto.setFocus()
            
        else:
            transferencia = Transferencia(
                tipo=self.registro.tipodedocumento.currentText(),
                documento=self.registro.txtNumeroDeDocumento.text(),
                motivo=self.registro.motivodelgiro.currentText(),
                monto=self.registro.txtMonto.text()
            )
            objData = TransferenciaData()
            if objData.registrar(info=transferencia):
                mBox = QMessageBox()
                mBox = QMessageBox()
                mBox.setText("Transferencia registrada correctamente")
                mBox.exec()
                self.limpiarCamposTransferencia()
                self.registro.close()
            else:
                mBox = QMessageBox()
                mBox.setText("Error al registrar la transferencia")
                mBox.exec()
    def limpiarCamposTransferencia(self):
        self.registro.tipodedocumento.setCurrentText("Tipo de documento")
        self.registro.txtNumeroDeDocumento.setText("")
        self.registro.motivodelgiro.setCurrentText("Motivo del giro")
        self.registro.txtMonto.setText("")
        
    
    def abrirDeposito(self):
        self.deposito.show()
        self.llenarComboPais()
        self.deposito.btnRegistrarTransferenciaRegistro.clicked.connect(self.registrarDeposito)

        
    def llenarComboPais(self):
        objData = PaisesData()
        datos = objData.listaCountries()
        for dato in datos:
            self.deposito.cbLugar.addItem(dato[1])
            
    def validarCamposObligatorios(self):
        mBox = QMessageBox()
        if (self.deposito.tipodedocumento.currentText()=="Tipo de documento" or
            not self.deposito.txtNumeroDeDocumento.text() or
            not self.deposito.txtPrimerNombre.text() or
            not self.deposito.txtPrimerApellido.text() or
            self.deposito.motivodelgiro.currentText()=="Motivo del giro" or
            not self.deposito.txtMonto.text() or
            self.deposito.cbLugar.currentText() == "Seleccione una opcion" or
            not self.deposito.txtFecha.text() or 
            self.deposito.txtSexo.currentText() == "Sexo"):
            return False
        else:
            return True
        
    def registrarDeposito(self):
        mBox = QMessageBox()
        if not self.validarCamposObligatorios():
            mBox.setText("Por favor llene todos los campos")
            mBox.exec()
        elif not self.deposito.checkTerminos.isChecked():
            mBox.setText("Por favor acepte los términos")
            mBox.exec()
        elif not self.deposito.txtMonto.text().isnumeric() or float(self.deposito.txtMonto.text()) < 0:
            mBox.setText("Por favor ingrese un monto valido")
            self.deposito.txtMonto.setText("0")
            mBox.exec()
            self.deposito.txtMonto.setFocus()
        else:
            fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            deposito = Deposito(
                monto=float(self.deposito.txtMonto.text()),
                tipo=self.deposito.tipodedocumento.currentText(),
                documento=self.deposito.txtNumeroDeDocumento.text(),
                motivo=self.deposito.motivodelgiro.currentText(),
                fecha=fecha_actual,
                nombre1=self.deposito.txtPrimerNombre.text(),
                nombre2=self.deposito.txtSegundoNombre.text(),
                apellido1=self.deposito.txtPrimerApellido.text(),
                apellido2=self.deposito.txtSegundoApellido.text(),
                sexo=self.deposito.txtSexo.currentText(),
                fecha_nacimiento=self.deposito.txtFecha.text(),  # Corregido a fecha_nacimiento
                pais=self.deposito.cbLugar.currentText(),
                terminos=self.deposito.checkTerminos.isChecked()
            )
            
            objData = DepositoData()
            if objData.registrar(info=deposito):
                mBox.setText("Depósito registrado correctamente")
                mBox.exec()
            else:
                mBox.setText("Error al registrar el depósito")
                mBox.exec()
            
