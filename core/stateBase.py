class State:
    """ Clase base para todos los estados del juego"""

    def __init__(self, game):
        self.game = game
    def handle_events(self,events):
        """Procesa los eventos del teclado, mouse, entre otros"""
        pass
    def update(self):
        """Actualiza la lógica del estado"""
        pass
    def draw(self,screen):
        """Dibuja los elementos en pantalla"""
        pass

#Utilizamos el pass porque esta clase es un plantilla, entonces las clases hijas (demas estados) heredaran estas funciones
# y colocaran la lógica de cada fucnión segun necesiten.