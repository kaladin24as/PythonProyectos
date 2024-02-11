import conexion as con
from model.movimientos import Deposito
from datetime import datetime

class DepositoData():
    
    def __init__(self):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_depositos = """CREATE TABLE IF NOT EXISTS depositos 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                monto NUMERIC,
                tipo TEXT,
                documento TEXT,
                motivo TEXT,
                fecha DATETIME,
                nombre1 TEXT,
                nombre2 TEXT,
                apellido1 TEXT,
                apellido2 TEXT,
                sexo TEXT,
                fecha_nacimiento DATETIME,
                pais TEXT,
                terminos BOOLEAN
                )"""
            self.cursor.execute(sql_create_depositos)
            print("TABLA CREADA CORRECTAMENTE")
        except Exception as ex:
            print("TABLA NO CREADA", ex)
            
    def registrar(self, info: Deposito):
        fecha = datetime.now()
        try:
            self.cursor.execute("""
                INSERT INTO depositos (monto, tipo, documento, motivo, fecha, nombre1, nombre2, apellido1, apellido2, sexo, fecha_nacimiento, pais, terminos)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (info._monto, info._tipo, info._documento, info._motivo, fecha, info._nombre1, info._nombre2, info._apellido1, info._apellido2, info._sexo, info._fecha_nacimiento, info._pais, info._terminos))
            self.db.commit()
            print("Depósito registrado correctamente")
            return True  # Devuelve True indicando que el depósito se registró correctamente
        except Exception as ex:
            print("Error al registrar el depósito:", ex)
            return False  # Devuelve False indicando que hubo un error al registrar el depósito
