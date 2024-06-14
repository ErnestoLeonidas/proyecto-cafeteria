import os
import json
os.system("cls")

URL_EMPLEADOS = 'empleados.json'
# URL_PRODUCTOS = 

# leer archivo json
def leer_archivo_json(url):
    try:
        with open(url, 'r') as archivo: # leemos el archivo
            return json.load(archivo) # retornamos lo que quenga el archivo
    except:
        return []

def guardar_archivo_json(url, data):
    try:
        with open(url, 'w') as archivo: # leemos el archivo
            json.dump(data, archivo, indent=4)
    except:
        return []
    
def crear_empleado():
    os.system("cls")
    print("== REGISTRAR DE EMPLEADO ==")
    empleados = leer_archivo_json(URL_EMPLEADOS)
    
    id_empleado = input("Ingrese el ID del nuevo empleado >> ")
    nombre = input("Ingrese el NOMBRE del nuevo empleado >> ")
    apellido = input("Ingrese el APELLIDO del nuevo empleado >> ")
    sueldo = int(input("Ingrese el SUELDO del nuevo empleado >> ")) # que falta validar el int
    id_cargo = input("Ingrese el ID CARGO del nuevo empleado >> ")

    nuevo_empleado = {
        "id_empleado": id_empleado,
        "nombre": nombre,
        "apellido": apellido,
        "sueldo": sueldo,
        "id_cargo": id_cargo
    }
    
    empleados.append(nuevo_empleado)
    
    guardar_archivo_json(URL_EMPLEADOS, empleados)

def listar_empleados():
    os.system("cls")
    print("== LISTADO DE EMPLEADOS ==")

    empleados = leer_archivo_json(URL_EMPLEADOS)
    
    headers = ['id_empleado', 'nombre', 'apellido', 'sueldo', 'id_cargo']
    col_widths = [15,15,15,15,15]
    
    # Imprimir el encabezado
    header_line = ' | '.join(f"{header.capitalize():^{col_widths[i]}}" for i, header in enumerate(headers))
    print(header_line)
    print('-' * len(header_line))
    
    for empleado in empleados:
        row = ' | '.join(f"{str(empleado.get(header, '')):^{col_widths[i]}}" for i, header in enumerate(headers))
        print(row)

def actualizar_empleado():
    os.system("cls")
    print("== EDITAR DE EMPLEADO ==")
    empleados = leer_archivo_json(URL_EMPLEADOS)
    
    listar_empleados()
    id_empleado = input("Ingrese el ID del empleado que desea Editar >> ")

    nombre = input("Ingresa el nuevo NOMBRE del empleado >> ")
    apellido = input("Ingresa el nuevo APELLIDO del empleado >> ")
    sueldo = int(input("Ingresa el nuevo SUELDO del empleado >> ")) # validar el int
    id_cargo = input("Ingresa el nuevo ID CARGO del empleado >> ")
    
    for empleado in empleados:
        if empleado['id_empleado'] == id_empleado:
            empleado['nombre'] = nombre
            empleado['apellido'] = apellido
            empleado['sueldo'] = sueldo
            empleado['id_cargo'] = id_cargo
            break
    
    guardar_archivo_json(URL_EMPLEADOS, empleados)
            
def eliminar_empleado():
    os.system("cls")
    print("== BORRAR DE EMPLEADO ==")
    empleados = leer_archivo_json(URL_EMPLEADOS)
    
    listar_empleados()
    id_empleado = input("Ingrese el ID del empleado que desea Eliminar >> ")
    
    empleados_que_quedan = []
    
    for empleado in empleados:
        if empleado['id_empleado'] != id_empleado:
            empleados_que_quedan.append(empleado)
    
    guardar_archivo_json(URL_EMPLEADOS, empleados_que_quedan)
    
def menu_general():
    os.system("cls")
    print("== EMPLEADOS ==")
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
            crear_empleado()
        elif opcion == 2:
            actualizar_empleado()
        elif opcion == 3:
            listar_empleados()
        elif opcion == 4:
            eliminar_empleado()
        elif opcion == 5:
            return
        input()

if __name__ == "__main__":
    iniciar_programa()