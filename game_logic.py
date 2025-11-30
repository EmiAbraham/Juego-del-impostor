#Logica del juego 

# game_logic.py
import random

def crear_ronda(equipos: list[str], num_jugadores: int) -> dict:
    """
    Crea una ronda del juego:
    - Elige equipo real y equipo del impostor.
    - Elige qué jugador es el impostor.
    - Asigna una palabra (equipo) a cada jugador.
    """
    if num_jugadores < 3:
        raise ValueError("Se necesitan al menos 3 jugadores.")
    if len(equipos) < 2:
        raise ValueError("Se necesitan al menos 2 equipos distintos.")

    # Elegimos dos equipos distintos
    equipo_real, equipo_impostor = random.sample(equipos, 2)

    # Elegimos impostor (jugador 1..num_jugadores)
    impostor = random.randint(1, num_jugadores)

    # Asignamos palabra a cada jugador
    palabras = []
    for jugador in range(1, num_jugadores + 1):
        if jugador == impostor:
            palabras.append("IMPOSTOR")
        else:
            palabras.append(equipo_real)

    return {
        "equipo_real": equipo_real,
        "equipo_impostor": equipo_impostor,
        "impostor": impostor,
        "palabras": palabras,  # lista en orden: jugador 1, 2, 3...
    }
