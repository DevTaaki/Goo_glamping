from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import  certifi
import datetime
import hashlib
import jwt

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.xsuuq.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


# @app.route("/", methods=[""])
# def ():
#
#
#     sample_receive = request.form['']
#     return jsonify({'': ''})

# doc = {
#        데이터
#     }
#
#     db.(각자 필요한 폴더 이름).insert_one(doc)


#####로그인 #######
@app.route('/sign_in', methods=['POST'])
def sign_in():
    id_receive = request.form['give_id']
    pw_receive = request.form['give_pw']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.users.find_one({'user_id': id_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
        'id': id_receive,
        'exp': datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
