import streamlit as st
import random

# Lista de muestras
samples = ["Sample 1", "Sample 2", "Sample 3", "Sample 4", "Sample 5",
           "Sample 6", "Sample 7", "Sample 8", "Sample 9", "Sample 10"]

# Inicializar variables de sesión
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'survey_started' not in st.session_state:
    st.session_state.survey_started = False
if 'survey_completed' not in st.session_state:
    st.session_state.survey_completed = False
if 'round_number' not in st.session_state:
    st.session_state.round_number = 1
if 'remaining_samples' not in st.session_state:
    st.session_state.remaining_samples = samples.copy()
if 'selected_sample' not in st.session_state:
    st.session_state.selected_sample = None
if 'rounds_info' not in st.session_state:
    st.session_state.rounds_info = []

# Función para manejar la encuesta
def conduct_survey():
    remaining_samples = st.session_state.remaining_samples
    round_number = st.session_state.round_number

    if len(remaining_samples) > 1:
        # Seleccionar dos muestras aleatorias al principio
        if round_number == 1:
            sample_pair = random.sample(remaining_samples, 2)
        else:
            # En las rondas siguientes, mantener la muestra seleccionada y elegir otra al azar
            sample_pair = [st.session_state.selected_sample, random.choice(remaining_samples)]

        st.write(f"Round {round_number}:")
        st.write(f"1: {sample_pair[0]}")
        st.write(f"2: {sample_pair[1]}")

        # Opción de seleccionar entre las dos muestras
        choice = st.radio("Select the sample you like more:", options=['1', '2'], index=0, key=f"round_{round_number}")

        if st.button("Next Round"):
            if choice == '1':
                selected_sample = sample_pair[0]
                remaining_samples.remove(sample_pair[1])  # Remover la no seleccionada
            elif choice == '2':
                selected_sample = sample_pair[1]
                remaining_samples.remove(sample_pair[0])  # Remover la no seleccionada

            # Guardar el historial de las rondas
            st.session_state.rounds_info.append({
                'round': round_number,
                'appeared_samples': sample_pair,
                'selected_sample': selected_sample
            })

            st.session_state.selected_sample = selected_sample
            st.session_state.remaining_samples = remaining_samples
            st.session_state.round_number += 1
    else:
        # Terminar la encuesta cuando queden una o ninguna muestra
        st.session_state.survey_completed = True

# Inicializar la app de Streamlit
st.title("Sample Preference Survey")

# Sección de autenticación para el panel de administración
password = st.text_input("Enter password to access the admin panel:", type='password')
if password == '0103':
    st.session_state.authenticated = True
    st.success("Access granted")
elif password != '':
    st.error("Invalid password")

# Panel de administración
if st.session_state.authenticated:
    st.subheader("Admin Panel")
    st.write("Real-time survey results:")
    if 'rounds_info' in st.session_state:
        for info in st.session_state.rounds_info:
            st.write(f"Round {info['round']}: Appeared Samples: {info['appeared_samples']}, Selected Sample: {info['selected_sample']}")

# Sección de encuesta
if not st.session_state.survey_completed:
    if not st.session_state.survey_started:
        participant_name = st.text_input("Enter your name or code to start the survey:")
        if participant_name and st.button("Start Survey"):
            st.session_state.participant_name = participant_name
            st.session_state.survey_started = True
            conduct_survey()  # Iniciar la encuesta
    else:
        conduct_survey()  # Continuar con la encuesta en progreso

# Mostrar botón para terminar la encuesta
if st.session_state.survey_completed:
    st.write("Survey completed. Here are your results:")
    for info in st.session_state.rounds_info:
        st.write(f"Round {info['round']}: Appeared Samples: {info['appeared_samples']}, Selected Sample: {info['selected_sample']}")

    if st.button("Finish Survey"):
        st.write("Thank you for participating!")
