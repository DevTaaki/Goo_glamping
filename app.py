from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import  certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.xsuuq.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():


    return render_template('index.html')


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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
