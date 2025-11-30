import streamlit as st
from dataset import cargar_temas, cargar_palabras
from game_logic import crear_ronda

st.set_page_config(page_title="Juego del Impostor", page_icon="🎭")

# Estado inicial
if "ronda" not in st.session_state:
    st.session_state.ronda = None
    st.session_state.jugador = 1

st.title("🎭 Juego del Impostor")

# ---------- selección de temática ----------
temas = cargar_temas()
tema_seleccionado = st.selectbox("Elegí una temática:", temas)

# ---------- número de jugadores ----------
num_jugadores = st.number_input(
    "Número de jugadores:", min_value=3, step=1, value=3
)

# ---------- botón para iniciar nueva ronda ----------
if st.button("Nueva ronda"):
    palabras = cargar_palabras(tema_seleccionado)
    st.session_state.ronda = crear_ronda(palabras, num_jugadores)
    st.session_state.jugador = 1

# ---------- lógica de la ronda ----------
if st.session_state.ronda:
    jugador = st.session_state.jugador
    st.subheader(f"Jugador {jugador}")

    if st.button("Mostrar palabra"):
        palabra = st.session_state.ronda["palabras"][jugador - 1]
        st.success(f"Tu palabra es: {palabra}")

    if st.button("Siguiente jugador"):
        st.session_state.jugador += 1
        if st.session_state.jugador > num_jugadores:
            st.info("¡Todos vieron su palabra! Hablen entre ustedes 😈")
        # no hace falta hacer nada más: el estado ya quedó actualizado
else:
    st.write("Iniciá una ronda para empezar 🔽")
