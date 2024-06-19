import json
import csv

def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion

# leer archivo json
def leer_archivo_json(dir):
    try:
        with open(dir, 'r') as archivo: # leemos el archivo
            return json.load(archivo) # retornamos lo que quenga el archivo
    except:
        return []

def guardar_archivo_json(dir, data):
    try:
        with open(dir, 'w') as archivo: # leemos el archivo
            json.dump(data, archivo, indent=4)
    except:
        return []