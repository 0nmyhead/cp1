from flask import Flask
from flask import request
from firestore_conn import Firestore_
import json
app = Flask(__name__)

#한글 깨짐 방지
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods = ['GET'])
def root():

    name_col = request.args.get('name','wanted')

    data = firestore_.pull_data()

    return json.dumps(data, ensure_ascii=False)

@app.route('/update')
def update():

    '''
    
    update firestore database

    '''

    response = ''
    
    response = firestore_.push_data()

    
    return response

if __name__ == "__main__":

    global firestore_
    firestore_ = Firestore_()
    app.run(host='0.0.0.0', port=5000, debug=True)