from logger_base import log  # Se importa la clase logger_base
import psycopg2 as db  # Se importa libreria de psycopg2 para manejar la db
import sys  # importamos la libreria sys para hacer uso de metodo exit() y asi salga del programa

class Conexion:  # Creacion de clase Conexion
    _DATABASE = 'test_db'  # se crean la variables de clase
    _USERNAME = 'admin'
    _PASSWORD = '1234'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _conexion = None
    _curson = None

    @classmethod
    def obtener_conexion(cls):  # Creamos la clase obtener conexion la cual nos permite crear un objeto tipo conexion, el cual hara la respectiva conexion a la BD
        if cls._conexion is None:  # Validamos si el objeto esta vacio
            try:
                cls._conexion = db.connect(host=cls._HOST,  # Le asignamos al objeto conexion los parametros para realizar la conexion correctamente
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexion exitosa: {cls._conexion}')  # Mandamos a imprimir un mensaje de exito
                return cls._conexion  # Retornamos el objeto conexion
            except Exception as e:
                log.debug(f'Ocurrio una excepcion {e}')  # En caso tal de que algo este mal, se imprime el error
                sys.exit()  # Sale del programa ya que detecto un error