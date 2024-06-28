import globales
import math

def buscar_cinco_ventas_mas_altas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    todos_los_empleados = globales.leer_archivo_json('empleados.json') # solo para obtener el nombre del empleado
    # sorted() sirve para ordenar
    # todas_las_ventas son los datos que queremos ordenar
    # key=lambda x: x['columna'] ordenar a partir de clave que indiquemos y que debe existir en los data
    # reverse=True o revese=False para ordenar de mayor a menor o menor a mayor correspondientemente
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['total_venta'], reverse=True)
    # return ventas_ordenadas[:5] # obtenemos las 5 ventas, :5 representa la cantidad de elementos

    print("| id venta | empleado | total venta | propina |")
    for venta in ventas_ordenadas[:5]:
        # obtener el nombre del empleado que se encuentra en json del empleado
        nombre_empleado = ""
        for empleado in todos_los_empleados:
            if empleado['id_empleado'] == venta['id_empleado']:
                nombre_empleado = f"{empleado['nombre']} {empleado['apellido']}"

        print(f"| {venta['id_venta']} | {nombre_empleado} | {venta['total_venta']} | {venta['propina']} |")


def obtener_media_geometrica():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    suma_ventas = 0
    cantidad_ventas = 0

    for venta in todas_las_ventas:
        suma_ventas += math.log(venta['total_venta'])
        cantidad_ventas += 1
    
    media_geometrica = math.exp(suma_ventas / cantidad_ventas)

    return media_geometrica

def obtener_promedio_ventas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    suma_ventas = 0
    cantidad_ventas = 0

    for venta in todas_las_ventas:
        suma_ventas += venta['total_venta']
        cantidad_ventas += 1
    
    promedio_ventas = suma_ventas / cantidad_ventas

    return promedio_ventas

print(obtener_media_geometrica())
