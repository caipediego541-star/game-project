class StateManager:

    def __init__(self):
<<<<<<< HEAD
        self.current_state=None
    def set_state(self,state):
        """Cambia el estado actual"""
        self.current_state = state

        if hasattr(state, "start"):
            state.start(state.game)
    def handle_events(self,events):
        """Envia los eventos al estado actual"""
=======
        self.current_state = None
        self.previous_state = None


    def set_state(self, state):
        if self.current_state:
            self.previous_state = self.current_state
        self.current_state = state
        if hasattr(
            self.current_state,
            "enter"
        ):
            self.current_state.enter()

    def return_previous_state(self):
        if self.previous_state:
            self.current_state = self.previous_state

    def handle_events(self, events):
>>>>>>> 07d51f75fbe74859957961a873a8b0ba5d65deb6
        if self.current_state:
            self.current_state.handle_events(events)


    def update(self):
        if self.current_state:
            self.current_state.update()


    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)