import os

import pymysql.cursors
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# PyMySQLを用いたMySQL接続の設定
db = pymysql.connect(
    host=os.getenv('MYSQL_HOST'),
    port=int(os.getenv('MYSQL_PORT')),
    user=os.getenv('MYSQL_USER'),
    db=os.getenv('MYSQL_DB'),
    password=os.getenv('MYSQL_PASSWORD'),
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()


def db_init():
    # データベースを初期化
    cursor.execute('CREATE DATABASE IF NOT EXISTS yoshiodb')
    cursor.execute('USE yoshiodb')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL AUTO_INCREMENT,
        name CHAR(100) NOT NULL,
        age INT NOT NULL,
        PRIMARY KEY (id)
    )''')
    db.commit()


@app.route('/', methods=['GET'])
def index():
    # クエリ文字列nameから値を取得
    # 値が設定されていない場合はCTFをデフォルトの値とする
    default_name = 'CTF'
    name = request.args.get('name', default_name)
    return render_template('index.html', name=name)


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        # データベースから値を取得
        cursor.execute('SELECT name, age FROM users')
        users = cursor.fetchall()

        return jsonify({
            'users': users
        })
    if request.method == 'POST':
        # データベースにデータを追加
        name = request.json['name']
        age = request.json['age']
        cursor.execute(
            'INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
        db.commit()

        return jsonify({
            'result': 'success',
            'name': name
        })


if __name__ == '__main__':
    db_init()
    app.run(host='0.0.0.0', port=5000)
