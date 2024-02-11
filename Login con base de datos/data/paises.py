import conexion as con
from model.usuario import Usuario

class PaisesData():
        
    def listaCountries(self):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM Countries ORDER BY NAME")
        paises = res.fetchall()
        return paises