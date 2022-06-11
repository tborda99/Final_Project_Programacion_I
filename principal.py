from jugadores import Jugador
from sponsors import Sponsor
from torneos import Torneo250, Torneo500, Torneo1000
from utilities import (check_fecha_format,
                       check_int, check_jugador_duplicate,
                       check_sponsor_duplicate, check_torneo_duplicate,
                       restar_año_datetime,check_cedula,check_ronda,
                       check_fecha_disponibilidad,check_year_format)
import datetime
import operator



def iniciar_listas(): #OKAY
    lista_sponsors = []
    lista_jugadores = []
    lista_torneos = []

    return lista_sponsors,lista_jugadores,lista_torneos


def menu_principal(lista_sponsors,lista_jugadores,lista_torneos): #OKAY
    print(" ")
    opcion = input('Menú principal\n \nSeleccione la opción del menú:\n \n1. Alta de sponsor\n2. Alta de jugador\n3. Alta de torneo\n4. Realizar consultas\n5. Finalizar programa\n')
    if check_int(opcion) == True:
        opcion = int(opcion)
        if opcion == 1:
            menu_sponsor(lista_sponsors,lista_jugadores,lista_torneos)
        elif opcion == 2:
            menu_jugador(lista_sponsors,lista_jugadores,lista_torneos)
        elif opcion == 3: 
            menu_torneo_1(lista_sponsors,lista_jugadores,lista_torneos)
        elif opcion == 4:
            menu_consultas_principal(lista_sponsors,lista_jugadores,lista_torneos)
        elif opcion == 5:
            exit()
        else:
            print('ERROR: Por favor intente denuvevo')
            menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
    else:
        print('ERROR: Ingrese un numero, no un caracter')
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)


def menu_sponsor(lista_sponsors,lista_jugadores,lista_torneos): #OKAY
    print(" ")
    nombre_sponsor = input('Alta de sponsor:\n \nIngrese nombre: ')
    sponsor_dup = check_sponsor_duplicate(nombre_sponsor,lista_sponsors)
    if sponsor_dup == True:
        pago_base = input('Ingrese pago base por torneo: ')
        
        if check_int(pago_base) == True:
            pago_base = int(pago_base)

            pago_partido = input('Ingrese premio por partido jugado: ')
            if check_int(pago_partido) == True:
                pago_partido = int(pago_partido)
                
                if pago_base > 0 and pago_partido > 0:
                    
                    lista_sponsors.append(Sponsor(nombre_sponsor,pago_base,pago_partido))
                    
                    menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
                        
                else:
                    print("Error: Los pagos deben ser mayores que 0")
                    menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
        
            else:
                print('ERROR: Pago partido tiene que ser un número')
                menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
        else:
            print('ERROR: Pago base tiene que ser un número')
            menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
    
    else:
        print("Error: Sponsor ya esta en el sistema")
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)


def menu_jugador(lista_sponsors,lista_jugadores,lista_torneos): #OKAY 
    print(" ")
    cedula = input('Alta de jugador:\n \nIngrese cédula: ')
    check_cedula_int = check_int(cedula)
    check_cedula_formato = check_cedula(cedula)

    if check_cedula_int == True and check_cedula_formato == True:
        cedula = int(cedula)
        jugador_dup = check_jugador_duplicate(cedula,lista_jugadores) #True si no esta en el sistema (Valor buscado TRUE)
        if jugador_dup == True:
            nombre = input('Ingrese nombre: ')
            pais = input('Ingrese país de nacimiento: ')
            fecha_de_nacimiento = input('Ingrese fecha de nacimiento: ')
            check_fecha = check_fecha_format(fecha_de_nacimiento)
            if check_fecha == True:
                nombre_sponsor = input('Ingrese nombre de sponsor: ')
                sponsor_dup = check_sponsor_duplicate(nombre_sponsor,lista_sponsors) #True si no esta en el sistema (Valor buscado FALSE)
                if sponsor_dup == False:
                    #Agrego el jugador a la lista de jugadores
                    lista_jugadores.append(Jugador(cedula,nombre,pais,fecha_de_nacimiento, nombre_sponsor))

                    #Agrego al jugador a su sponsor
                    for i in lista_sponsors:
                        if i.nombre == nombre_sponsor:
                            i.jugadores.append(cedula)
                    menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
                
                else:
                    print(f'ERROR El sponsor {nombre_sponsor} no esta registado:\n Visite el menu de Alta de sponsor e intente nuevamente')
                    menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
                

            else:
                print('ERROR: Fecha en formato incorrecto')
                menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

        else:
            print(f'ERROR: El jugador de cedula {cedula} ya esta en el sistema')
            menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

    else:
        print('ERROR: Ingrese correctamente la cedula')
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
    

def menu_torneo_1(lista_sponsors,lista_jugadores,lista_torneos): #OKAY
    print(" ")
 
    fecha_torneo = input('Alta de torneo:\n \nIngrese fecha del toreno: ')
    if check_fecha_format(fecha_torneo) == True:
        nombre_torneo = input('Ingrese nombre del toreno: ')
        menu_torneo_2(lista_sponsors,lista_jugadores,lista_torneos,fecha_torneo,nombre_torneo)
        
        
    else:
        print('ERROR: Fecha en formato incorrecto')
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
        

def menu_torneo_2(lista_sponsors,lista_jugadores,lista_torneos,fecha, nombre): # OKAY
    tipo_torneo = input('Seleccione el tipo de torneo a ser creado:\n 1.ATP250\n 2.ATP500\n 3.ATPMASTERS1000\n')

    if check_int(tipo_torneo) == True:
        tipo_torneo = int(tipo_torneo)
        if tipo_torneo == 1:
            if check_torneo_duplicate(nombre,fecha,lista_torneos) == True: 

                if check_fecha_disponibilidad(fecha,250,lista_torneos) == True:
                    menu_250(lista_sponsors,lista_jugadores,lista_torneos,fecha,nombre)

                else:
                    print(f'ERROR: Ya existe un torneo del tipo ATP250 para la fecha {fecha}')
                    menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

            else:
                print(f'ERROR: El torneo {nombre}, ya esta ingresado en ese año')
                menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
                
        elif tipo_torneo == 2:
            if check_torneo_duplicate(nombre,fecha,lista_torneos)== True:

                if check_fecha_disponibilidad(fecha,500,lista_torneos) == True:
                    menu_500(lista_sponsors,lista_jugadores,lista_torneos,fecha,nombre)
                else:
                    print(f'ERROR: Ya existe un torneo del tipo ATP500 para la fecha {fecha}')
                    menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
            
            else:
                print(f'ERROR: El torneo {nombre}, ya esta ingresado en ese año')
                menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
            
        elif tipo_torneo == 3:
            if check_torneo_duplicate(nombre,fecha,lista_torneos)== True:

                if check_fecha_disponibilidad(fecha,1000,lista_torneos) == True:
                    menu_1000(lista_sponsors,lista_jugadores,lista_torneos,fecha,nombre)

                else:
                    print(f'ERROR: Ya existe un torneo del tipo ATP1000 para la fecha {fecha}')
                    menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
            
            else:
                print(f'ERROR: El torneo {nombre}, ya esta ingresado en ese año')
                menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
        
        else:
            print('ERROR: Ingrese un numero valido')
            menu_principal(lista_sponsors,lista_jugadores,lista_torneos,fecha, nombre)

    else:
        print('ERROR: Ingrese un numero, no un caracter')
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)


def menu_250(lista_sponsors,lista_jugadores,lista_torneos,fecha, nombre): #OKAY 
    print(' ')
    jugadores = {} 
    broke = False
    for i in range(4):
        cedula =input('Ingrese jugadores que participaron:\nIngrese Cedula:')
        if check_cedula(cedula) == True and check_int(cedula):
            cedula = int(cedula)
            ronda_max = input('Ingrese ronda máxima alcanzada:\n 1. Campeon \n 2. Final \n 3. Semifinal \n')
            if check_int(ronda_max) == True: 
                ronda_max = int(ronda_max)

                if check_ronda(ronda_max,3) == True:
                    jugadores.update({cedula:ronda_max})

                else:
                    print('ERROR: Ronda maxima tiene que ser uno de los valores especificados')
                    broke = True
                    break
            else:
                print('ERROR: Ronda maxima tiene que ser un numero')
                broke = True
                break

        else:
            print('ERROR: Cedula en formato incorrecto')
            broke = True
            break
    
    if broke == False:
        lista_torneos.append(Torneo250(fecha,nombre,jugadores))
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

    else:
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
        

def menu_500(lista_sponsors,lista_jugadores,lista_torneos,fecha, nombre): #OKAY
    print(' ')
    jugadores = {} 
    broke = False
    for i in range(4):
        cedula =input('Ingrese jugadores que participaron:\nIngrese Cedula:')
        if check_cedula(cedula) == True and check_int(cedula):
            cedula = int(cedula)
            ronda_max = input('Ingrese ronda máxima alcanzada:\n 1. Campeon \n 2. Final \n 3. Semifinal \n')
            if check_int(ronda_max) == True: 
                ronda_max = int(ronda_max)

                if check_ronda(ronda_max,3) == True:
                    jugadores.update({cedula:ronda_max})

                else:
                    print('ERROR: Ronda maxima tiene que ser uno de los valores especificados')
                    broke = True
                    break
            else:
                print('ERROR: Ronda maxima tiene que ser un numero')
                broke = True
                break

        else:
            print('ERROR: Cedula en formato incorrecto')
            broke = True
            break
    
    if broke == False:
        lista_torneos.append(Torneo500(fecha,nombre,jugadores))
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

    else:
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)


def menu_1000(lista_sponsors,lista_jugadores,lista_torneos,fecha, nombre): #OKAY
    print(' ')    
    jugadores = {} 
    broke = False
    for i in range(8):
        cedula =input('Ingrese jugadores que participaron:\nIngrese Cedula:')
        if check_cedula(cedula) == True and check_int(cedula):
            cedula = int(cedula)
            ronda_max = input('Ingrese ronda máxima alcanzada:\n 1. Campeon \n 2. Final \n 3. Semifinal \n 4. Cuartos de final\n')
            if check_int(ronda_max) == True:
                ronda_max = int(ronda_max)
                if check_ronda(ronda_max,4) == True:
                    jugadores.update({cedula:ronda_max})
                else:
                    print('ERROR: Ronda max tiene que ser uno de los valores especificados')
                    broke = True
                    break
            else:
                print('ERROR: Ronda maxima tiene que ser un numero')
                broke = True
                break

        else:
            print('ERROR: Cedula en formato incorrecto')
            broke = True
            break
    
    if broke == False:
        lista_torneos.append(Torneo1000(fecha,nombre,jugadores))
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

    else:
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

    
def menu_consultas_principal(lista_sponsors,lista_jugadores,lista_torneos): #OKAY
    tipo_consulta = input('Realizar consultas:\n \n1.Determine torneos jugados en un año especifico para un jugador\n2.Top 5 de jugadores con mayor puntaje para la fecha ingresada.\n3.Top 5 de torneos ganados por país\n4.Dinero recaudado por un jugador en un periodo de tiempo gracias al sponsor\n')
    
    if check_int(tipo_consulta): 
        tipo_consulta =int(tipo_consulta)

        if tipo_consulta == 1:
            menu_consultas_1(lista_sponsors,lista_jugadores,lista_torneos)

        elif tipo_consulta == 2:
            menu_consultas_2(lista_sponsors,lista_jugadores,lista_torneos)

        elif tipo_consulta == 3:
            menu_consultas_3(lista_sponsors,lista_jugadores,lista_torneos)

        elif tipo_consulta == 4:
            menu_consultas_4(lista_sponsors,lista_jugadores,lista_torneos)

        else:
            print('ERROR: Ingrese un numero valido')
            menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

    else:
        print('ERROR: Ingrese un numero')
        menu_consultas_principal(lista_sponsors,lista_jugadores,lista_torneos)


def menu_consultas_1(lista_sponsors,lista_jugadores,lista_torneos): #OKAY
    fecha = input('1.Determine torneos jugados en un año especifico para un jugador.\nIngrese fecha en formato YYYY: ')
    if check_int(fecha) == True and check_year_format(fecha) == True:
        fecha = int(fecha)
        cedula = input('Ingrese cédula del jugador: ')
        if check_cedula(cedula) == True and check_int(cedula):
            cedula = int(cedula)
            if check_jugador_duplicate(cedula,lista_jugadores) == False:

                count = 0
                for torneo in lista_torneos:
                    if torneo.get_año() == fecha:
                        for jugador in torneo.jugadores:
                            if jugador == cedula:
                                count += 1

                print(f'\nEl número de torneos jugados es de: {count}')
                menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

            else:
                print(f'Jugador {cedula} no esta en el sistema')
                menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

        else:
            print('ERROR: Ingrese la cedula en formato correcto')
            menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
    
    else:
        print('ERROR: Ingrese la fecha en formato correcto')
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
   

def menu_consultas_2(lista_sponsors,lista_jugadores,lista_torneos): #OKAY
    top = {} #Key = cedula, value = puntos
    top.clear()
    
    fecha = input('\nTop 5 de jugadores con mayor puntaje para la fecha ingresada:\n \nIngrese fecha en formato: YYYY-MM-dd: ')

    if check_fecha_format(fecha) == True:
        fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d")
        
        for torneo in lista_torneos:

            if fecha.year >= torneo.get_año() and torneo.get_año() >= restar_año_datetime(fecha).year:
                for jugador in torneo.jugadores: #ITERO POR EL DICTIONARY, python automaticamente itera por las keys
                    
                    esta_en_top = False       
                    for jugadores in list(top):   # CHEQUEO SI YA ESTA LA KEY(CEDULA) O NO
                        if jugadores == jugador:
                            esta_en_top = True
                    
                    if esta_en_top == True:
                        top[jugador] = top[jugador] + torneo.get_puntos(jugador)
                        
                        
                    else: #Agregar jugador al diccionario
                        nuevo_dic = {jugador:torneo.get_puntos(jugador)}
                        top.update(nuevo_dic)
        
        #Elimino punto duplicados de mismo torneo dos veces 
        for torneo_1 in lista_torneos:
            for torneo_2 in lista_torneos:
                if torneo_1.nombre_torneo == torneo_2.nombre_torneo and torneo_1.get_año() > torneo_2.get_año():
                    for jugadores in list(top):
                        top[jugador] = top[jugador] - torneo_2.get_puntos(jugador)

                elif torneo_1.nombre_torneo == torneo_2.nombre_torneo and torneo_1.get_año() < torneo_2.get_año():
                    for jugadores in list(top):
                        top[jugador] = top[jugador] - torneo_1.get_puntos(jugador)
        
        
        #ORDENO EL DICCIONARIO DE MAYOR A MENOR 
        top_sorted ={}
        top_sorted.clear()
        top_sorted = dict( sorted(top.items(), key=operator.itemgetter(1),reverse=True))
        dict_items = top_sorted.items()
        top_5 ={}
        top_5.clear()
        top_5 = list(dict_items)[:5]


        #GET NOMBRES
        
        nombres = []
        for cedula,valor in top_5:
            for jugador in lista_jugadores:
                if jugador.cedula == cedula:
                    nombres.append(jugador.nombre)

        
        if bool(top_5) == True: #si vacio devuelven False
            i = 0
            for key, value in top_5:
                print(f'Cedula: {key}, Nombre: {nombres[i]}, Puntos: {value}')
                i += 1
        
        elif bool(top_5) == False:
            print('No hay campeonatos para ese periodo')

        
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
 
    else: 
        print('ERROR: Fecha en formato incorrecto\n ¡ Debe ingresar YYYY-MM-DD !')
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)


def menu_consultas_3(lista_sponsors,lista_jugadores,lista_torneos): #OKAY
    
    #No se necesita input
    #Agarrar todos los paises inscriptos
    lista_paises = []
    for jugador in lista_jugadores:
        if jugador.pais not in lista_paises:
            lista_paises.append(jugador.pais)

        #['Uruguay', 'Brasil', 'Paraguay', 'Argentina', 'EEUU', 'Francia']

    #Para cada pais conseguir los torneos donde salio primero
    
    dic_paises ={}
    for i in lista_paises:
        dic_paises[i] = 0

        #{'Uruguay':0, 'Brasil':0, 'Paraguay':0, 'Argentina':0, 'EEUU':0, 'Francia':0}

    
    for jugador in lista_jugadores:
        for torneo in lista_torneos:
            for pais in dic_paises:
                if jugador.pais == pais:
                    if torneo.get_puesto(jugador.cedula) == 1:
                     dic_paises[pais] += 1
  
    #Ordenar de mayor a menor
    top_sorted ={}
    top_sorted.clear()
    top_sorted = dict( sorted(dic_paises.items(), key=operator.itemgetter(1),reverse=True))
    dict_items = top_sorted.items()
    top_5 ={}
    top_5.clear()
    top_5 = list(dict_items)[:5]

    #Mostrar resulado con loop
    if bool(top_5) == True: #si vacio devuelven False
            print('Top 5 de torneos ganados por país.\n')
            i = 0
            for key, value in top_5:
                print(f'País {key}: {value} torneos ganados')
                i += 1
            menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
    else:
        print('ERROR: No existen campeonatos')
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)


def menu_consultas_4(lista_sponsors,lista_jugadores,lista_torneos): #OKAY
    
    cedula_ingresada = input('Ingrese cédula del jugador: ')

    if check_cedula(cedula_ingresada) == True and check_int(cedula_ingresada):
        cedula_ingresada = int(cedula_ingresada)
        if check_jugador_duplicate(cedula_ingresada,lista_jugadores) == False:
            fecha_ini = input('Ingrese fecha inicio en formato YYYY-MM-DD: ')
            if check_fecha_format(fecha_ini) == True:
                fecha_ini = datetime.datetime.strptime(fecha_ini,"%Y-%m-%d")
                fecha_fin = input('Ingrese fecha fin en formato YYYY-MM-DD: ')

                if check_fecha_format(fecha_fin) == True:
                    fecha_fin = datetime.datetime.strptime(fecha_fin,"%Y-%m-%d")
                    if fecha_fin > fecha_ini:

                        #Get sponsor del jugador
                        nombre_sponsor = None
                        for jugador in lista_jugadores:
                            if jugador.cedula == cedula_ingresada:
                                nombre_sponsor = jugador.sponsor
                        
                        #Get pagos sponsor
                        pago_por_partido = 0
                        pago_fijo =0
                        for sponsor in lista_sponsors:
                            if sponsor.nombre == nombre_sponsor:
                                pago_por_partido = sponsor.pago_partido
                                pago_fijo = sponsor.pago_base
                        
                    
                        #Get campeonatos jugados durante el periodo
                        campeonatos_jugados = 0
                        for torneo in lista_torneos:
                            for jugador in torneo.jugadores:
                                
                                cedula_jugador = jugador
                                if cedula_jugador == cedula_ingresada and torneo.fecha_torneo <= fecha_fin and torneo.fecha_torneo >= fecha_ini:
                                    campeonatos_jugados += 1
                        
                
                        #Get puestos del jugador
                        puestos =[]
                        for torneo in lista_torneos:
                            #print(torneo.jugadores.items())
                            for cedula,puesto in torneo.jugadores.items():
                                if cedula == cedula_ingresada and torneo.fecha_torneo <= fecha_fin and torneo.fecha_torneo >= fecha_ini:
                                    puestos.append((puesto,torneo.tipo_torneo))
                    
                        #Contabilizo 

                        total_por_pago_base = campeonatos_jugados*pago_fijo
                        total_por_partido = 0

                        for index,tuple in enumerate(puestos):
                            if tuple[1] == 250 or tuple[1] == 500:
                                if tuple[0] == 3:
                                    #Solo llego a semi
                                    total_por_partido += 1*pago_por_partido
                                elif tuple[0] == 1 or tuple[0] ==2:
                                    #Llego a final o es campeon
                                    total_por_partido += 2*pago_por_partido
                                    
                            elif tuple[1] == 1000:
                                if tuple[0] == 4:
                                    total_por_partido += 1*pago_por_partido
                                
                                elif tuple[0] == 3:
                                    total_por_partido += 2*pago_por_partido
                                
                                elif tuple[0] == 2 or tuple[0] ==1:
                                    total_por_partido += 3*pago_por_partido

                        total_pagado = total_por_pago_base + total_por_partido
                    
                        print(f'\nEl monto ganado por el jugador {cedula_ingresada} es de ${total_pagado}')
                        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

                    else:
                        print('ERROR: Fecha no puede final no puede ser menor o igual a fecha inicial')
                        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

                else:
                    print('ERROR: Fecha en formato incorrecto\n ¡ Debe ingresar YYYY-MM-DD !')
                    menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
            
            else:
                print('ERROR: Fecha en formato incorrecto\n ¡ Debe ingresar YYYY-MM-DD !')
                menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

        else:
            print(f'Jugador {cedula_ingresada} no esta en el sistema')
            menu_principal(lista_sponsors,lista_jugadores,lista_torneos)
    else:
        print('ERROR: Cedula en formato incorrecto')
        menu_principal(lista_sponsors,lista_jugadores,lista_torneos)

    
    
if __name__ == '__main__':

    #Inicializo las listas que van a guardar los datos
    lista_sponsors, lista_jugadores, lista_torneos = iniciar_listas()

    #menu_principal(lista_sponsors, lista_jugadores, lista_torneos)

#PRUEBAS
# PRUEBA MANUAL   
    #lista_sponsors.append(Sponsor('Nike',200,10))
    #lista_sponsors.append(Sponsor('Coca-cola',500,20))

    #lista_jugadores.append(Jugador(51434026,"Tomas Bordaberry","Uruguay","1999-12-06","Nike"))
    #lista_jugadores.append(Jugador(12345678,"Manuel Bordaberry","Brasil","1992-12-22","Coca-cola"))
    #lista_jugadores.append(Jugador(87654321,"Juan Pablo Bordaberry","Paraguay","1991-04-11","Coca-cola"))
    #lista_jugadores.append(Jugador(78654321,"Pablo Bordaberry","Argentina","1999-12-06","Coca-cola"))
    #lista_jugadores.append(Jugador(68654321,"John Doe","EEUU","1999-12-06","Nike"))
    #lista_jugadores.append(Jugador(58654321,"John Doe Jr","EEUU","1999-12-06","Nike"))
    #lista_jugadores.append(Jugador(48654321,"John Doe Sr","EEUU","1999-12-06","Nike"))
    #lista_jugadores.append(Jugador(11111111,"John Doe 1","Francia","1999-12-06","Nike"))

    #lista_torneos.append(Torneo250('2020-11-09','Wizard Open',{51434026:1,12345678:2,87654321:3,78654321:3}))
    #lista_torneos.append(Torneo250('2020-11-10','Wizard 4',{51434026:2,12345678:3,87654321:1,78654321:3}))
    #lista_torneos.append(Torneo500('2020-12-09','Wizard 5',{58654321:2,48654321:3,68654321:1,78654321:3}))
    #lista_torneos.append(Torneo500('2021-12-19','Wizard 6',{58654321:2,48654321:3,68654321:1,78654321:3}))
    #lista_torneos.append(Torneo500('2021-12-13','Wizard 7',{58654321:2,48654321:3,68654321:1,78654321:3}))
    #lista_torneos.append(Torneo500('2021-12-14','Wizard 8',{58654321:2,48654321:3,68654321:1,78654321:3}))
    #lista_torneos.append(Torneo1000('2021-12-15','Wizard 9',{78654321:2,48654321:3,11111111:1,48654321:3,68654321:4,12345678:4}))
    #lista_torneos.append(Torneo1000('2021-12-16','Wizard 10',{51434026:2,48654321:3,11111111:1,12345678:3,68654321:4,58654321:4}))
    #lista_torneos.append(Torneo1000('2021-12-17','Wizard 11',{51434026:1,48654321:2,11111111:3,12345678:3,68654321:4,58654321:4}))

#Inicializar
    menu_principal(lista_sponsors, lista_jugadores, lista_torneos)

#PRUEBA VIA TERMINAR
# Para ingresar por terminal (Apretar enter despues de poner paste)
    #1
    #Nike
    #10
    #5
    #2
    #11111111
    #Roger Federer
    #Suiza
    #1981-08-08
    #Nike
    #2
    #22222222
    #Rafael Nadal
    #Espana
    #1986-06-03
    #Nike
    #2
    #33333333
    #Novak Djokovic
    #Serbia
    #1987-05-22
    #Nike
    #2
    #44444444
    #Stefanos Tsitsipas
    #Grecia
    #1998-08-12
    #Nike
    #2
    #55555555
    #Alexander Zverev
    #Alemania
    #1997-04-20
    #Nike
    #2
    #66666666
    #Daniil Medvedev
    #Rusia
    #1996-02-11
    #Nike
    #2
    #77777777
    #Jannik Sinner
    #Italia
    #2001-08-16
    #Nike
    #2
    #88888888
    #Carlos Alcaraz
    #Espana
    #2003-05-05
    #Nike
    #3
    #2021-12-29
    #ATP250 Montevideo
    #1
    #11111111
    #2
    #22222222
    #1
    #33333333
    #3
    #66666666
    #3
    #3
    #2021-11-29
    #ATP500 Basilea
    #2
    #11111111
    #1
    #88888888
    #3
    #77777777
    #2
    #44444444
    #3
    #3
    #2021-10-29
    #ATP Masters 1000 Monte Carlo
    #3
    #22222222
    #1
    #33333333
    #2
    #11111111
    #3
    #66666666
    #3
    #44444444
    #4
    #55555555
    #4
    #77777777
    #4
    #88888888
    #4
    

#NOTA: Con lo ultimo que dimos en clase, seria mejor armar una class en principal con un constructor 
    # y poner por ej self._lista_jugadores = [],..., 
    # luego llamar cada vez a las listas con el self._
    #Aclaro que cuando arranque con el proyecto no habiamos dado eso aun. 