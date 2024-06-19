import os
import random
from manejo_archivo import leer_archivo_json, guardar_archivo_json, leer_archivo_csv, guardar_archivo_csv

os.system("cls")

def cargar_ventas():
    ventas = leer_archivo_json('ventas.json')
    empleados = leer_archivo_json('empleados.json')
    ultimo_id = 103

    for i in range(10): # generar 10 vueltas
        empleado = random.choice(empleados)
        total_ventas = random.randint(20000,70000)
        ultimo_id += 1

        nueva_venta = {
            "id_venta": ultimo_id,
            "empleado": empleado['id_empleado'],
            "total_venta": total_ventas,
            "propina": total_ventas * 0.1
        }

        ventas.append(nueva_venta)
        
    guardar_archivo_json('ventas.json', ventas)
    print("ventas aleatoreas cargadas")
        
