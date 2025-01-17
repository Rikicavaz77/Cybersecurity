import requests
import string

url = "http://127.0.0.1:124"
alphabet = list(string.ascii_letters)

for a in alphabet:
  headers = {
    'User-Agent': a
  }
  response = requests.get(f"{url}?pass={a}", headers=headers)
  print(f"Character: {a}\n{response.text}")

  lines = response.text.split("\n")
  if lines[-1] != '':
    print(f"Flag: {lines[-1]}")
    break
