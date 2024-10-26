import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import random
import firebase_admin
from firebase_admin import credentials, firestore

# Descargar el archivo JSON de Firebase Console y colocar la ruta del archivo aquí
cred = credentials.Certificate("ruta/a/tu/archivo-de-credenciales.json")

# Inicializar la aplicación de Firebase con las credenciales
firebase_admin.initialize_app(cred)

# Inicializar Firestore
db = firestore.client()


# Inicializar Firebase
cred = credentials.Certificate("path_to_your_firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Lista de muestras
samples = ["Sample 1", "Sample 2", "Sample 3", "Sample 4", "Sample 5",
           "Sample 6", "Sample 7", "Sample 8", "Sample 9", "Sample 10"]

# Función para actualizar y leer datos desde Firestore
def save_to_firestore(collection, doc_id, data):
    db.collection(collection).document(doc_id).set(data)

def get_from_firestore(collection, doc_id):
    return db.collection(collection).document(doc_id).get().to_dict()

# Función para manejar la encuesta
def conduct_survey(user_id):
    round_number = st.session_state.round_number

    # Si estamos en una ronda válida
    if round_number <= 9:
        if not st.session_state.current_pair:
            if round_number == 1:
                st.session_state.current_pair = random.sample(st.session_state.remaining_samples, 2)
            else:
                new_sample = random.choice([sample for sample in st.session_state.remaining_samples if sample != st.session_state.current_sample])
                st.session_state.current_pair = [st.session_state.current_sample, new_sample]

        st.write(f"Round {round_number}:")
        st.write(f"1: {st.session_state.current_pair[0]}")
        st.write(f"2: {st.session_state.current_pair[1]}")

        choice = st.radio("Select the sample you like more:",
                          options=['1', '2'], index=0,
                          key=f"radio_{round_number}")

        if st.button("Next Round", key=f"next_button_{round_number}"):
            selected_sample = st.session_state.current_pair[int(choice)-1]
            st.session_state.current_sample = selected_sample

            # Guardar selección en Firestore
            save_to_firestore('survey_data', user_id, {
                'round': round_number,
                'appeared_samples': st.session_state.current_pair,
                'selected_sample': selected_sample
            })

            st.session_state.selected_samples.append(selected_sample)
            remaining_sample = st.session_state.current_pair[1] if selected_sample == st.session_state.current_pair[0] else st.session_state.current_pair[0]
            st.session_state.remaining_samples.remove(remaining_sample)
            st.session_state.round_number += 1
            st.session_state.current_pair = []

            return
    else:
        st.session_state.survey_completed = True

# Panel de administración
def admin_panel():
    st.subheader("Admin Panel - Real-time Results")
    users = db.collection('survey_data').stream()
    for user in users:
        st.write(f"User: {user.id}, Data: {user.to_dict()}")

# Interfaz de usuario
st.title("Sample Preference Survey")

# Identificar al usuario
user_id = st.text_input("Enter your unique ID (or name):")

if st.button("Start Survey") and user_id:
    conduct_survey(user_id)

# Sección del administrador (solo accesible con contraseña)
password = st.text_input("Enter admin password:", type='password')
if password == 'admin123':
    admin_panel()
