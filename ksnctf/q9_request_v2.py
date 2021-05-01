import hashlib

import requests
from bs4 import BeautifulSoup as bs

# アクセス先URL
url = "http://ctfq.u1tramarine.blue/q9//flag.html"

# response用に用いるパラメタ
md5a1 = "c627e19450db746b739f41b64097d449"
nonce = ""
nc = "00000001"
cnonce = "5f70c9b7a0f15b7d"
qop = "auth"
a2 = "GET:/q9/flag.html"
md5a2 = "ffffdd8b8029499600f95a69beb239c2"

# Authorizationヘッダ作成に用いるパラメタ
username = "q9"
realm = "secret"
algorithm = "MD5"
uri = "/q9/flag.html"


# MD5ハッシュ値を返却する関数
def get_md5(arg):
    return hashlib.md5(arg.encode("utf-8")).hexdigest()


def main():
    # リクエストの送信
    auth_header = requests.get(url).headers["WWW-Authenticate"]

    # nonceの取得
    nonce = auth_header.split(" ")[2][7:-2]

    # responseの生成とハッシュ化
    not_md5_response = (
        md5a1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + md5a2
    )
    md5_response = get_md5(not_md5_response)

    # Authorizationヘッダの作成
    headers = {
        "Authorization": 'Digest username="'
        + username
        + '"'
        + ', realm="'
        + realm
        + '"'
        + ', nonce="'
        + nonce
        + '"'
        + ', uri="'
        + uri
        + '"'
        + ', algorithm="'
        + algorithm
        + '"'
        + ', response="'
        + md5_response
        + '"'
        + ", qop="
        + qop
        + ", nc="
        + nc
        + ', cnonce="'
        + cnonce
        + '"'
    }

    # ヘッダを付与してリクエストを生成
    answer = requests.get(url, headers=headers)

    answer_soup = bs(answer.text, "html.parser")
    print(answer_soup.p.text)


main()
