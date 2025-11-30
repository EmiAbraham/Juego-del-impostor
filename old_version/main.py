#Proyecto: Juego del impostor    
# main.py
from dataset import cargar_equipos
from game_logic import crear_ronda

def mostrar_palabras_a_jugadores(ronda: dict):
    num_jugadores = len(ronda["palabras"])

    for i in range(num_jugadores):
        jugador = i + 1
        input(f"\n👉 Pasar la compu al JUGADOR {jugador} y presionar ENTER cuando esté listo...")

        palabra = ronda["palabras"][i]
        print(f"Tu equipo es: {palabra}")

        input("Cuando termines de ver tu palabra, presioná ENTER y pasá la compu al siguiente jugador.")
        print("\n" * 40)  # pseudo “limpieza” de pantalla

def main():
    print("🏀 Juego del Impostor NBA")
    equipos = cargar_equipos()

    num_jugadores = int(input("¿Cuántos jugadores son? (mínimo 3): "))

    seguir = "s"
    while seguir.lower() == "s":
        ronda = crear_ronda(equipos, num_jugadores)

        mostrar_palabras_a_jugadores(ronda)

        print("🗣 Ahora hablen entre ustedes y voten quién creen que es el impostor 😈")
        seguir = input("\n¿Quieren jugar otra ronda? (s/n): ")

    print("Gracias por jugar 😎")

if __name__ == "__main__":
    main()
