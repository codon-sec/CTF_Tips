import requests

headers = {'MY_HEADER': 'CTF_IS_FUN'}  # リクエストヘッダーを設定
param = {'my_query': '123'}  # クエリ文字列を設定
cookies = {'MY_COOKIE': 'abc'}  # cookieヘッダーの値を設定

response = requests.get('http://localhost:5000',
                        headers=headers, params=param, cookies=cookies)

if response.status_code == 200:
    print('[200 OK]', response.text)
else:
    print('[ERROR]', response.status_code)
