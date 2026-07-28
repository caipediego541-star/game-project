import pygame

def scale_image(image, screen):

    ventana_w , ventana_h = screen.get_size()
    img_w, img_h = image.get_size()

    scale= min(ventana_w / img_w, ventana_h / img_h)
    new_size= (int(img_w* scale), int(img_h * scale))

    return pygame.transform.scale(image, new_size)

import pygame

def agregar_margen_negro(imagen, margen=5):
    """
    Agrega un borde negro alrededor de una imagen.

    :param imagen: Surface de pygame
    :param margen: tamaño del borde en píxeles
    :return: nueva Surface con borde
    """

    ancho = imagen.get_width() + margen * 2
    alto = imagen.get_height() + margen * 2

    nueva_imagen = pygame.Surface(
        (ancho, alto),
        pygame.SRCALPHA
    )

    # Fondo negro
    pygame.draw.rect(
        nueva_imagen,
        (0, 0, 0),
        (0, 0, ancho, alto)
    )

    # Imagen centrada encima
    nueva_imagen.blit(
        imagen,
        (margen, margen)
    )

    return nueva_imagen

