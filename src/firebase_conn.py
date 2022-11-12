import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from WantedScrapper import WantedScrapper


scrapper = WantedScrapper()
pagelist = scrapper.get_pagelist(scrapper.url)
clist = []

for i in pagelist:
    
    clist.append(scrapper.get_info(i))

cred = credentials.Certificate('conductive-coil-351110-firebase-adminsdk-1is5w-ca0cdf61e0.json')
firebase_admin.initialize_app(cred, {
  'projectId': 'conductive-coil-351110',
})


db = firestore.client()

for data in clist:
    
    db.collection(u'wanted').document(u'company').set(data)