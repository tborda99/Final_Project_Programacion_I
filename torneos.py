from abc import ABC
import datetime


class Torneo(ABC):

    def __init__ (self,fecha_torneo,nombre_torneo,jugadores):

        self._fecha_torneo = datetime.datetime.strptime(fecha_torneo, "%Y-%m-%d")   
        self._nombre_torneo = nombre_torneo
        self._jugadores = jugadores #dictionary
        

    #GETTERS & SETTERS

    #NOMBRE
    @property
    def nombre_torneo(self):
        return self._nombre_torneo

    #TIPO DE TORNEO
    @property
    def tipo_torneo(self):
        return self._tipo_torneo


    #FECHA DE TORNEO
    @property
    def fecha_torneo(self):
        return self._fecha_torneo


    #JUGADORES
    @property
    def jugadores(self):
        return self._jugadores


    def __eq__(self, otro_torneo):
        return self._nombre_torneo.lower() == otro_torneo.nombre_torneo.lower()

    
    #AGREGAR JUGADOR (FUNCIONES QUE NO SE USAN EN EL CODIGO PERO SIRVEN PARA PRUEBAS)
    #def agregar_jugador(self,jugador): 
        if len(self._jugadores) < self._numero_jugadores:
            self._jugadores.append(jugador)
        else:
            print('ERROR: campeonato ya esta completo')
    
    #ELIMINAR JUGADOR
    #def eliminar_jugador(self, jugador, lista_jugadores):
        existe = False
        for i in lista_jugadores:
            if i == jugador:
                existe = True

        if existe == True:
            lista_jugadores.remove(jugador)
        else:
            print('No se pudo borrar jugador')
    

    #DEVOLVER EL AñO 
    def get_año(self):
        '''
        Dado una torneo, devuelve su año
        '''
        #datem = datetime.datetime.strptime(self._fecha_torneo, "%Y-%m-%d")
        return self._fecha_torneo.year
    
    #DEVOLVER PUNTOS
    def get_puntos(self, jugador):
        '''
        Dado un jugador devuelve su puntos en el campeonato
        '''
        #self._jugadores ==> {1:5143402}

        esta_en_campeonato = False
        for jugadores in list(self._jugadores):
            if jugadores == jugador:
                esta_en_campeonato = True
        
        if esta_en_campeonato == True:
            puesto = self._jugadores.get(jugador)
            return self._puntos.get(puesto)
        
        else:
            return 0
    
    #DEVOLVER EL PUESTO
    def get_puesto(self, jugador):
        '''
        Dado un jugador, devuelve su puesto en el campeonato
        '''
        esta_en_campeonato = False
        for jugadores in list(self._jugadores):
            if jugadores == jugador:
                esta_en_campeonato = True
        
        if esta_en_campeonato == True:
            return self._jugadores.get(jugador)
        
        else:
            return 0

        
    
#INHERITANCE
class Torneo250(Torneo):

    def __init__(self, fecha_torneo,nombre_torneo,jugadores):
        super().__init__(fecha_torneo,nombre_torneo,jugadores)
        self._tipo_torneo = 250
        self._numero_jugadores = 4
        self._puntos = {1:250, 2:125, 3:0} #DICCIONARIO DE CORRESPONDENCIA

    
        #GETTERS (No agrego setters porque estos no se editan)
    @property
    def numero_jugadores(self):
        return self._numero_jugadores

    @property
    def puntos(self):
        return self._numero_jugadores
    
    @property
    def tipo_torneo(self):
        return self._tipo_torneo


class Torneo500(Torneo):

    def __init__(self, fecha_torneo,nombre_torneo,jugadores):
        super().__init__(fecha_torneo,nombre_torneo,jugadores)
        self._tipo_torneo = 500
        self._numero_jugadores = 4
        self._puntos = {1:500, 2:250, 3:0} #DICCIONARIO DE CORRESPONDENCIA
    
        #GETTERS (No agrego setters porque estos no se editan)
    @property
    def numero_jugadores(self):
        return self._numero_jugadores

    @property
    def puntos(self):
        return self._numero_jugadores
    
    @property
    def tipo_torneo(self):
        return self._tipo_torneo
    

class Torneo1000(Torneo):

    def __init__(self, fecha_torneo,nombre_torneo,jugadores):
        super().__init__(fecha_torneo,nombre_torneo,jugadores)
        self._tipo_torneo = 1000
        self._numero_jugadores = 8
        self._puntos = {1:1000, 2:500, 3:250, 4:0} #DICCIONARIO DE CORRESPONDENCIA
    
        #GETTERS (No agrego setters porque estos no se editan)
    @property
    def numero_jugadores(self):
        return self._numero_jugadores

    @property
    def puntos(self):
        return self._numero_jugadores
    
    @property
    def tipo_torneo(self):
        return self._tipo_torneo



    