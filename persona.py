class persona:
    def __init__(self, id_persona, nombre, apellido, email):  # Inicializacion de los atributos a recibit
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email

    def __str__(self):  # Creacion metodo __str__ para imprimir los valores
        return f'''
            Id Persona: {self.__id_persona}, Nombre: {self.__nombre}
            Apellido: {self.__apellido}, Email: {self.__email} 
        '''

    # Getters and Setters de cada uno de los atributos
    @property
    def id_persona(self):
        return self.__id_persona

    @id_persona.setter
    def id_persona(self,id_persona):
        self.__id_persona = id_persona

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email = email

if __name__ == '__main__':

