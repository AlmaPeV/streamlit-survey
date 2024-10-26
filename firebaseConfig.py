import firebase_admin
from firebase_admin import credentials, firestore

# Configurar Firebase
def init_firebase():
    cred = credentials.Certificate("C:\Users\Z20100\Downloads\maxdiff-a1891-firebase-adminsdk-enu7i-6a840fda73.json")  # Reemplaza esta ruta con la ruta de tu archivo JSON
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db
