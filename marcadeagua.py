from PIL import Image, ImageDraw, ImageFont
import os

def agregar_marca_agua(carpeta_origen, texto_marca_agua, carpeta_destino="marcadas"):
    # Crear carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    
    # Recorrer todos los archivos en la carpeta de origen
    for archivo in os.listdir(carpeta_origen):
        # Verificar si el archivo es una imagen
        if archivo.lower().endswith((".jpg", ".jpeg", ".png", '.webp')):
            # Abrir la imagen
            ruta_imagen = os.path.join(carpeta_origen, archivo)
            with Image.open(ruta_imagen).convert("RGBA") as imagen:
                ancho, alto = imagen.size

                # Crear una imagen temporal para la marca de agua
                marca_agua_temp = Image.new("RGBA", (ancho, alto), (255, 255, 255, 0))
                draw_temp = ImageDraw.Draw(marca_agua_temp)

                # Definir la fuente y el tamaño
                font_size = int(alto / 10)  # Tamaño relativo al alto de la imagen
                font = ImageFont.truetype("arial.ttf", font_size)

                # Obtener el tamaño del texto utilizando textbbox
                bbox = draw_temp.textbbox((0, 0), texto_marca_agua, font=font)
                texto_ancho = bbox[2] - bbox[0]
                texto_alto = bbox[3] - bbox[1]

                # Crear una imagen del texto de la marca de agua con espacio adicional
                espacio_extra = 50  # Espacio adicional para evitar cortes
                texto_imagen = Image.new("RGBA", (texto_ancho + espacio_extra, texto_alto + espacio_extra), (255, 255, 255, 0))
                texto_draw = ImageDraw.Draw(texto_imagen)

                # Dibujar el texto en el centro de la imagen de marca de agua
                texto_draw.text((espacio_extra // 2, espacio_extra // 2), texto_marca_agua, fill=(255, 255, 255, 128), font=font)

                # Rotar la imagen del texto
                texto_imagen = texto_imagen.rotate(45, expand=True)

                # Calcular la posición para centrar el texto rotado en la imagen principal
                posicion = ((ancho - texto_imagen.width) // 2, (alto - texto_imagen.height) // 2)

                # Superponer la marca de agua rotada en la imagen principal
                marca_agua_temp.paste(texto_imagen, posicion, texto_imagen)

                # Combinar la marca de agua con la imagen original
                imagen_marcada = Image.alpha_composite(imagen, marca_agua_temp).convert("RGB")

                # Guardar la imagen en la carpeta de destino
                ruta_guardado = os.path.join(carpeta_destino, archivo)
                imagen_marcada.save(ruta_guardado)

    print("Marca de agua añadida a todas las imágenes en la carpeta.")

# Uso del script
carpeta_origen = 'C:/Users/Usuario/Desktop/indumentaria/conjuntos/cortos'
texto_marca_agua = "flashbackstore.com.ar"
agregar_marca_agua(carpeta_origen, texto_marca_agua)
