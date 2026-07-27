import pygame
class SoundManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(
                SoundManager, cls
            ).__new__(cls)

            cls._instance.initialized = False

        return cls._instance


    def __init__(self):

        if self.initialized:
            return

        self.volume = 0.5
        self.sound_volume = 1.0
        self.music_on = True

        self.sounds = []

        pygame.mixer.init()

        self.initialized = True


    def play_music(self, path):

        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(
            self.volume
        )
        pygame.mixer.music.play(-1)

    def toggle_music(self):
        self.music_on = not self.music_on
        if self.music_on:
            pygame.mixer.music.set_volume(
                self.volume
            )
            for sound in self.sounds:
                sound.set_volume(
                    self.volume
                )

        else:
            pygame.mixer.music.set_volume(0)
            for sound in self.sounds:
                sound.set_volume(0)

    def volume_up(self):
        self.volume += 0.1

        if self.volume > 1:
            self.volume = 1

        self.update_volume()


    def volume_down(self):

        self.volume = round(self.volume - 0.1, 2)

        if self.volume < 0:
            self.volume = 0

        self.update_volume()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
        self.volume = volume

    def get_volume(self):
        return self.volume

    def is_music_on(self):
        return self.music_on

    def change_music(self, path, fade_time=1000):
        pygame.mixer.music.fadeout(
            fade_time
        )
        pygame.time.delay(
            fade_time
        )
        pygame.mixer.music.load(
            path
        )
        pygame.mixer.music.set_volume(
            self.volume
        )
        pygame.mixer.music.play(-1)

    def play_sound(self, sound):
        sound.set_volume(
            self.sound_volume
        )
        sound.play()

    def play_sound_loop(self, sound):
        sound.set_volume(
            self.volume
        )

        sound.play(-1)

    def stop_sound(self, sound):
        sound.stop()

    def update_volume(self):
        pygame.mixer.music.set_volume(
        self.volume)

        for sound in self.sounds:
            sound.set_volume(
                self.volume
            )

    def register_sound(self, sound):
        self.sounds.append(sound)