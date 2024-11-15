from moviepy.editor import VideoFileClip
import os

def resize_video(input_path, output_path, width, height):
    # Cargar el video
    with VideoFileClip(input_path) as video:
        # Redimensionar el video
        video_resized = video.resize(newsize=(width, height))
        # Guardar el video redimensionado en la ubicación de salida
        video_resized.write_videofile(output_path, codec="libx264")
    print(f"Video redimensionado y guardado en {output_path}")

# Ejemplo de uso
input_path = 'C:/Users/Usuario/Desktop/redimensionador de videos/video.mp4'
output_path = 'C:/Users/Usuario/Desktop/redimensionador de videos/video_redimensionado.mp4'
width, height = 1080, 1920  # Cambia las dimensiones según lo que necesites
resize_video(input_path, output_path, width, height)
