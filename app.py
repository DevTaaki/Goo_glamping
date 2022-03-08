from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.xsuuq.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/review_list', method=["POST"])
def review_post():
    title_receive = request.form['title_give']
    address_receive = request.form['address_give']
    star_receive = request.form['star_receive']
    review_receive = request.form['review_give']

    doc = {
        'title': title_receive,
        'star': star_receive,
        
    }

    return jsonify({'msg':'POST 연결 완료!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
