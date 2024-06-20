from conexion import Conexion
from persona import Persona


class PersonaDAO:  # Se crea la el patron de diseño dao, para la conexion de bases de datos
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''

    # Se crean las variables de entorno en donde especificacmos las acciones que puede realizar el usuario
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod  # Creamos el metodo seleccionar en un metodo de clase
    def seleccionar(cls):
        with Conexion.obtener_cursor() as cursor:  # Hacemos uso del with para no tener que hacer commits y rollback manuales
            cursor.execute(cls._SELECCIONAR)  # Usamos el metodo de ejecutar y dentro le pasamos el parametro de cls._SELECCIONAR, el cual tiene la sentencia sql
            registros = cursor.fetchall()  # Decimos que recupere todos los elementos de nuestro registro
            personas = []  # Creamos una lista para agregar nuestros registros
            for registro in registros:  # Usamos un for para iterar los registros obtenidos anteriormente
                persona = Persona(registro[0], registro[1], registro[2], registro[3])  # Creamos un objeto persona y lo volvemos una lista el cual contrenda los registros y los asignara a su respectivo indice siendo el indice[0] el nombre y asi sucesivamente
                personas.append(persona) # usamos la operacion de anexar los registros a la lista a una variable llamada personas la cual es una lista
            return personas  # Pedimos que nos retorne esta lista de personas