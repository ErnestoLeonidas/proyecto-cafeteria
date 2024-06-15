import os
import csv
os.system("cls")

DIR_PRODUCTOS = 'productos.csv'
FIELDNAMES_PRODUCTOS = ['id_producto', 'nombre_producto', 'precio', 'stock']

def leer_archivo_csv(dir):
    try:
        with open(dir, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.DictReader(archivo)
            return list(data)
    except:
        return []

def guardar_archivo_csv(dir, data, fieldnames):
    try:
        with open(dir, mode='w', newline='', encoding='utf-8') as archivo:
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

def listar_productos():
    os.system("cls")
    print("== LISTADO DE PRODUCTOS ==")

    productos = leer_archivo_csv(DIR_PRODUCTOS)
    
    headers = FIELDNAMES_PRODUCTOS
    col_widths = [15,25,15,15]
    
    # Imprimir el encabezado
    header_line = ' | '.join(f"{header.capitalize():^{col_widths[i]}}" for i, header in enumerate(headers))
    print(header_line)
    print('-' * len(header_line))
    
    for producto in productos:
        row = ' | '.join(f"{str(producto.get(header, '')):^{col_widths[i]}}" for i, header in enumerate(headers))
        print(row)

def actualizar_productos():
    os.system("cls")
    print("== EDITAR PRODUCTO ==")
    productos = leer_archivo_csv(DIR_PRODUCTOS)
    
    listar_productos()
    id_producto = input("Ingrese el ID del producto que desea Editar >> ")   

    nombre_producto = input("Ingrese el NOMBRE del producto >> ")
    precio = int(input("Ingrese el VALOR del producto >> ")) # validar los int (try)
    stock = int(input("Ingrese el STOCK del producto >> ")) # validar los int (try)

    
    for producto in productos:
        if producto['id_producto'] == id_producto:
            producto['nombre_producto'] = nombre_producto
            producto['precio'] = precio
            producto['stock'] = stock
            break
    
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
            actualizar_productos()
        elif opcion == 3:
            listar_productos()
        elif opcion == 4:
            print("Borrar")
        elif opcion == 5:
            return
        input()

if __name__ == "__main__":
    iniciar_programa()