import os
# import ventas
from ventas import cargar_ventas

os.system("cls")

def main_menu():
    while True:
        os.system("cls")
        print("1. Precargar ventas")
        print("2. Crear venta")
        print("3. Reporte de sueldos")
        print("4. Ver Estadísticas")
        print("5. Salir")

        opcion = seleccionar_opcion(5)

        if opcion == 1:
            cargar_ventas()
            # ventas.cargar_ventas()
        elif opcion == 2:
            print("2. Crear venta")
        elif opcion == 3:
            print("3. Reporte de sueldos")
        elif opcion == 4:
            print("4. Ver Estadísticas")
        elif opcion == 5:
            print("5. Salir")
            return

        input()

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

if __name__ == "__main__":
    main_menu()