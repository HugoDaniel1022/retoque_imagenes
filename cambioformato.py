from PIL import Image
import os
import shutil

def convertir_a_jpeg(ruta_entrada, ruta_salida):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)
    
    # Recorrer todos los archivos en la carpeta de entrada
    for nombre_archivo in os.listdir(ruta_entrada):
        ruta_completa_entrada = os.path.join(ruta_entrada, nombre_archivo)
        
        # Verificar si es un archivo de imagen
        if os.path.isfile(ruta_completa_entrada):
            try:
                with Image.open(ruta_completa_entrada) as img:
                    # Verificar si la imagen ya está en formato JPEG
                    if img.format == 'JPEG':
                        # Si ya es JPEG, simplemente copiar la imagen a la carpeta de salida
                        ruta_completa_salida = os.path.join(ruta_salida, nombre_archivo)
                        shutil.copy(ruta_completa_entrada, ruta_completa_salida)
                        print(f"{nombre_archivo} ya está en formato JPEG. Se ha copiado a la carpeta de salida.")
                    else:
                        # Definir la nueva ruta de salida con la extensión .jpg
                        nombre_salida = os.path.splitext(nombre_archivo)[0] + ".jpg"
                        ruta_completa_salida = os.path.join(ruta_salida, nombre_salida)
                        
                        # Convertir y guardar la imagen en formato JPEG
                        img.convert("RGB").save(ruta_completa_salida, "JPEG")
                        print(f"{nombre_archivo} se ha convertido a JPEG y guardado en {ruta_completa_salida}.")
            except Exception as e:
                print(f"No se pudo procesar {nombre_archivo}: {e}")

# Ejemplo de uso
ruta_entrada = "C:/Users/Usuario/Desktop/redimensionador de imagenes/redimensionadas"
ruta_salida = "C:/Users/Usuario/Desktop/redimensionador de imagenes/formateadas"
convertir_a_jpeg(ruta_entrada, ruta_salida)
