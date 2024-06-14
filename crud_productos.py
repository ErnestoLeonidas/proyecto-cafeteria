import os
import csv
os.system("cls")

DIR_PRODUCTOS = 'productos.csv'
FIELDNAMES_PRODUCTOS = ['id_producto', 'nombre_producto', 'precio', 'stock']

def leer_archivo_csv(dir):
    try:
        with open(dir, mode='r', newline='') as archivo:
            data = csv.DictReader(archivo)
            return list(data)
    except:
        return []

def guardar_archivo_csv(dir, data, fieldnames):
    try:
        with open(dir, mode='w', newline='') as archivo:
            data_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
            data_csv.writeheader()
            data_csv.writerows(data)
    except:
        return []


def crear_productos():
    os.system("cls")
    print("== REGISTRAR NUEVO PRODUCTO ==")
    productos = leer_archivo_csv(DIR_PRODUCTOS)

    # id_producto,nombre_producto,precio,stock

    id_producto = input("Ingrese el ID del producto >> ")
    nombre_producto = input("Ingrese el NOMBRE del producto >> ")
    precio = int(input("Ingrese el VALOR del producto >> ")) # validar los int (try)
    stock = int(input("Ingrese el STOCK del producto >> ")) # validar los int (try)

    nuevo_producto = {
        "id_producto": id_producto,
        "nombre_producto": nombre_producto,
        "precio": precio,
        "stock": stock
    }

    productos.append(nuevo_producto)

    # usar la funcion para crear el archivo csv
    guardar_archivo_csv(DIR_PRODUCTOS, productos, FIELDNAMES_PRODUCTOS)


def menu_general():
    os.system("cls")
    print("== PRODUCTOS ==")
    print("1. Crear         - Create")
    print("2. Actualizar    - Update")
    print("3. Listar        - Read")
    print("4. Borrar        - Delete")
    print("5. Salir")
    
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

def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)
        
        if opcion == 1:
            crear_productos()
        elif opcion == 2:
            print("Actualizar")
        elif opcion == 3:
            print("Listar")
        elif opcion == 4:
            print("Borrar")
        elif opcion == 5:
            return
        input()

if __name__ == "__main__":
    iniciar_programa()