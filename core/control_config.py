import pygame

from patterns.command.player.move_left import MoveLeftCommand
from patterns.command.player.move_right import MoveRightCommand
from patterns.command.player.move_jump import JumpCommand
from patterns.command.player.punch import PunchCommand
from patterns.command.player.kick import KickCommand
from patterns.command.player.block import BlockCommand
from patterns.command.player.stop_block import StopBlockCommand
from patterns.command.player.stop_move import StopMoveCommand


class ControlsConfig:


    @staticmethod
    def configurar_jugador1(input_manager, player):

        input_manager.registrar_jugador(
            "jugador1"
        )

        input_manager.registrar_comando_mantener(
            "jugador1",
            pygame.K_a,
            MoveLeftCommand(player)
        )

        input_manager.registrar_comando_mantener(
            "jugador1",
            pygame.K_d,
            MoveRightCommand(player)
        )

        input_manager.registrar_comando_presionar(
            "jugador1",
            pygame.K_w,
            JumpCommand(player)
        )

        input_manager.registrar_comando_presionar(
            "jugador1",
            pygame.K_f,
            PunchCommand(player)
        )

        input_manager.registrar_comando_presionar(
            "jugador1",
            pygame.K_g,
            KickCommand(player)
        )

        input_manager.registrar_comando_presionar(
            "jugador1",
            pygame.K_h,
            BlockCommand(player)
        )

        input_manager.registrar_comando_soltar(
            "jugador1",
            pygame.K_h,
            StopBlockCommand(player)
        )

        input_manager.registrar_comando_soltar(
            "jugador1",
            pygame.K_a,
            StopMoveCommand(player)
        )


        input_manager.registrar_comando_soltar(
            "jugador1",
            pygame.K_d,
            StopMoveCommand(player)
        )



    @staticmethod
    def configurar_jugador2(input_manager, player):

        input_manager.registrar_jugador(
            "jugador2"
        )

        input_manager.registrar_comando_mantener(
            "jugador2",
            pygame.K_LEFT,
            MoveLeftCommand(player)
        )

        input_manager.registrar_comando_mantener(
            "jugador2",
            pygame.K_RIGHT,
            MoveRightCommand(player)
        )

        input_manager.registrar_comando_presionar(
            "jugador2",
            pygame.K_UP,
            JumpCommand(player)
        )

        input_manager.registrar_comando_presionar(
            "jugador2",
            pygame.K_j,
            PunchCommand(player)
        )

        input_manager.registrar_comando_presionar(
            "jugador2",
            pygame.K_k,
            KickCommand(player)
        )

        input_manager.registrar_comando_presionar(
            "jugador2",
            pygame.K_l,
            BlockCommand(player)
        )

        input_manager.registrar_comando_soltar(
            "jugador2",
            pygame.K_l,
            StopBlockCommand(player)
        )

        input_manager.registrar_comando_soltar(
            "jugador2",
            pygame.K_LEFT,
            StopMoveCommand(player)
        )

        input_manager.registrar_comando_soltar(
            "jugador2",
            pygame.K_RIGHT,
            StopMoveCommand(player)
        )