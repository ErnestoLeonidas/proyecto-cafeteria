import os
import json
os.system("clear")

URL_EMPLEADOS = 'empleados.json'
# URL_CARGOS
# URL_PRODUCTOS

def cargar_json(url_archivo):
    try:
        with open(url_archivo, 'r') as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_archivo(url_archivo, data):
    with open(url_archivo, 'w') as archivo:
        json.dump(data, archivo, indent=4)

def crear_empleado():
    empleados = cargar_json(URL_EMPLEADOS)
    
    id_empleado = input("Ingrese el ID del empleado >> ")
    nombre = input("Ingrese NOMBRE del empleado >> ")
    apellido = input("Ingrese APELLIDO del empleado >> ")
    try:
        sueldo = int(input("Ingrese el SUELDO del empleado >> "))
    except:
        sueldo = 0
    id_cargo = input("Ingrese el CARGO del empleado >> ")
    
    nuevo_empleado = {
        "id_empleado": id_empleado,
        "nombre": nombre,
        "apellido": apellido,
        "sueldo": sueldo,
        "id_cargo": id_cargo
    }
    
    empleados.append(nuevo_empleado) # acá tenemos el nuevo empleado añadido solamente al array y no al archivo json
    # ahora guardamos el array dentro del archivo json
    guardar_archivo(URL_EMPLEADOS, empleados)

def actualizar_empleado():
    empleados = cargar_json(URL_EMPLEADOS)
    
    id_empleado = input("Ingrese el ID del empleado a modificar >> ")
    
    nombre = input("Ingrese NOMBRE del empleado >> ")
    apellido = input("Ingrese APELLIDO del empleado >> ")
    try:
        sueldo = int(input("Ingrese el SUELDO del empleado >> "))
    except:
        sueldo = 0
    id_cargo = input("Ingrese el CARGO del empleado >> ")
    
    for emp in empleados:
        if emp['id_empleado'] == id_empleado:
            emp['nombre'] = nombre
            emp['apellido'] = apellido
            emp['sueldo'] = sueldo
            emp['id_cargo'] = id_cargo
            break
        
    guardar_archivo(URL_EMPLEADOS, empleados)

def eliminar_empleado():
    empleados = cargar_json(URL_EMPLEADOS)
    id_empleado = input("Ingrese el ID del empleado a eliminar >> ")
    
    aux_empleado = []
    
    for emp in empleados:
        if emp['id_empleado'] != id_empleado:
            aux_empleado.append(emp)
    
    guardar_archivo(URL_EMPLEADOS, aux_empleado)
    

def listar_empleados():
    empleados = cargar_json(URL_EMPLEADOS)
    
    headers = ['id_empleado', 'nombre', 'apellido', 'sueldo', 'id_cargo']
    col_widths = [15,15,15,15,15]
    
    # Imprimir el encabezado
    header_line = ' | '.join(f"{header.capitalize():^{col_widths[i]}}" for i, header in enumerate(headers))
    print(header_line)
    print('-' * len(header_line))
    
    for empleado in empleados:
        row = ' | '.join(f"{str(empleado.get(header, '')):^{col_widths[i]}}" for i, header in enumerate(headers))
        print(row)
    

def menu_general():
    os.system("clear")
    print("1. Crear empleado")
    print("2. Actualizar empleado")
    print("3. Eliminar empleado")
    print("4. Listar empleado")
    print("5. Salir")

def seleccionar_opcion(max_opcion):
    opcion = 0
    while True: 
        try:
            opcion = int(input("Seleccione una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opcion:
            input("Opción invalida intente nuevamente >> ")
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
            eliminar_empleado()
        elif opcion == 4:
            listar_empleados()
        elif opcion == 5:
            return

        input()

if __name__ == "__main__":
    iniciar_programa()