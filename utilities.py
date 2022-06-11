import datetime 

def check_int(x):
    '''
    Devuelve True si es convertible a int\n
    utiliza .isnumeric()
    '''
    return x.isnumeric()

def check_fecha_format(fecha):
    '''
    Devuelve TRUE si es que se puede transformar el valor en 'YYYY-MM-DD'
    '''
    try:
        datetime.datetime.strptime(fecha, '%Y-%m-%d')
        return True #El codigo se va a romper antes si es que no anda
    except ValueError:
        return False
    
        

def check_fecha_disponibilidad(fecha,tipo,lista_torneos):
    '''
    Devuelve TRUE si es que esta disponible la fecha\n
    No esta disponible la fecha si tengo en un mismo dia\n
    un campeonato de la misma clase
    '''
    check = True
    fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d")
    for i in lista_torneos:
        if i.fecha_torneo == fecha and i.tipo_torneo == tipo:
            check = False
    return check


def check_torneo_duplicate(torneo,fecha,lista_torneos):
    '''
    Chequea que solo haya un torneo con ese nombre en ese año.\n
    Devuelve True si todo okay, (NO esta el torneo ya en el sistema\n
    Y si se puede agregar)\n
    Utiliza funcion __eq__() definida en la class
    '''
    fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d")
    check = True
    for i in lista_torneos:
        if i.nombre_torneo == torneo and i.fecha_torneo.year == fecha.year:
            check = False

    return check

def check_jugador_duplicate(jugador,lista_jugadores):
    '''
    Devuelve True si NO estar el jugador ya en el sistema\n

    '''
    check = True
    for i in lista_jugadores:
        if i.cedula == jugador:
            check = False
    
    return check

def check_sponsor_duplicate(sponsor,lista_sponsors):
    '''
    Devuelve True si NO esta el sponsor ya en el sistema\n
    Utiliza funcion __eq__() definida en la class
    '''
    check = True
    for i in lista_sponsors:
        if i.nombre == sponsor:
            check = False

    return check

def check_cedula(cedula): #PARA LA CLASE
    '''
    Devuelve True si cedula tiene el largo de 8 digitos
    Solo funciona con Strings
    '''
    check = False
    if len(cedula) == 8: 
        check = True
    return check

def check_year_format(year):
    '''
    Devuelve True si el año tiene el largo de 4 digitos
    Solo funciona con Strings
    '''
    check = False
    if len(year) == 4: 
        check = True
    return check


def restar_año_datetime(fecha):
    '''
    Dado una fecha (En formato datetime),\n
    devuelve la fecha un año atras
    '''
    #fecha_datetime = datetime.datetime.strptime(fecha,'%Y-%m-%d')
    fecha_datetime = fecha.replace(year = fecha.year-1 )
    return fecha_datetime


def check_ronda(ronda, ronda_max):
    '''
    Dado una ronda(valor ingresado por el usuario), y la ronda maxima \n
    chequea si es el valor estan contenido en esos valores. \n
    Devuelve True si esta bien la ronda ingresada
    '''
    check = False
    if ronda_max == 3:
        for i in [1,2,3]:
            if i == ronda:
                check = True
    elif ronda_max == 4:
        for i in [1,2,3,4]:
            if i == ronda:
                check = True
    
    return check
            
