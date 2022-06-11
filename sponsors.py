class Sponsor():

    def __init__(self, nombre, pago_base, pago_partido):
        
        self._nombre = nombre
        self._pago_base = pago_base
        self._pago_partido = pago_partido
        self._jugadores = []

    
    #GETTERS & SETTERS
    @property
    def nombre(self):
        return self._nombre


    @property
    def pago_base(self):
        return self._pago_base


    @property
    def pago_partido(self):
        return self._pago_partido

    @property
    def jugadores(self):
        return self._jugadores


    def __eq__(self, otro_torneo):
        nombre_1 = self._nombre.lower()
        nombre_2 = otro_torneo.nombre.lower()
        return nombre_1 == nombre_2


