class Transferencia():
    def __init__(self, tipo:str,documento:str,motivo:float,monto:float):
        self._tipo = tipo
        self._documento = documento
        self._motivo = motivo
        self._monto = monto
        
class Deposito:
    def __init__(self, monto, tipo, documento, motivo, fecha, nombre1, nombre2, apellido1, apellido2, sexo, fecha_nacimiento, pais, terminos):
        self._monto = monto
        self._tipo = tipo
        self._documento = documento
        self._motivo = motivo
        self._fecha = fecha
        self._nombre1 = nombre1
        self._nombre2 = nombre2
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._sexo = sexo
        self._fecha_nacimiento = fecha_nacimiento  # Parámetro de fecha de nacimiento
        self._pais = pais
        self._terminos = terminos
