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
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()  # Con getconn recuperamos un objeto de conexion
        log.info(f'Conexion obtenida del pool {conexion}')
        return conexion



if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()  # Conexion uno
    conexion2 = Conexion.obtenerConexion()  # Conexion dos
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    # conexion6 = Conexion.obtenerConexion()  # Podemos ver que al momento de crear una sexta conexion devuelve un error ya que el maximo de conexiones es 6
