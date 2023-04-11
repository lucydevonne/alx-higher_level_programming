#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

url = 'https://www.example.com'
try:
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f'Error code: {e.code}')
