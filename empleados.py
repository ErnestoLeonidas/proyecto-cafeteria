import os
import globales

def reporte_sueldos():
    todos_los_empleados = globales.leer_archivo_json('empleados.json')

    for empleado in todos_los_empleados:
        print(f" {empleado['id_empleado']} | {empleado['nombre']} {empleado['apellido']} | ${empleado['sueldo']} ")