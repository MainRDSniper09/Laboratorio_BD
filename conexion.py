from psycopg2 import pool  # Se importa la clase pool

from logger_base import log


class Conexion:  # Creacion de clase Conexion
    _DATABASE = 'test_db'  # se crean la variables de clase
    _USERNAME = 'admin'
    _PASSWORD = '1234'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1  # Se crea variable minimo de conexiones
    _MAX_CON = 5  # Se crea variable maximo de conexiones
    _pool = None  # Se crea variable pool para que reciba las diferentes conexiones

    @classmethod  # Creamos el metodo de clase obtenerPool
    def obtenerPool(cls):
        if cls._pool is None:  # Preguntamos si no se ha creado un pool
            try:  # Hcemos un try
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      # Usando la libreria de psycopg2 le asignamos a nuestra variable de pool el objeto pool y usamos su metodo simpleConnectionPool para realizar la conexion
                                                      host=cls._HOST, user=cls._USERNAME,
                                                      password=cls._PASSWORD, port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.info(f'Creacion del pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')

    @classmethod
    def obtenerConexion(cls):  # Creamos la clase obtener conexion la cual nos permite crear un objeto tipo conexion, el cual hara la respectiva conexion a la BD
        pass


if __name__ == '__main__':
    pass
