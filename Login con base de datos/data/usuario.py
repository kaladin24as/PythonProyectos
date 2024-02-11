import conexion as con
from model.usuario import Usuario

class UsuarioData():
    
    def __init__(self):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            # Verificar si ya existe un usuario 'Admin'
            res = self.cursor.execute("SELECT * FROM usuarios WHERE usuario = 'Admin'")
            if res.fetchone() is None:
                # Si no existe, crearlo
                sql_insert = """INSERT INTO usuarios (usuario, clave) VALUES (?, ?)"""
                usuario_admin = ('Admin', 'Admin')
                self.cursor.execute(sql_insert, usuario_admin)
                self.db.commit()
                print("Usuario 'Admin' creado correctamente")
            else:
                print("El usuario 'Admin' ya existe en la base de datos.")
        except Exception as ex:
            print("Error al intentar crear el usuario admin:", ex)

            
            
    def login(self, usuario: Usuario):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            res = self.cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND clave = ?", 
                                      (usuario._usuario, usuario._clave))
            fila = res.fetchone()
            if fila is not None:
                usuario = Usuario(nombre=fila[1], usuario=fila[2])
                return usuario
            else:
                return None
        except Exception as ex:
            print("Error al intentar iniciar sesión:", ex)
            return None

    def registrar(self, usuario: Usuario):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            # Verificar si el nombre de usuario ya existe
            res = self.cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario._usuario,))
            if res.fetchone() is not None:
                print("El nombre de usuario '{}' ya está en uso.".format(usuario._usuario))
                return False
            else:
                # Insertar el nuevo usuario
                sql_insert = "INSERT INTO usuarios (usuario, clave) VALUES (?, ?)"
                self.cursor.execute(sql_insert, (usuario._usuario, usuario._clave))
                self.db.commit()
                print("Usuario registrado correctamente")
                return True
        except Exception as ex:
            print("Error al registrar el usuario:", ex)
            return False
