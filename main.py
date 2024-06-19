import os
import globales
import ventas
os.system("cls")

def menu_general():
    while True:
        os.system("cls")
        print("1. Precargar ventas")
        print("2. Crear Venta")
        print("3. Reporte de sueldos")
        print("4. Estadisticas")
        print("5. Salir")

        opcion = globales.seleccionar_opcion(5)

        if opcion == 1:
            print("1. Precargar ventas")
            ventas.precargar_ventas()
        elif opcion == 2:
            print("2. Crear Venta")
        elif opcion == 3:
            print("3. Reporte de sueldos")
        elif opcion == 4:
            print("4. Estadisticas")
        elif opcion == 5:
            print("5. Salir")
            return
        
        input()

if __name__ == "__main__":
    menu_general()