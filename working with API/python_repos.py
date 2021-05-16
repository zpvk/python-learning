# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-12-30 22:50:41
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-12-30 23:07:21

# this code file shows you how to working with API
# in this project i'm going to use github API

#now we are going to find how many python projects on github and sote them by stars

#before working with this you have to install "request" package using pip module -- pip install requests --

import requests

# Make an API call and store response.

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept' : 'application/vnd.github.v3+jeson'}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

#Store API response in a variable

response_dict = r.jeson()

#Process results
print(response_dict.keys())
