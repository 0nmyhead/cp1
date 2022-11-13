import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
'''

  get raw data(dict) from firestore database

'''


cred = credentials.Certificate('./conductive-coil-351110-firebase-adminsdk-1is5w-ca0cdf61e0.json')
firebase_admin.initialize_app(cred, {
  'projectId': 'conductive-coil-351110',
})

db = firestore.client()

data = db.collection(u'wanted')

dics = data.stream()

for dic in dics:

  print(u'{} => {}'.format(dic.id, dic.to_dict()))