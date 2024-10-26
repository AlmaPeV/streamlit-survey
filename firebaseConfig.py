import firebase_admin
from firebase_admin import credentials, firestore

# Configurar Firebase
def init_firebase():
    cred = credentials.Certificate("path/to/your-firebase-adminsdk-key.json")  # Reemplaza esta ruta con la ruta de tu archivo JSON
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db
