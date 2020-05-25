#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import urllib.parse

base_url = "http://tweetstore.quals.beginners.seccon.jp/"
split_s = 'https://twitter.com/user/status/'
split_e = '">Watch@Twitter'

# enumrate tweets
tweet_ids = []
for i in range(200):
    url = base_url + '?search=&limit=1+offset+' + str(i)
    res = requests.get(url)
    tweet_ids.append(res.text.split(split_s)[1].split(split_e)[0])
    print(chr(tweet_ids.index(tweet_id)),end='')

with open('tweet_ids.txt', 'w') as f:
    f.write(str(tweet_ids))
    url = base_url