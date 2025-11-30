# gui.py
import tkinter as tk
from tkinter import messagebox

from dataset import cargar_equipos
from game_logic import crear_ronda


class JuegoImpostorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Impostor NBA 🏀")

        # Cargamos equipos
        self.equipos = cargar_equipos()

        # Estado de la ronda
        self.ronda = None
        self.jugador_actual = 0
        self.num_jugadores = 0

        # --- Widgets ---
        tk.Label(root, text="Número de jugadores (mínimo 3):").pack(pady=5)

        self.entry_jugadores = tk.Entry(root, width=10, justify="center")
        self.entry_jugadores.insert(0, "3")
        self.entry_jugadores.pack(pady=5)

        self.btn_nueva_ronda = tk.Button(
            root, text="Nueva ronda", command=self.nueva_ronda
        )
        self.btn_nueva_ronda.pack(pady=10)

        self.label_jugador = tk.Label(root, text="Jugador actual: -")
        self.label_jugador.pack(pady=5)

        self.label_palabra = tk.Label(
            root, text="Presioná 'Mostrar palabra' para ver tu palabra", font=("Arial", 12, "bold")
        )
        self.label_palabra.pack(pady=10)

        self.btn_mostrar = tk.Button(
            root, text="Mostrar palabra", command=self.mostrar_palabra, state="disabled"
        )
        self.btn_mostrar.pack(pady=5)

        self.btn_siguiente = tk.Button(
            root, text="Siguiente jugador", command=self.siguiente_jugador, state="disabled"
        )
        self.btn_siguiente.pack(pady=5)

        self.label_info = tk.Label(root, text="")
        self.label_info.pack(pady=10)

    def nueva_ronda(self):
        try:
            n = int(self.entry_jugadores.get())
            if n < 3:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresá un número de jugadores válido (mínimo 3).")
            return

        self.num_jugadores = n
        self.ronda = crear_ronda(self.equipos, n)
        self.jugador_actual = 1

        self.label_jugador.config(text=f"Jugador actual: {self.jugador_actual}")
        self.label_palabra.config(text="Presioná 'Mostrar palabra' para ver tu palabra")
        self.label_info.config(text="")

        self.btn_mostrar.config(state="normal")
        self.btn_siguiente.config(state="disabled")

    def mostrar_palabra(self):
        if not self.ronda:
            return

        palabra = self.ronda["palabras"][self.jugador_actual - 1]
        self.label_palabra.config(text=f"Tu palabra es: {palabra}")
        # Luego de mostrar, habilitamos avanzar
        self.btn_siguiente.config(state="normal")
        self.btn_mostrar.config(state="disabled")

    def siguiente_jugador(self):
        if self.jugador_actual >= self.num_jugadores:
            # Terminó la ronda
            self.label_jugador.config(text="Ronda terminada")
            self.label_palabra.config(
                text="Ahora hablen entre ustedes y voten al impostor 😈"
            )
         
            self.btn_mostrar.config(state="disabled")
            self.btn_siguiente.config(state="disabled")
            return

        # Pasamos al siguiente jugador
        self.jugador_actual += 1
        self.label_jugador.config(text=f"Jugador actual: {self.jugador_actual}")
        self.label_palabra.config(text="Presioná 'Mostrar palabra' para ver tu palabra")

        self.btn_mostrar.config(state="normal")
        self.btn_siguiente.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoImpostorGUI(root)
    root.mainloop()
