import os
import random
import globales
os.system("cls")

def crear_venta():
    # 1. abrimos el archivo json y cargamos su informacion en una variable
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    # 2. Capturar las variables para generar la nueva venta
    # el archivo da la estructura
    # id_venta = int(input("Ingresa el ID de la venta >> "))
    id_venta = todas_las_ventas[-1:][0]['id_venta']+1 # recordar sumar 1
    id_empleado = input("Ingresa el ID EMPLEADO de la nueva venta >> ")
    total_venta = int(input("Ingresa el total de la nueva venta >> "))
    propina = total_venta * 0.1
    # 3. Crear nueva venta
    nueva_venta = {
        "id_venta": id_venta,
        "id_empleado": id_empleado,
        "total_venta": total_venta,
        "propina": propina
    }
    # 4. Debemos agregar la nueva venta a todas las ventas
    todas_las_ventas.append(nueva_venta)
    # 5. guardar el archivo con la nueva informacion
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
