import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from WantedScrapper import WantedScrapper
'''
  Add data(dict) to Firestore Database(NoSQL) from scrapped data using by WantedScrapper.py

'''

class Firestore_():

  def __init__(self, url = None):

    self.url = url

    cred = credentials.Certificate('C:/Users/jg020/Desktop/aib/CP1/cp1/src/conductive-coil-351110-firebase-adminsdk-1is5w-ca0cdf61e0.json')
    firebase_admin.initialize_app(cred, {
      'projectId': 'conductive-coil-351110',
    })
    self.db = firestore.client()

  
  def push_data(self):

    scrapper = WantedScrapper()
    pagelist = scrapper.get_pagelist(scrapper.url)
    clist = []

    for i in pagelist:
        
        clist.append(scrapper.get_info(i))

    for data in clist:
        
        self.db.collection(u'wanted').document().set(data)

  def pull_data(self):

    data = self.db.collection(u'wanted')

    dics = data.stream()

    clist = {}

    counter = 0

    for dic in dics:

      clist[counter] = dic.to_dict()
      counter += 1

    return clist

# firestore = Firestore_()

# company_list = firestore.pull_data()

# print('~')