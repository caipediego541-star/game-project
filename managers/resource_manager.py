import pygame
import os

class ResourceManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}
        self.animations= {}

    # Carga de recursos
    def load_image(self, name, path):
        image = pygame.image.load(path).convert_alpha() # convert_alpha() para manejar transparencias
        self.images[name] = image
        return image

    # Obtiene una imagen cargada
    def get_image(self, name):
        return self.images.get(name)

    # Carga de sonidos
    def load_sound(self, name, path):
        sound = pygame.mixer.Sound(path)
        self.sounds[name] = sound
        return sound

    # Obtiene un sonido cargado
    def get_sound(self, name):
        return self.sounds.get(name)

    # Carga de fuentes
    def load_font(self, name, path, size):
        font = pygame.font.Font(path, size)
        self.fonts[name] = font
        return font

    # Obtiene una fuente cargada
    def get_font(self, name):
        return self.fonts.get(name)
    
    # Carga animaciones
    def load_animation(self, name, folder):
        frames = []

        files = sorted(os.listdir(folder))

        for file in files:
            if file.endswith(".png"):
                path = os.path.join(folder, file)

                image = pygame.image.load(path).convert_alpha()

                frames.append(image)

        self.animations[name] = frames

        return frames
    
    # Obtener imagenes
    def get_animation(self, name):
        return self.animations.get(name)
    
    # Cargar personajes
    def load_character(self, character_name):
        base_path = os.path.join(
            "assets",
            "images",
            "personajes",
            character_name
        )

        animations = {}

        for animation in os.listdir(base_path):

            animation_path = os.path.join(base_path, animation)

            if os.path.isdir(animation_path):
                animations[animation] = self.load_animation(
                    f"{character_name}_{animation}",
                    animation_path
                )

        return animations
    