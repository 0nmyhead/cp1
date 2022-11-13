import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from WantedScrapper import WantedScrapper
import time
'''
  Add data(dict) to Firestore Database(NoSQL) from scrapped data using by WantedScrapper.py

'''

class Firestore_():

  def __init__(self, url = None):

    self.url = url

    cred = credentials.Certificate('conductive-coil-351110-firebase-adminsdk-1is5w-ca0cdf61e0.json')
    firebase_admin.initialize_app(cred, {
      'projectId': 'conductive-coil-351110',
    })
    self.db = firestore.client()

  
  def push_data(self):

    scrapper = WantedScrapper()
    pagelist = scrapper.get_pagelist(scrapper.url)
    clist = []

    timenow = time.strftime('%Y-%m-%d', time.localtime())

    for i in pagelist:
        
        clist.append(scrapper.get_info(i))

    for data in clist:
        
        self.db.collection(timenow).document().set(data)
    
    return timenow

  def pull_data(self, name_col = 'wanted'):

    data = self.db.collection(name_col)

    dics = data.stream()

    clist = {}

    counter = 0

    for dic in dics:

      clist[counter] = dic.to_dict()
      counter += 1

    return clist