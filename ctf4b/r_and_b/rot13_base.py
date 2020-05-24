#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from os import getenv
import base64
import string
import os

FLAG = ""
alphabet = list(string.ascii_lowercase)

with open('encoded_flag', 'r') as f:
    encoded_flag = f.read()

# .indexは便利
def rot13(s):
    return alphabet[(alphabet.index(s) + 13) % 26]

def rot13_str(cipher):
    plain = ''
    for c in cipher:
        if c.isupper():
            plain += rot13(c.lower()).upper()
        elif c.islower():
            plain += rot13(c)
        else:
            plain += c
    return plain

print(encoded_flag)
while True:
    if encoded_flag[0] == 'R':
        encoded_flag = rot13_str(encoded_flag[1:])
        print(encoded_flag)
    elif encoded_flag[0] == 'B':
        encoded_flag = base64.b64decode(encoded_flag[1:]).decode()
        print(encoded_flag)
    else:
        break

print(FLAG)
