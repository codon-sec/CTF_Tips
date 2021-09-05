from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

METHODS = ['GET', 'HEAD', 'PUT', 'DELETE',
           'CONNECT', 'OPTIONS', 'TRACE', 'POST']


@app.route('/', defaults={'path': ''}, methods=METHODS)
@app.route('/<path:path>', methods=METHODS)
def index(path):
    '''
    リクエストのRequest-URI, メソッド及びヘッダーの内容をレスポンスする
    '''
    return f'''
    <h1>Path: /{path}</h1>
    <h2>Method: {request.method}</h2>
    <h2>Request Headers</h2>
    <ul>
        {''.join((f'<li>{name}: {value}</li>') for name, value in request.headers)}
    </ul>
    <h2>Request Body</h2>
    <p>{ request.get_data().decode() if request.get_data() else 'None.'}</p>
    <p>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
