C = "UFJKXQZQUNB"
K = "SOLVECRYPTO"

C = [ord(c)-ord("A") for c in C]
K = [ord(k)-ord("A") for k in K]
P = [(c-k) % 26 for c, k in zip(C, K)]
print("".join(chr(p+ord("A")) for p in P))
