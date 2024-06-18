import manejo_archivos
import ventas

def main_menu():
    while True:
        print("\nMenu Principal")
        print("1. Precargar ventas")
        print("2. Crear venta")
        print("3. Reporte de sueldos")
        print("4. Ver Estadísticas")
        print("5. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            ventas.preload_sales()
        elif choice == "2":
            ventas.create_sale()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main_menu()
