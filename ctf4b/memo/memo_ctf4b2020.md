# SECCON Begineers 2020
-  Date 2020/05/23(sat) 14:00 JST ~ 5/24 14:00
-  Style: Jeopardy

## Misc
### emoemoencode
    U+1F300-U+1F3FFまでが絵文字であるためUnicordの下8bitにASCII文字列を対応させている。
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

## pwn
    まだ練習不足であり、本CTFでは取り組まなかった。

## rev
    上に同じく、チームメンバーに任せたが次回は取り組みたい。

