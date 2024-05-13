import json
from datetime import datetime
import pytz
import os

# Obtener la zona horaria de España
spain_timezone = pytz.timezone('Europe/Madrid')

# Obtener la fecha y hora actual en la zona horaria de España
current_time_in_spain = datetime.now(spain_timezone)

# Formatear la fecha y hora
formatted_time = current_time_in_spain.strftime('%Y-%m-%d %H:%M:%S')

# Crear un diccionario con la información
data = {
    'datetime': formatted_time
}

# Obtener el directorio actual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Nombre del archivo
file_name = 'datetime_spain.json'

# Ruta completa del archivo
file_path = os.path.join(current_directory, file_name)

# Guardar los datos en un archivo .json
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f'Archivo {file_name} creado con éxito en {current_directory}')
