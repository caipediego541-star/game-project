import sqlite3
import json
import os
from datetime import datetime
 
import pygame
 
 
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tournament_save.db")
 
 
class TournamentSaveManager:
    """Encapsula toda la logica de la base de datos SQLite para el torneo."""
 
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._init_db()
 
    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # id fijo en 1 -> solo guardamos UN torneo en progreso a la vez.
        # Si tu juego necesita varios "slots" de guardado, se puede cambiar
        # esto por un id autoincremental o por perfil de usuario.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tournament_progress (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                players_data TEXT NOT NULL,
                bracket_data TEXT NOT NULL,
                current_round INTEGER NOT NULL,
                current_match_index INTEGER NOT NULL,
                last_updated TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
 
    def has_saved_tournament(self) -> bool:
        """Devuelve True si existe un torneo sin terminar guardado."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tournament_progress WHERE id = 1")
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0
 
    def save_progress(self, players, bracket, current_round, current_match_index):
        """
        Guarda (o sobreescribe) el progreso del torneo actual.
 
        players: lista de dicts, ej:
            [{"name": "Ryu", "wins": 2}, {"name": "Ken", "wins": 1}, ...]
        bracket: estructura que representa los combates restantes/hechos.
            Puede ser una lista de tuplas/dicts, lo que uses en tu logica
            de emparejamientos. Se guarda tal cual como JSON.
        current_round: int, ronda actual del torneo (0, 1, 2...).
        current_match_index: int, indice del combate actual dentro de la ronda.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tournament_progress
                (id, players_data, bracket_data, current_round, current_match_index, last_updated)
            VALUES (1, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                players_data = excluded.players_data,
                bracket_data = excluded.bracket_data,
                current_round = excluded.current_round,
                current_match_index = excluded.current_match_index,
                last_updated = excluded.last_updated
        """, (
            json.dumps(players),
            json.dumps(bracket),
            current_round,
            current_match_index,
            datetime.now().isoformat(),
        ))
        conn.commit()
        conn.close()
 
    def load_progress(self):
        """
        Devuelve un dict con el estado guardado, o None si no hay nada.
        {
            "players": [...],
            "bracket": [...],
            "current_round": int,
            "current_match_index": int
        }
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT players_data, bracket_data, current_round, current_match_index
            FROM tournament_progress WHERE id = 1
        """)
        row = cursor.fetchone()
        conn.close()
 
        if row is None:
            return None
 
        players_json, bracket_json, current_round, current_match_index = row
        return {
            "players": json.loads(players_json),
            "bracket": json.loads(bracket_json),
            "current_round": current_round,
            "current_match_index": current_match_index,
        }
 
    def clear_progress(self):
        """Borra el torneo guardado (usar cuando el torneo termina del todo)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tournament_progress WHERE id = 1")
        conn.commit()
        conn.close()
 
 
def prompt_load_or_new(screen, clock, font=None):
    """
    Muestra una pantalla simple con dos opciones (Cargar / Nuevo) y devuelve
    "load" o "new" segun lo que elija el jugador con flechas + Enter.
 
    Es una pantalla generica pensada para integrarse facil en tu loop de
    pygame ya existente. Podes cambiarle los colores/fuente para que
    combine con el estilo del resto del juego.
    """
    if font is None:
        font = pygame.font.SysFont(None, 40)
    title_font = pygame.font.SysFont(None, 50)
 
    options = ["Cargar torneo guardado", "Empezar torneo nuevo"]
    selected = 0
    waiting = True
 
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    selected = (selected - 1) % len(options)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    waiting = False
 
        screen.fill((20, 20, 20))
 
        title = title_font.render("Se encontro un torneo en progreso", True, (255, 255, 255))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))
 
        for i, option in enumerate(options):
            color = (255, 215, 0) if i == selected else (200, 200, 200)
            text = font.render(option, True, color)
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 220 + i * 60))
 
        hint = font.render("Flechas para elegir, Enter para confirmar", True, (120, 120, 120))
        screen.blit(hint, (screen.get_width() // 2 - hint.get_width() // 2, 400))
 
        pygame.display.flip()
        clock.tick(30)
 
    return "load" if selected == 0 else "new"
 
 
# ---------------------------------------------------------------------------
# EJEMPLO DE INTEGRACION (no es parte del modulo, es solo referencia)
# ---------------------------------------------------------------------------
def ejemplo_entrar_a_modo_torneo(screen, clock):
    """
    Ejemplo de como quedaria la logica al entrar al modo torneo.
    Adaptalo a tus clases/estructuras reales (Player, Bracket, etc).
    """
    save_manager = TournamentSaveManager()
 
    if save_manager.has_saved_tournament():
        choice = prompt_load_or_new(screen, clock)
        if choice == "load":
            data = save_manager.load_progress()
            players = data["players"]           # ej: [{"name": "Ryu", "wins": 2}, ...]
            bracket = data["bracket"]
            current_round = data["current_round"]
            current_match_index = data["current_match_index"]
            # aca reconstruis tu bracket / estado de torneo con estos datos
        else:
            # el jugador eligio "nuevo" -> se borra el guardado viejo
            save_manager.clear_progress()
            players, bracket, current_round, current_match_index = crear_torneo_nuevo()
    else:
        players, bracket, current_round, current_match_index = crear_torneo_nuevo()
 
    return players, bracket, current_round, current_match_index
 
 
def crear_torneo_nuevo():
    """Placeholder: aca va tu logica real de armar el bracket inicial."""
    players = [{"name": "Ryu", "wins": 0}, {"name": "Ken", "wins": 0}]
    bracket = []
    return players, bracket, 0, 0
 
 
def ejemplo_despues_de_cada_combate(save_manager, players, bracket, current_round, current_match_index):
    """
    Llamar esto cada vez que termina un combate (haya ganado quien haya
    ganado) para que el progreso quede persistido por si el jugador
    cierra el juego despues.
    """
    save_manager.save_progress(players, bracket, current_round, current_match_index)
 
 
def ejemplo_manejo_de_salida(save_manager, players, bracket, current_round, current_match_index):
    """
    Llamar esto en el evento pygame.QUIT (o en tu boton de 'salir del
    torneo') para asegurarte de guardar el ultimo estado antes de cerrar.
    """
    save_manager.save_progress(players, bracket, current_round, current_match_index)