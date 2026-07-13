import pygame

def scale_image(image, screen):

    ventana_w , ventana_h = screen.get_size()
    img_w, img_h = image.get_size()

    scale= min(ventana_w / img_w, ventana_h / img_h)
    new_size= (int(img_w* scale), int(img_h * scale))

    return pygame.transform.scale(image, new_size)