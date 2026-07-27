from database.connection import DatabaseConnection

class TournamentRepository:
    def __init__(self):
        self.connection = (
            DatabaseConnection.get_connection()
        )


    def crear_torneo(self, jugador1, jugador2 ):
        cursor = self.connection.cursor()

        sql = """
        INSERT INTO torneo
        (
            jugador1,
            jugador2,
            victorias_jugador1,
            victorias_jugador2,
            ronda_actual,
            estado
        )
        VALUES
        (
            %s,
            %s,
            0,
            0,
            1,
            'EN_CURSO'
        )
        """
        cursor.execute(
            sql,
            (
                jugador1,
                jugador2
            ))

        self.connection.commit()
        cursor.close()
        return cursor.lastrowid

    def obtener_torneo(self):
        cursor = self.connection.cursor(
            dictionary=True
        )

        cursor.execute(
            """
            SELECT *
            FROM torneo
            WHERE estado = 'EN_CURSO'
            LIMIT 1
            """
        )
        torneo = cursor.fetchone()
        cursor.close()
        return torneo

    def actualizar_torneo(self, id_torneo, victorias_jugador1, victorias_jugador2, ronda_actual, estado):
        cursor = self.connection.cursor()
        sql = """
        UPDATE torneo

        SET
            victorias_jugador1 = %s,
            victorias_jugador2 = %s,
            ronda_actual = %s,
            estado = %s

        WHERE id = %s
        """
        cursor.execute(
            sql,
            (
                victorias_jugador1,
                victorias_jugador2,
                ronda_actual,
                estado,
                id_torneo
            ))
        self.connection.commit()
        cursor.close()

    def finalizar_torneo(self, id_torneo):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            UPDATE torneo
            SET estado = 'FINALIZADO'
            WHERE id = %s
            """,
            (
                id_torneo,
            ))
        self.connection.commit()
        cursor.close()


    def eliminar_torneo(self, id_torneo):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            DELETE FROM torneo
            WHERE id = %s
            """,
            (
                id_torneo,
            ))

        self.connection.commit()
        cursor.close()