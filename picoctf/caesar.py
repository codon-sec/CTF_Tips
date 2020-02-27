target = r"jyvzzpunaolybipjvunfzpthre"
for i in range(26):
    print ("".join(chr((ord(x) - ord("a") + i ) % 26 + ord("a"))for x in target))
    picob956CTF{ts_plienlz_eno_cb}