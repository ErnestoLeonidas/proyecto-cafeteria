import random
import json
from manejo_archivos import load_json_data, save_json_data, load_csv_data

# Función para precargar 80 ventas aleatorias
def preload_sales():
    ventas = load_json_data('ventas.json')
    empleados = load_json_data('empleados.json')
    productos = load_csv_data('productos.csv')
    last_id = int(ventas[-1]['id_venta'][1:])  # Obtiene el último ID de venta y lo convierte en entero

    for i in range(80):
        empleado = random.choice(empleados)
        num_productos = random.randint(1, 5)  # Cantidad aleatoria de productos diferentes por venta
        total_venta = 0
        detalles_productos = []

        for _ in range(num_productos):
            producto = random.choice(productos)
            cantidad = random.randint(1, 3)  # Cantidad aleatoria de cada producto
            subtotal = int(producto['precio']) * cantidad
            total_venta += subtotal
            detalles_productos.append({
                "id_producto": producto['id_producto'],
                "cantidad": cantidad,
                "precio_unitario": int(producto['precio']),
                "subtotal": subtotal
            })

        total_venta = round(total_venta, -2)  # Redondear al centenar más cercano
        propina = round(0.1 * total_venta)  # Propina del 10%

        ventas.append({
            "id_venta": f"V{last_id + i + 1}",
            "empleado": empleado['id_empleado'],
            "fecha": "2024-06-15",
            "total_venta": total_venta,
            "productos": detalles_productos,
            "propina": propina
        })

    save_json_data('ventas.json', ventas)
    print("Ventas aleatorias generadas con éxito.")

# Función para crear una nueva venta
def create_sale():
    empleados = load_json_data('empleados.json')
    productos = load_csv_data('productos.csv')
    ventas = load_json_data('ventas.json')
    last_id = int(ventas[-1]['id_venta'][1:])  # Obtiene el último ID de venta

    # Selección del empleado
    print("Empleados disponibles:")
    for emp in empleados:
        print(f"ID: {emp['id_empleado']} - Nombre: {emp['nombre']} {emp['apellido']}")
    emp_id = input("Ingrese el ID del empleado que realiza la venta: ")

    # Agregar productos a la venta
    total_venta = 0
    detalles_productos = []
    while True:
        print("Productos disponibles:")
        for prod in productos:
            print(f"ID: {prod['id_producto']} - Nombre: {prod['nombre']} - Precio: {prod['precio']}")
        prod_id = input("Ingrese el ID del producto a vender (escriba 'fin' para terminar): ")
        if prod_id.lower() == 'fin':
            break
        cantidad = int(input("Ingrese la cantidad del producto: "))
        producto_seleccionado = next((p for p in productos if p['id_producto'] == prod_id), None)
        
        if producto_seleccionado:
            subtotal = int(producto_seleccionado['precio']) * cantidad
            total_venta += subtotal
            detalles_productos.append({
                "id_producto": prod_id,
                "cantidad": cantidad,
                "precio_unitario": int(producto_seleccionado['precio']),
                "subtotal": subtotal
            })
        else:
            print("Producto no encontrado, intente nuevamente.")
    
    total_venta = round(total_venta, -2)
    propina = round(0.1 * total_venta)
    
    # Generar la boleta
    ventas.append({
        "id_venta": f"V{last_id + 1}",
        "empleado": emp_id,
        "fecha": "2024-06-15",
        "total_venta": total_venta,
        "productos": detalles_productos,
        "propina": propina
    })
    save_json_data('ventas.json', ventas)
    print("Venta creada con éxito.")
