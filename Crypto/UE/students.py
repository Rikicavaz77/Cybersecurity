import base64

def base64_decode(text):
  return base64.b64decode(text).decode('utf-8', errors='ignore')

with open("secret.txt", "r") as file:
  cipher = file.read().strip()
  print(cipher)

  decoded = cipher
  flag = ''
  iteration = 0
  while len(decoded) % 4 == 0:
    decoded = base64_decode(decoded)
    print(decoded)
    iteration += 1
    
    if "spritzCTF{" in decoded:
      flag = decoded
      break
  
  print(f"After decoding {iteration} times we get the flag: {flag}")
  