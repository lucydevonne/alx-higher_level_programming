#!/usr/bin/python3

import requests

response = requests.get('https://alx-intranet.hbtn.io/status')

if response.status_code == 200:
    # Use a loop to add a tabulation before each line
    content = ""
    for line in response.content.decode('utf-8').splitlines():
        content += "\t" + line + "\n"
    print(content)
else:
    print(f"Error fetching status: {response.status_code}")
