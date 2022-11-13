from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'