import os
import random
import globales
os.system("cls")


def crear_ventas():
    # 1. Traemos la información que existe en el archivo
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    # 2. capturamos los datos para la nueva venta 
    # utilizando la estructura de la venta
    id_venta = int(input("Ingrese el id_venta de la nueva venta >> "))
    id_empleado = input("Ingresa el id_empleado de la nueva venta >> ")
    total_venta = int(input("Ingresa el TOTAL de la nueva venta >> "))
    propina = total_venta * 0.1
    # 3. creamos la variable de la nueva venta
    # utilizando la estructura de la venta
    nueva_venta = {
        "id_venta": id_venta,
        "id_empleado": id_empleado,
        "total_venta": total_venta,
        "propina": propina
    }
    # 4. Agregamos la nueva_venta al todas_las_ventas
    todas_las_ventas.append(nueva_venta)
    # 5. Guardamos el archivo con la nueva venta indicando el archivo y la data
    globales.guardar_archivo_json('ventas.json', todas_las_ventas)

def precargar_ventas():
    ventas = globales.leer_archivo_json('ventas.json')
    empleados = globales.leer_archivo_json('empleados.json') # todos los empleados

    # ventas[-1:] Va a buscar el último elemento del listado
    # ventas[-1:][0] Aceder a ese última venta porque trae el array con 1 elemento
    # ventas[-1:][0]['id_venta'] Accede solo a la clave que necesitamos
    id_venta = ventas[-1:][0]['id_venta']

    for i in range(10):
        empleado = random.choice(empleados) # traemos 1 empleado aleatorio

        id_venta += 1
        id_empleado = empleado['id_empleado']
        # Generar una venta aleatorea entre 30.000 y 70.000 redondeado a la centena
        total_venta = random.randint(300,700) * 100
        propina = total_venta * 0.1

        nueva_venta = {
            "id_venta": id_venta,
            "id_empleado": id_empleado,
            "total_venta": total_venta,
            "propina": propina
        }

        ventas.append(nueva_venta)
    
    globales.guardar_archivo_json('ventas.json', ventas)
    input("Ventas cargadas")
