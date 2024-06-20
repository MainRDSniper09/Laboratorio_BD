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

