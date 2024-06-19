import logging as log

'''
vamos a usar un handler: es un recurso a donde vamos a mandar esta info, no solo mandamos la info a la consola
sino tambien vamos a configurar un archivo
'''

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',  # Manejando el login en debug, muestra todos los mensajes hacia abajo
                datefmt='%I:%M:%S %p',
                handlers = [
                    log.FileHandler('capa_datos.log'),  # Lo envia a un archivo.log, todos los errores ocasionados
                    log.StreamHandler()
                ])  # Configuracion para manejar los errores o loggin, esto es para un manejo mas profesional

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')  # Si no tiene ninguna configuracion anterior, mostrara desde warning hacia abajo, por default
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critical')


