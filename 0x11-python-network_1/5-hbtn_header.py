import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

if response.status_code == 200:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(f"X-Request-Id: {x_request_id}")
    else:
        print("X-Request-Id header not found in response")
else:
    print(f"Error fetching URL: {response.status_code}")

