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

    def __exit__(self, tipo_excepcion, valor_excepcion,
                 detalle_excepcion):  # Se crea el metodo __exit__ para que en caso tal de si es nulo haga rollback y nos arroje un error
        log.debug(f'Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(
                f'Ocurrio una excepcion, se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:  # En caso de exito realice un commit
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()  # Cerramos nuestro cursor para realizar querys
        Conexion.liberarConexion(self._conexion)  # Regresamos nuestra conexion a la pool


if __name__ == '__main__':  # Se crea la prueba
    with CursorDelPool() as cursor:  # Se usa with para usar metodo CursorDelPool y se lo asigna a una variable cursor
        log.debug(f'Dentro del bloque with')  # Se ejecuta un log cuando entra al bloque with
        cursor.execute('SELECT * FROM persona')  # Se ejecuta la sentencia select
        log.debug(cursor.fetchall())  # Recuperamos todos los valores de nuestra tabla
