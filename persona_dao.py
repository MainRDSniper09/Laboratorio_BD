from cursor_del_pool import CursorDelPool
from logger_base import log
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
        with CursorDelPool() as cursor:  # Usamos el objeto cursor del pool creada anteriormente para simplificar nuestro codigo
            cursor.execute(cls._SELECCIONAR)  # Usamos el metodo de ejecutar y dentro le pasamos el parametro de cls._SELECCIONAR, el cual tiene la sentencia sql
            registros = cursor.fetchall()  # Decimos que recupere todos los elementos de nuestro registro
            personas = []  # Creamos una lista para agregar nuestros registros
            for registro in registros:  # Usamos un for para iterar los registros obtenidos anteriormente
                persona = Persona(registro[0], registro[1], registro[2], registro[3])  # Creamos un objeto persona y lo volvemos una lista el cual contrenda los registros y los asignara a su respectivo indice siendo el indice[0] el nombre y asi sucesivamente
                personas.append(persona) # usamos la operacion de anexar los registros a la lista a una variable llamada personas la cual es una lista
            return personas  # Pedimos que nos retorne esta lista de personas

    @classmethod  # Creamos el metodo insertar en un metodo de clase
    def insertar(cls, persona):  # Recibimos como parametro el objeto persona
        with CursorDelPool() as cursor:  # Se usa metodo del pool para crear el objeto cursor
            log.debug(
                f'Persona a insertar: {persona}')  # Mandamos un mensaje por consola la persona que se va a insertar
            valores = (persona.nombre, persona.apellido,
                       persona.email)  # Creamos la tupla en donde pasamos los valores del objeto persona, con sus respectivos atributos
            cursor.execute(cls._INSERTAR,
                           valores)  # Hacemos uso de execute para que ejecute la sentencia SQL y le pasamos la tupla de valores
            log.debug(
                f'Persona insertada correctamente: {persona}')  # Mandamos un mensaje por consola mostrando que la persona ha sido insertada correctamente
            return cursor.rowcount  # Retornamos la cantidad de personas insertadas a nuestra tabla

    @classmethod  # Creamos el metodo de clase actualizar
    def actualizar(cls, persona):  # Como parametro tambien recibimos el objeto persona
        with CursorDelPool() as cursor:  # Se usa metodo del pool para crear el objeto cursor
                valores = (persona.nombre,persona.apellido,persona.email, persona.id_persona)  # Creamos la tupla de valores ya que se tiene que proporcionar los valores de cada uno de los atributos incluyendo id_persona ya que tenemos que especificar que id es el que vamos a modificar
                cursor.execute(cls._ACTUALIZAR, valores)  # Hacemos uso de execute para ejecutar el comando SQL y le pasamos la tupla
                log.debug(f'Persona actualizada: {persona}')  # Mandamos mensaje por consola indicando que persona se va a modificar
                return cursor.rowcount  # Retornamos la cantidad de registros modificados

    @classmethod  # Se crea el metodo de clase eliminar
    def eliminar(cls,persona):  # En donde nuevamente recibe como parametro el objeto persona
        with CursorDelPool() as cursor:  # Se usa metodo del pool para crear el objeto cursor
                valores = (persona.id_persona,)  # Creamos la tupla de valores en donde solo recibimos de parametro id_persona para poder eliminarla
                cursor.execute(cls._ELIMINAR, valores)  # Hacemos que ejecute el comando SQL y mandamos la tupla
                log.debug(f'Objeto eliminado: {persona}')  # Creamos el mensaje por consola para que el usuario vea que registro se esta eliminando
                return cursor.rowcount  # Retornamos la cantidad de registros eliminados

if __name__ == '__main__':  # Creamos una prueba y vemos que funcione correctamente
        # Insertar un registro
        # persona1 = Persona(nombre='Jorge',apellido='Vega',email='jv@email.com')  # Se crea el objeto persona1 en donde recibe los parametros para poder insertarla en la tabla
        # personas_insertadas = PersonaDAO.insertar(persona1)  # Creamos la variable personas_insertadas para asignarle el metodo insertar y de parametro le pasamos persona1
        # log.debug(f'Personas insertadas: {personas_insertadas}')  # Finalmente mandamos mensaje por consola mostrando la persona insertada

        # Actualizar un registro
        # persona1 = Persona(16,'Jorge','Eliecer','Je@email.com')
        # personas_actualizadas = PersonaDAO.actualizar(persona1)
        # log.debug(f'Personas actualizadas: {personas_actualizadas}')

        # Eliminar registro
        # persona1 = Persona(id_persona=12)
        # personas_eliminadas = PersonaDAO.eliminar(persona1)
        # log.debug(f'Personas eliminadas {personas_eliminadas}')

        # Seleccionar objetos
        personas = PersonaDAO.seleccionar()  # Creamos el objeto PersonaDAO y mandamos a llamar el metodo seleccionar
        for persona in personas:  # Creamos un for para que itere cada registro dentro de nuestra tabla
            log.debug(persona)  # Imprimimos con un log.debug
