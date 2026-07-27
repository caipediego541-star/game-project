from patterns.repository.tournament_repository import TournamentRepository


repo = TournamentRepository()


repo.crear_torneo(
    "BELEN",
    "PROFE"
)


torneo = repo.obtener_torneo()

print("ANTES:")
print(torneo)


repo.actualizar_torneo(
    torneo["id"],
    1,
    0,
    2,
    "EN_CURSO"
)


torneo = repo.obtener_torneo()

print("DESPUES:")
print(torneo)


repo.eliminar_torneo()


print("TORNEO ELIMINADO")