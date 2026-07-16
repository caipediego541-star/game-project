from PIL import Image
import os

carpeta = "assets/images/personajes/belen"

for raiz, _, archivos in os.walk(carpeta):
    for archivo in archivos:
        if archivo.lower().endswith(".png"):
            ruta = os.path.join(raiz, archivo)

            imagen = Image.open(ruta)
            imagen = imagen.resize((128, 128), Image.Resampling.LANCZOS)
            imagen.save(ruta)

print("¡Todas las imágenes fueron redimensionadas!")