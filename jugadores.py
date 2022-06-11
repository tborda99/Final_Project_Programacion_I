from datetime import datetime
import datetime

class Jugador:

#CONSTRUCTOR
    def __init__(self, cedula, nombre, pais, fecha_de_nacimiento, sponsor):

        self._cedula = int(cedula)
        self._nombre = nombre
        self._pais = pais
        self._fecha_de_nacimiento = datetime.datetime.strptime(fecha_de_nacimiento, "%Y-%m-%d")
        self._sponsor = sponsor

#GETTERS & SETTERS
    #CEDULA
    @property
    def cedula(self):
        return self._cedula
    
    #NOMBRE
    @property
    def nombre(self):
        return self._nombre

    #PAIS
    @property
    def pais(self):
        return self._pais


    #FECHA DE NACIMIENTO    
    @property
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento


    #SPONSOR
    @property
    def sponsor(self):
        return self._sponsor

   
    def __eq__(self, otro_jugador):
        '''
    Un jugador es IGUAL a otro si, y solo si, su cedula es la misma.
        '''
        return self._cedula == otro_jugador.cedula









