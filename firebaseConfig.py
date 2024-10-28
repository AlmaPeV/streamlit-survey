import firebase_admin
from firebase_admin import credentials, firestore

def init_firebase():
    # Usa la ruta al archivo de credenciales de Firebase
    cred = credentials.Certificate("path_to_your_firebase_credentials.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()
