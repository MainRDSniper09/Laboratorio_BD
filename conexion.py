class Conexion:  # Creacion de clase Conexion
    _DATABASE = 'test_db'  # se crean la variables de clase
    _USERNAME = 'admin'
    _PASSWORD = '1234'
    _DB_PORT = '5432'
    _HOST = 'localhost'


    @classmethod
    def obtenerConexion(cls):  # Creamos la clase obtener conexion la cual nos permite crear un objeto tipo conexion, el cual hara la respectiva conexion a la BD
        pass


if __name__ == '__main__':
    pass
