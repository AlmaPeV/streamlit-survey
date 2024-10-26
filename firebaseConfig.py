import firebase_admin
from firebase_admin import credentials, firestore

# Configurar Firebase
def init_firebase():
    cred = credentials.Certificate(import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred))  # Reemplaza esta ruta con la ruta de tu archivo JSON
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db
