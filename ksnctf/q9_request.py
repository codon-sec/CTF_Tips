import hashlib

algorithm = "MD5"
H_A1 = "c627e19450db746b739f41b64097d449"  # digest data
nonce = "YuJAb0TBBQA=2e06708e9050486fa219069ffcc6610d77e5d85c"  # random
nc = "00000001"  # count
cnonce = "888994e11c4d20ea"  # random
qop = "auth"
A2 = "GET:/q9/flag.html"
H_A2 = "9e2b6bca5d4d92f6ead358623df264c8"

param = "{}:{}:{}:{}:{}:{}:{}".format(H_A1, nonce, nc, cnonce, qop, A2, H_A2)
response = hashlib.md5(param.encode("utf-8")).hexdigest()
print(response)
