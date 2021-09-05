# 脆弱性 nが小さく素因数分解が可能な場合

from Crypto.Util.number import inverse, long_to_bytes

c = 39119617768257067256541748412833564043113729163757164299687579984124653789492591457335
n = 13373801376856352919495636794117610920860037770702465464324474778341963699665011787021257
e = 65537
p = 3058517013146002381763962882964790715736519

q = n // p
d = inverse(e, (p-1)*(q-1))
m = pow(c, d, n)
print(long_to_bytes(m))
