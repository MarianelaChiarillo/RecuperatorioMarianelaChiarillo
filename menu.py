from data import *

def menu():

    print("""
    *** Menu de opciones ***"
    ----------------------- 
    Bienvenido, comenzamos? Ingrese -> 0
    1. Cargar datos.
    2. Imprimir Lista.
    3. Asignar Tiempos.
    4. Filtar por tipo.
    5. Mostrar duraciones.
    6. Guardar Peliculas.
    7. Salir""")
    opcion = input("Ingrese una opcion numerica: ") 
    return opcion 
