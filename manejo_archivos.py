import json
import csv

def load_json_data(filename):
    """
    Carga datos desde un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo a cargar.
        
    Returns:
        list or dict: Los datos cargados desde el archivo JSON.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json_data(filename, data):
    """
    Guarda datos en un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo donde se guardarán los datos.
        data (list or dict): Los datos a guardar en formato JSON.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_csv_data(filename):
    """
    Carga datos desde un archivo CSV.
    
    Args:
        filename (str): El nombre del archivo a cargar.
        
    Returns:
        list of dict: Los datos cargados desde el archivo CSV.
    """
    with open(filename, newline='', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def save_csv_data(filename, data, fieldnames):
    """
    Guarda datos en un archivo CSV.
    
    Args:
        filename (str): El nombre del archivo donde se guardarán los datos.
        data (list of dict): Los datos a guardar en formato CSV.
        fieldnames (list of str): Los nombres de las columnas para el archivo CSV.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
