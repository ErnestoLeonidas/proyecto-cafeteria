import globales
import math

def buscar_ventas_mas_altas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    todos_los_empleados = globales.leer_archivo_json('empleados.json')

    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['total_venta'] ,reverse=True)
    print("\n VENTAS MAS ALTAS\n")
    print("| ID Venta \t| Empeado \t| Total Venta \t| Propina \t|")
    print("-----------------------------------------------------------------")
    for venta in ventas_ordenadas[:5]:
        # buscar la coincidencia entre id_empleados
        nombre_empleado = ""
        apellido_empleado = ""
        for empleado in todos_los_empleados:
            if empleado['id_empleado'] == venta['id_empleado']:
                nombre_empleado = empleado['nombre']
                apellido_empleado = empleado['apellido']

        print(f"| {venta['id_venta']} \t\t| {nombre_empleado} {apellido_empleado} \t\t| {venta['total_venta']} \t| {venta['propina']} \t|")

def buscar_ventas_mas_bajas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['total_venta'] ,reverse=False)
    # print("\n VENTAS MAS BAJAS\n")
    # print("| ID Venta \t| Empeado \t| Total Venta \t| Propina \t|")
    # print("-----------------------------------------------------------------")
    # for venta in ventas_ordenadas[:5]:
    #     print(f"| {venta['id_venta']} \t\t| {venta['id_empleado']} \t\t| {venta['total_venta']} \t| {venta['propina']} \t|")
    
    encabezado = ['id_venta','id_empleado','total_venta','propina']
    
    globales.listado_tabla(ventas_ordenadas, encabezado)

def promedio_de_ventas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    suma_ventas = 0
    cantidad_ventas = 0

    for venta in todas_las_ventas:
        suma_ventas += venta['total_venta']
        cantidad_ventas += 1

    try:
        promedio = suma_ventas / cantidad_ventas
    except:
        print("El promedio de ventas es 0")
    
    print(f"El promedio de ventas es {promedio}")

def media_geometrica():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    suma_ventas = 0
    cantidad_ventas = 0

    for venta in todas_las_ventas:
        suma_ventas += math.log(venta['total_venta'])
        cantidad_ventas += 1

    try:
        media_geometrica = math.exp(suma_ventas / cantidad_ventas)
    except:
        print("La media geometricas de ventas es 0")
    
    print(f"La media geometricas de ventas es {media_geometrica}")

def reporte_sueldos():
    todos_los_empleados = globales.leer_archivo_json('empleados.json')

    descuento_salud = 0
    descuesto_previsional = 0
    bono = 0
    total = 0

    print("| id empleado \t| nombre \t| sueldo | salud | previsional | bono | total |")
    for empleado in todos_los_empleados:
        descuento_salud = int(empleado['sueldo'] * 0.07) # 7%
        descuesto_previsional = int(empleado['sueldo'] * 0.12) # 12%
        bono = int(empleado['sueldo'] * 0.1) # 10%

        total = empleado['sueldo'] + bono - descuento_salud - descuesto_previsional

        print(f"| {empleado['id_empleado']}\t\t| {empleado['nombre']} {empleado['apellido']} | ${empleado['sueldo']} | ${descuento_salud} | ${descuesto_previsional} | ${bono} | ${total} |")

def clasificar_ventas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    categorias = {
        "30000 a 40000": [],
        "40001 a 50000": [],
        "50001 a 70000": []
    }

    for venta in todas_las_ventas:
        if venta['total_venta'] >= 30000 and venta['total_venta'] <= 40000:
            categorias['30000 a 40000'].append(venta)
        elif venta['total_venta'] >= 40001 and venta['total_venta'] <= 50000:
            categorias['40001 a 50000'].append(venta)
        elif venta['total_venta'] >= 50001 and venta['total_venta'] <= 70000:
            categorias['50001 a 70000'].append(venta)

    for rango, detalle_ventas in categorias.items():
        print(f"{rango}")
        print("| ID Venta \t| Empeado \t| Total Venta \t| Propina \t|")
        print("-----------------------------------------------------------------")
        for venta in detalle_ventas:
            print(f"| {venta['id_venta']} \t\t| {venta['id_empleado']} \t\t| {venta['total_venta']} \t| {venta['propina']} \t|")


        

buscar_ventas_mas_bajas()
