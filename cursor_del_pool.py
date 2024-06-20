from conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):  # Se inicializa los atributos conexion y cursor, se le asigna el valor de None
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio metodo with __enter__')  # Este metodo se encarga de obtener una conexion
        self._conexion = Conexion.obtenerConexion()  # le asignamos a nuestro atributo conexion el metodo de obtener conexion
        self._cursor = self._conexion.cursor()  # luego se le asigna a nuestro atributo cursor, el atributo conexion junto a el metodo cursor
        return self._cursor  # Retornamos nuestro cursor creado
