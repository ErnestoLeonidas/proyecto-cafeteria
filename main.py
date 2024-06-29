import os
import globales
import ventas
import reportes
import estadisticas
os.system("cls")

def menu_estadisticas():
    while True:
        os.system("cls")
        print("1. Venta más alta")
        print("2. Venta más baja")
        print("3. Promedio Ventas")
        print("4. Media Geométrica")
        print("5. Salir")

        opcion = globales.seleccionar_opcion(5)

        if opcion == 1:
            print("1. Venta más alta")
            estadisticas.buscar_venta_mas_alta()
        elif opcion == 2:
            print("2. Venta más baja")
            estadisticas.buscar_venta_mas_baja()
        elif opcion == 3:
            print("3. Promedio Ventas")
            estadisticas.obtener_promedio_ventas()
        elif opcion == 4:
            print("4. Media Geométrica")
            estadisticas.obtener_media_geometrica()
        elif opcion == 5:
            print("5. Salir")
            return
        input()


def menu_general():
    while True:
        os.system("cls")
        print("1. Precargar ventas")
        print("2. Crear Venta")
        print("3. Reporte de sueldos")
        print("4. Estadisticas")
        print("5. Clasificación de ventas")
        print("6. Salir")

        opcion = globales.seleccionar_opcion(6)

        if opcion == 1:
            print("1. Precargar ventas")
            ventas.precargar_ventas()
        elif opcion == 2:
            print("2. Crear Venta")
            ventas.crear_venta()
        elif opcion == 3:
            print("3. Reporte de sueldos")
            reportes.reporte_sueldos()
        elif opcion == 4:
            print("4. Estadisticas")
            menu_estadisticas()
        elif opcion == 5:
            print("5. Clasificación de ventas")
            estadisticas.clasificar_ventas()
        elif opcion == 6:
            print("6. Salir")
            return
        
        input()

if __name__ == "__main__":
    menu_general()