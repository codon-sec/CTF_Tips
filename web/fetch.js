// 1.URIを指定する（後述のオプションを指定しない場合にはGETリクエストが送信される）
fetch('http://localhost:5000')
    // 2.レスポンスを受け取った際の処理の定義
    .then(response => {
        if (response.ok) {
            return response.text()
        } else {
            throw new Error()
        }
    })
    // 3. レスポンスが正常にテキストに変換できた際の処理の定義
    .then(text => console.log(text))
    .catch(error => console.error(error))
