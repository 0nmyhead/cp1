from flask import Flask
from firebase_conn import Firestore_
app = Flask(__name__)

#한글 깨짐 방지
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def publish():

    firestore_ = Firestore_()

    data = firestore_.pull_data()

    return data

if __name__ == "__main__":
    app.run()