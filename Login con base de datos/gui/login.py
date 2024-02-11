from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox

from data.usuario import UsuarioData
from gui.main import MainWindow
from model.usuario import Usuario

class Login():
    def __init__(self):
        self.login = uic.loadUi("gui/banco3.ui")
        self.initGUI()
        self.login.lblMensaje.setText("")
        self.login.show()
    
    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2: 
            self.login.lblMensaje.setText("Ingresa un usuario valido")
        elif len(self.login.txtPassword.text()) < 3:
            self.login.lblMensaje.setText("Ingresa una clave valida") 
        else:
            self.login.lblMensaje.setText("")
            usu = Usuario(usuario=self.login.txtUsuario.text(),clave=self.login.txtPassword.text())
            usuData = UsuarioData()
            res=usuData.login(usu)
            if res:
                self.main = MainWindow()
                self.login.hide()
            else:
                self.login.lblMensaje.setText("Login incorrecto")
                

    def registrar_usuario(self):
        if len(self.login.txtUsuario.text()) < 2: 
            self.login.lblMensaje.setText("Ingresa un usuario válido")
        elif len(self.login.txtPassword.text()) < 3:
            self.login.lblMensaje.setText("Ingresa una clave válida") 
        else:
            self.login.lblMensaje.setText("")
            usu = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtPassword.text())
            usuData = UsuarioData()
            if usuData.registrar(usu):
                self.login.lblMensaje.setText("Usuario registrado correctamente")
            else:
                self.login.lblMensaje.setText("Error al registrar el usuario")


    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)
        self.login.btnRegistrarUsuario.clicked.connect(self.registrar_usuario)
