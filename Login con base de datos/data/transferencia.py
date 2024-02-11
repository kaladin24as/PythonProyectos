import conexion as con
from model.movimientos import Transferencia
from datetime import datetime

class TransferenciaData():
    
    def __init__(self):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_transferencias = """CREATE TABLE IF NOT EXISTS transferencias 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            monto NUMERIC,
            tipo TEXT,
            documento TEXT,
            motivo TEXT,
            fecha DATETIME)"""
            self.cursor.execute(sql_create_transferencias)
            print("TABLA CREADA CORRECTAMENTE")
        except Exception as ex:
            print("TABLA NO CREADA", ex)
            
    def registrar(self, info: Transferencia):
        fecha = datetime.now()
        try:
            self.cursor.execute("""
                INSERT INTO transferencias (tipo, documento, motivo, monto, fecha)
                VALUES (?, ?, ?, ?, ?)
            """, (info._tipo, info._documento, info._motivo, info._monto, fecha))
            self.db.commit()
            print("Transferencia registrada correctamente")
            return True  # Devuelve True indicando que la transferencia se registró correctamente
        except Exception as ex:
            print("Error al registrar la transferencia:", ex)
            return False  # Devuelve False indicando que hubo un error al registrar la transferencia
        
    def transferencia(self, transferencia: Transferencia):
        try:
            self.cursor.execute("INSERT INTO transferencias (tipo, documento, motivo, monto) VALUES (?, ?, ?, ?)", 
                                (transferencia._tipo, transferencia._documento, transferencia._motivo, transferencia._monto))
            self.db.commit()
            print("Transferencia registrada correctamente")
        except Exception as ex:
            print("Error al registrar la transferencia:", ex)
