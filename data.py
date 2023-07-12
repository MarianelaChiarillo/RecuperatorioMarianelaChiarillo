
import os
import re
import random
from menu import menu


def listar(nombre_archivo: str) -> list[dict]:
    Lista = []  # Lista vacía que va a almacenar los elementos.
	
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file: 
            lineas = map(lambda linea: linea.strip().split(","), file)  # En cada línea elimino los espacios en blanco y las separo por comas
            for linea in lineas:
                if len(linea) == 4:  # Verificar si la línea tiene los 6 campos necesarios (incluyendo el stock)
                    pelicula = {
                        "id_peli": linea[0],
                        "titulo": linea[1],
                        "genero": linea[2],
                        "duracion": linea[3],
                    }
                    Lista.append(pelicula)
                
        # Agregar líneas de stock a los diccionarios de peliculas
        for pelicula in Lista:
            if pelicula["duracion"] == "0":
                pelicula["duracion"] = str(random.randint(100, 240))  # Genero un número aleatorio para el stock y lo convierto a cadena

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'.")
    
    return Lista

# Ejemplo de uso
ruta_csv = "movies.csv"  # Ruta del archivo CSV
peliculas = listar(ruta_csv)  # Obtener la lista de productos desde el archivo CSV

#------------------------------------------------------------------------------------------------------------
def listaPeli(lista: list[dict]) -> set:

    nombres = set() #set marcas para almacenar las pelis sin duplicados.
    generos = set() #set pelis para almacenar las pelis sin duplicados.

    for diccionario in lista:
        nombre = diccionario.get('titulo') #cada dict, se consigue el valor  de la clave 'MARCA' utilizando  get(). 
        #Si se encuentra un valor válido  se agrega la marca al set.
        if nombre:
            nombres.add(nombre) #Si se encuentra un valor válido  se agrega la marca al set.

    for diccionario in lista:
        genero = diccionario.get('genero') #cada dict, se consigue el valor  de la clave 'MARCA' utilizando  get(). 
        #Si se encuentra un valor válido  se agrega la marca al set.
        if genero:
            generos.add(genero) #Si se encuentra un valor válido  se agrega la marca al set.

    print("""
---------------------------------- 
Peliculas:
----------------------------------  
        """)
    for nombre in nombres: #itera sobre cada marca en el conjunto pelis.
        cantidad = len(list(filter(lambda x: x.get('titulo') == nombre, lista)))
        cantidad = len(list(filter(lambda x: x.get('genero') == genero, lista)))#la función filter junto con una expresión lambda para filtrar los elementos .
        print(f"*Nombre: {nombre} Genero: {genero} ")


#-----------------------------------------------------------------------------------------------------------------------------------------
def listar_generos(lista: list[dict]):
    generos = set()  # Conjunto para almacenar las generos sin duplicados


    for diccionario in lista:
        titu = diccionario.get('genero')  # Obtener el valor del índice 'titu' del diccionario
        if titu:  # Verificar si se encontró una titu válida
            generos.add(titu)  # Agregar la titu al conjunto

    print("""
---------------------------------- 
Listado pelis por genero:
----------------------------------  
        """)

    for titu in generos:
        print(f"Genero: {titu}")
        insumos_filtrados = filter(lambda x: x.get('genero') == titu, lista)  # Filtrar insumos por marca
        
        insumos_lista = []  # Lista para almacenar 
        for insumo in insumos_filtrados:  
            nombre = insumo.get('titulo')  # Obtener el nombre del insumo
            insumos_filtrados = sorted(lista[1:], key=lambda producto: (producto['duracion']))
            duracion = insumo.get('duracion')  # Obtener el nombre del insumo

            insumos_lista.append(f"  Titulo: {nombre} - Duracion: {duracion} ")
        
        print('\n'.join(insumos_lista))  # Imprimir la lista completa de insumos de la marca
        print("." * 90)

    return lista_peliculas

ruta_csv = 'Peliculas.csv' #defino ruta.
lista_peliculas = listar(ruta_csv)

#peliculas = listar(ruta_csv)  # Obtener la lista de productos desde el archivo CSV
 
def guardar_csv(ruta):
    print(peliculas)
    with open(ruta, 'w', newline='', encoding='utf-8') as file:
        # Escribir título indicando que contiene peliculas actualizados
        file.write("\n--- Peliculas ---\n")
        for pelicula in peliculas:
            linea = f"{pelicula['id_peli']},{pelicula['titulo']},{pelicula['genero']},{pelicula['duracion']}\n"
            file.write(linea)
            

#------------------------------------------------------------------------------------------------------------------------------------------

def buscar(listaP: list[dict]):
    coincidencias = [] #Lista que va a recibir todas las coincidencias.

    for pelicula in listaP: #itea en la lista de insumos.
        generos = pelicula["genero"] #se tiene el value de la clave lo que seria las caracteristicas.
        if re.match(rf'.*\b{clave.lower()}\b.*', generos.lower()): #el re match lo utilizo para buscar coincidencias por lo que se buscan coincidnecias en la palabra clave.
            coincidencias.append(pelicula) #cualquier caracteristica lo integro.

    if coincidencias: # si hay coincidencias imprimo toda la informacion.
        print("""
--------------------------------------------
 Coincidencias encontradas con su búsqueda:
--------------------------------------------""")
        
        for pelicula in coincidencias:
            pelicula = pelicula["titulo"]
            #generos_juntas = ", ".join(generos)  # Une las características en una cadena separada por comas
            print(f"Titulo: {pelicula}")
            #print(f"Característica: {generos_juntas}")
            print("." * 130)
    else:
        print("* Lo siento, no se han encontrado coincidencias.") #si no hay caracteristicas mando un mensaje.

#-----------------------------------------------------------------------------------------------------------------------------------------
flag_bienvenida = False
nombre_archivo = None  # Variable para almacenar el nombre del archivo

while True:
    os.system("cls")

    match(menu()):
        case "0":
            print("Entendido, comencemos.")
            flag_bienvenida = True

        case "1":
            if flag_bienvenida:
                if nombre_archivo is None:
                    nombre_archivo = input("Ingrese el nombre del archivo: ")
                    peliculas = listar(nombre_archivo)
            else:
                print("Debe poner confirmar para saber más información.")

        case "2":
            if flag_bienvenida:
                if nombre_archivo is None:
                    print("Debe ingresar un archivo primero.")
                else:
                    lista = listar(nombre_archivo)  # Obtener la lista de insumos
                    listaPeli(lista)  # Mostrar los insumos por marca
            else:
                print("Debe poner confirmar para saber más información.")
        
        case "3":
            if flag_bienvenida:
                if nombre_archivo is None:
                    print("Debe ingresar un archivo primero.")
                else:
                   print("Ya se han asignado las duraciones.")
            else:
                print("Debe poner confirmar para saber más información.")
        
       
        case "4":
            if flag_bienvenida:
                if nombre_archivo is None:
                    print("Debe ingresar un archivo primero.")
                else:
                    clave = input("Ingrese la característica que desea buscar --> ")
                    clave = clave.lower()
                    lista = listar(nombre_archivo)
                    buscar(lista)     
            else:
                print("Debe poner confirmar para saber más información.")

        case "5":
            if flag_bienvenida:
                if nombre_archivo is None:
                    print("Debe ingresar un archivo primero.")
                else:
                    lista = listar(nombre_archivo)  # Obtener la lista de insumos
                    listar_generos(lista)  # Mostrar los insumos por marca
            else:
                print("Debe poner confirmar para saber más información.")
        
        case "6":
            if flag_bienvenida:
                if nombre_archivo is None:
                    print("Debe ingresar un archivo primero.")
                else:
                    guardar_csv('Peliculas.csv')
                    print("Archivo generado.")              
            else:
                print("Debe poner confirmar para saber más información.")

        case "7":
            if nombre_archivo is None:
                print("Debe ingresar un archivo primero.")
            else:
                salir = input("Confirma salida? 01: ")
                if salir == "01":
                    break
        
        
    input("Presione enter para continuar")
