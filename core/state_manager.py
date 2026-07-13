
class StateManager:
    """Administra el estado actual del juego"""
    def __init__(self):
        self.current_state=None
    def set_state(self,state):
        """Cambia el estado actual"""
        self.current_state=state
    def handle_events(self,events):
        """Envia los eventos al estado actual"""
        if self.current_state:
            self.current_state.handle_events(events)
    def update(self):
        """Actualiza el estado actual"""
        if self.current_state:
            self.current_state.update()
    def draw(self,screen):
        """Dibuja el estado actual"""
        if self.current_state:
            self.current_state.draw(screen)
