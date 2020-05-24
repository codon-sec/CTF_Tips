# SECCON Begineers 2020
-  Date 2020/05/23(sat) 14:00 JST ~ 5/24 14:00
-  Style: Jeopardy

## Misc
### emoemoencode
    U+1F300-U+1F3FFまでが絵文字であるためUnicordの下8bitにASCII文字列を対応させている。
    U+1F363 → c (63) ascii
    絵文字から戻すときはUnicode表示(pythonのordもOK)にしてから0x1F300を引く

### readme
    Linux環境では、実行中のプロセスに関する情報は /proc/[PID] 以下に展開される
    動作環境はAlpine Linuxであり、
    /proc/self/environ を読むことで pwdコマンドを叩いたのと同じ状態になる(シンボリックリンク)
    Answer: `/proc/self/cwd/../flag`
    参考サイト: man page of proc

## web
### spy
    ログイン時の実行時間の差で利用ユーザを判断することができる。


### tweetstore
    配布コードを読んでいくとsql文を
    select url, text, tweeted_at from tweets where text like '%{search}%' order by tweet_at desc limit
    条件: searchは'が使えない。
    このlimitの後がインジェクション対策を怠っており攻撃が可能になっている。がsplitされるためクエリを投げられない。


### unzip


## pwn
    まだ練習不足であり、本CTFでは取り組まなかった。
    pythonのpwntoolを使用している人が多い印象。

## rev
    上に同じく、チームメンバーに任せたが次回は取り組みたい。
    angrを使用すると簡単に解けるらしい。

