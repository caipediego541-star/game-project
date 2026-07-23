class StateManager:

    def __init__(self):
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
        if self.current_state:
            self.current_state.handle_events(events)


    def update(self):
        if self.current_state:
            self.current_state.update()


    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)