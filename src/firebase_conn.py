import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred, {
  'projectId': 'conductive-coil-351110',
})

db = firestore.client()