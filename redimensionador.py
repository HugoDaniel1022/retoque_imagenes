from PIL import Image
import os

def resize_images(input_folder, output_folder, width, height):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Procesar cada archivo en la carpeta de entrada
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.webp', '.png')):
            # Abrir la imagen
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                # Redimensionar la imagen
                img_resized = img.resize((width, height))
                # Guardar la imagen redimensionada en la carpeta de salida
                output_path = os.path.join(output_folder, filename)
                img_resized.save(output_path)
            print(f"{filename} redimensionada y guardada en {output_folder}")

# Ejemplo de uso
input_folder = 'C:/Users/Usuario/Desktop/redimensionador de imagenes/marcadas'
output_folder = 'C:/Users/Usuario/Desktop/redimensionador de imagenes/redimensionadas'
width, height = 600, 600  # Cambia las dimensiones según lo que necesites
resize_images(input_folder, output_folder, width, height)
