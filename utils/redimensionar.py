from PIL import Image
import os

carpeta = "assets/images/ui"

for raiz, _, archivos in os.walk(carpeta):
    for archivo in archivos:
        if archivo.lower().endswith(".png"):
            ruta = os.path.join(raiz, archivo)

            imagen = Image.open(ruta)
            imagen = imagen.resize((1000, 1200), Image.Resampling.LANCZOS)
            imagen.save(ruta)

print("¡Todas las imágenes fueron redimensionadas!")