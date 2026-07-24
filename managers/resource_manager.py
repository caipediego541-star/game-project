import pygame
import os


class ResourceManager:

    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}
        self.animations = {}
        self.characters = {}

    def load_image(self, name, path):
        if name in self.images:
            return self.images[name]

        image = pygame.image.load(
            path
        ).convert_alpha()

        self.images[name] = image
        return image

    def get_image(self, name):
        return self.images.get(
            name
        )

    def load_sound(self, name, path):

        sound = pygame.mixer.Sound(path)

        sound.set_volume(
            0.8
        )

        self.sounds[name] = sound

        return sound

    def get_sound(self, name):
        return self.sounds.get(
            name
        )

    def load_font(self, name, path, size):
        font = pygame.font.Font(
            path,
            size
        )
        self.fonts[name] = font
        return font

    def get_font(self, name):
        return self.fonts.get(
            name
        )

    def load_animation(self, name, folder):
        if name in self.animations:
            return self.animations[name]

        frames = []
        files = sorted(
            os.listdir(folder)
        )

        for file in files:
            if file.endswith(".png"):
                path = os.path.join(
                    folder,
                    file
                )

                image = pygame.image.load(
                    path
                ).convert_alpha()

                frames.append(
                    image
                )

        self.animations[name] = frames
        return frames

    def get_animation(self, name):
        return self.animations.get(
            name
        )

    def load_character(self, character_name):
        if character_name in self.characters:
            return self.characters[character_name]

        base_path = os.path.join(
            "assets",
            "images",
            "personajes",
            character_name
        )

        animations = {}
        for animation in os.listdir(base_path):
            animation_path = os.path.join(
                base_path,
                animation
            )

            if os.path.isdir(animation_path):

                animations[animation] = self.load_animation(
                    f"{character_name}_{animation}",
                    animation_path
                )

        self.characters[character_name] = animations
        return animations