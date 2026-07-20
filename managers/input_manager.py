import pygame


class InputManager:

    def __init__(self):
        self.comandos_presionar = {}

        self.comandos_mantener = {}
        self.comandos_soltar = {}

        self.teclas_presionadas = set()


    def registrar_jugador(self, jugador):

        if jugador not in self.comandos_presionar:

            self.comandos_presionar[jugador] = {}
            self.comandos_mantener[jugador] = {}
            self.comandos_soltar[jugador] = {}


    def registrar_comando_presionar(
        self,
        jugador,
        tecla,
        comando
    ):

        self.registrar_jugador(jugador)
        self.comandos_presionar[jugador][tecla] = comando



    def registrar_comando_mantener(
        self,
        jugador,
        tecla,
        comando
    ):

        self.registrar_jugador(jugador)
        self.comandos_mantener[jugador][tecla] = comando



    def registrar_comando_soltar(
        self,
        jugador,
        tecla,
        comando
    ):

        self.registrar_jugador(jugador)
        self.comandos_soltar[jugador][tecla] = comando



    def manejar_evento(self, evento):

        if evento.type == pygame.KEYDOWN:
            self.teclas_presionadas.add(
                evento.key
            )

            for comandos in self.comandos_presionar.values():
                comando = comandos.get(
                    evento.key
                )
                if comando:
                    comando.execute()



        elif evento.type == pygame.KEYUP:

            self.teclas_presionadas.discard(
                evento.key
            )

            for comandos in self.comandos_soltar.values():
                comando = comandos.get(
                    evento.key
                )
                if comando:
                    comando.execute()



    def actualizar(self):

        for tecla in self.teclas_presionadas:
            for comandos in self.comandos_mantener.values():
                comando = comandos.get(tecla)
                if comando:
                    comando.execute()