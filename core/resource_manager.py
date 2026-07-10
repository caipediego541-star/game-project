import pygame

class ResourceManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}

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