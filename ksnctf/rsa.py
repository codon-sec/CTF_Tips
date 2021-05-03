# python 3.8+ required
# this is a calculate m program
import binascii
import math

# 暗号化
# 1.巨大な素数p,qを用意しn=pqを計算
# 2.p-1とq-1の最小公倍数Lをもとめる
# 3.ed≡1(mod L) (ed-1がLの倍数である)となるようなedの組を求める
# 4.平文mを公開鍵(e,n)を使ってc = m^e mod n (mのe乗をnで割った余り)を計算して暗号化
# (n・e): 公開鍵
# (n・d): 秘密鍵


# 拡張ユークリッド互除法 x=e,y=L,gcd(x,y)=gcd(e,L)=1
def ex_euclid(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1

    while c1 != 0:
        m = c0 % c1
        q = c0 // c1

        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
    # return d
    return a0


# 復号化(mを求める)
# 1. n = pqを計算しておく
p = ""
q = ""
# 2. p-1とq-1の最小公倍数Lを求める L = lcm(a,b) = ab/gcd(a,b)
lcm = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
L = lcm
# 3. ed≡1(modL)(ed-1がLの倍数)となるedの組を求める
e = 65537
d = ex_euclid(e, L)
# 4. m = c^d mod n
c = ""
n = p * q
m = pow(c, d, n)

# to get the flag
# required python2
# print("%0512x" % m).decode("hex")
print(binascii.unhexlify(m.encode()))
