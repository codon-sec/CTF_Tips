import hashlib

algorithm = "MD5"
H_A1 = "c627e19450db746b739f41b64097d449"  # digest data
nonce = "UyDCjkHBBQA=30175f4637b70cdcd2621e5aad7b7da2211a1db5"  # random
nc = "00000001"  # count
cnonce = "0a4f113b"  # random
qop = "auth"
A2 = "GET:/~q9/flag.html"
H_A2 = "ffffdd8b8029499600f95a69beb239c2"

param = "{}:{}:{}:{}:{}:{}:{}".format(H_A1, nonce, nc, cnonce, qop, A2, H_A2)
response = hashlib.md5(param.encode("utf-8")).hexdigest()
print(response)
