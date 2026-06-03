import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:

    cred = credentials.Certificate("firebase_key.json")

    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_to_firebase(person_count, status):

    data = {

        "person_count": person_count,

        "status": status,

        "timestamp": firestore.SERVER_TIMESTAMP
    }

    db.collection("attendance").add(data)