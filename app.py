import streamlit as st
from dataset import cargar_equipos
from game_logic import crear_ronda

st.set_page_config(page_title="Juego del Impostor NBA", page_icon="🏀")

if "ronda" not in st.session_state:
    st.session_state.ronda = None
    st.session_state.jugador = 1

st.title("🏀 Juego del Impostor NBA")

equipos = cargar_equipos()

num_jugadores = st.number_input("Número de jugadores:", min_value=3, step=1)

if st.button("Nueva ronda"):
    st.session_state.ronda = crear_ronda(equipos, num_jugadores)
    st.session_state.jugador = 1

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
else:
    st.write("Iniciá una ronda para empezar 🔽")
