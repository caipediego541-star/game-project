import pygame
from patterns.state.stateBase import State
from patterns.factory.button_factory import ButtonFactory
from utils.helpers import scale_image



class OptionsState(State):

    def __init__(self, game):

        self.game = game
        self.background = self.game.resource_manager.get_image("menu_background")
        self.buttons = []
        self.music_on = True
        self.volume = 50
        self.message = ""
        self.message_timer = 0
        #musica
        imagen_musica = self.game.resource_manager.get_image("boton_musica")
        imagen_musica = pygame.transform.scale_by(imagen_musica, 0.4)
        self.button_musica = ButtonFactory.create_button(
            image=imagen_musica,
            x=260,
            y=80,
            action=self.toggle_music
        )
        self.buttons.append(self.button_musica)
        #volumen +
        imagen_volumen_mas = self.game.resource_manager.get_image("boton_volumen_mas")
        imagen_volumen_mas = pygame.transform.scale_by(imagen_volumen_mas, 0.4)
        self.button_volumen_mas = ButtonFactory.create_button(
            image=imagen_volumen_mas,
            x=260,
            y=230,
            action=self.volume_up
        )
        self.buttons.append(self.button_volumen_mas)
        #volumen -
        imagen_volumen_menos = self.game.resource_manager.get_image("boton_volumen_menos")
        imagen_volumen_menos = pygame.transform.scale_by(imagen_volumen_menos, 0.4)
        self.button_volumen_menos = ButtonFactory.create_button(
            image=imagen_volumen_menos,
            x=260,
            y=380,
            action=self.volume_down
        )
        self.buttons.append(self.button_volumen_menos)
        # Volver
        imagen_volver = self.game.resource_manager.get_image("boton_volver")
        imagen_volver = pygame.transform.scale_by(imagen_volver, 0.33)
        self.button_volver = ButtonFactory.create_button(
            image=imagen_volver,
            x=260,
            y=530,
            action=self.go_back
        )
        self.buttons.append(self.button_volver)

       

    def handle_events(self, events):

        for event in events:

            if event.type == pygame.QUIT:
                self.game.running = False

            for button in self.buttons:
                button.handle_event(event)


    def update(self):
        pass


    def draw(self, screen):

        fondo = scale_image(self.background, screen)
        x = (screen.get_width() - fondo.get_width()) // 2
        y = (screen.get_height() - fondo.get_height()) // 2

        screen.blit(fondo, (x, y))
        #dibujar botones
        for button in self.buttons:
            button.draw(screen)
        #mostrar mensaje musica
        if self.message_timer > 0:
            font = pygame.font.Font(None, 40)
            text = font.render(self.message, True, (255,255,0))
            screen.blit(text, (560, 250))
            self.message_timer -= 1


    def toggle_music(self):
        self.music_on = not self.music_on
        if self.music_on:
            pygame.mixer.music.unpause()
            self.message = "MÚSICA ACTIVADA"
        else:
            pygame.mixer.music.pause()
            self.message = "MÚSICA DESACTIVADA"
        self.message_timer = 120

    def volume_up(self):
        self.volume += 10
        if self.volume > 100:
            self.volume = 100
        pygame.mixer.music.set_volume(self.volume / 100)
        self.message = f"VOLUMEN: {self.volume} %"
        self.message_timer = 120

    def volume_down(self):
        self.volume -= 10
        if self.volume < 0:
            self.volume = 0
        pygame.mixer.music.set_volume(self.volume / 100)
        self.message = f"VOLUMEN: {self.volume} %"
        self.message_timer = 120

    def go_back(self):
        print("VOLVER")
        from patterns.state.mainMenuState import MainMenuState
        self.game.state_manager.set_state(MainMenuState(self.game))