

# 1. atd4`qdedtUpetepqeUdaaeUeaqau
# 2. agr を 0xeb で &-> c`b bk`kj`KbababcaKbacaKiacki

str1 = "atd4`qdedtUpetepqeUdaaeUeaqau"
str2 = "c`b bk`kj`KbababcaKbacaKiacki"

flag = ""

for i in range(len(str1)):
    flag += chr((ord(str1[i]) & 0x75) | (ord(str2[i]) & 0xeb))

print(flag)