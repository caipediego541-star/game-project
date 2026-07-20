from config import PROPORCION_PISO
class Stage():
    def __init__(self, alto, ancho):
        self.alto= alto
        self.ancho= ancho

    @property
    def piso_y(self):
        return self.alto - (self.alto * PROPORCION_PISO)
    

