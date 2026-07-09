from config import ANCHO, ALTO, FPS, TITULO
from core.game import Game

def main():
    """
    Función principal del videojuego.
    """
    juego = Game()
    juego.run()
    print("Iniciando el juego...")
    

if __name__ == "__main__":
    main()

