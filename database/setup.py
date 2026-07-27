from database.connection import DatabaseConnection

class DatabaseSetup:
    @staticmethod
    def create_tables():
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS torneo (

                id INT AUTO_INCREMENT PRIMARY KEY,

                jugador1 VARCHAR(50) NOT NULL,

                jugador2 VARCHAR(50) NOT NULL,

                victorias_jugador1 TINYINT DEFAULT 0,

                victorias_jugador2 TINYINT DEFAULT 0,

                ronda_actual TINYINT DEFAULT 1,

                estado ENUM(
                    'EN_CURSO',
                    'FINALIZADO'
                )
                DEFAULT 'EN_CURSO'

            )
            """
        )

        connection.commit()
        cursor.close()
        connection.close()